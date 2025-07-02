import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIGURATION ===
location = "Port Angeles, Washington"
checkin_date = "2025-07-09"
checkout_date = "2025-07-10"
adults = 3
children = 2
rooms = 2  # optional, 2 rooms could increase chance of multiple beds

# === SETUP SELENIUM ===
options = Options()
# options.add_argument("--start-maximized") # You can enable normal mode here
options.add_argument("--headless")  # You can enable headless mode here

driver = webdriver.Chrome(service=ChromeService(), options=options)
wait = WebDriverWait(driver, 15)

checkin = datetime.strptime(checkin_date, "%Y-%m-%d")
checkout = datetime.strptime(checkout_date, "%Y-%m-%d")

# === URL Builder ===
def build_url(offset=0):
    return (
        f"https://www.booking.com/searchresults.html?"
        f"ss={location.replace(' ', '+')}"
        f"&checkin_year={checkin.year}&checkin_month={checkin.month}&checkin_monthday={checkin.day}"
        f"&checkout_year={checkout.year}&checkout_month={checkout.month}&checkout_monthday={checkout.day}"
        f"&group_adults={adults}&group_children={children}&no_rooms={rooms}"
        f"&offset={offset}"
    )

# === Scrape One Page ===
def scrape_current_page():
    time.sleep(3)
    hotels_data = []

    results = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    for result in results:
        try:
            name = result.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
            price_elem = result.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')
            price = price_elem.text if price_elem else "N/A"
            href = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
            link = href.split("?")[0] if href else "N/A"

            try:
                room_desc = result.find_element(By.CSS_SELECTOR, '[data-testid="room_info"]').text
            except:
                room_desc = "N/A"

            # Optional: filter by text hinting at multiple beds
            if any(term in room_desc.lower() for term in ["2 beds", "3 beds", "multiple beds", "2-bedroom", "suite"]):
                hotels_data.append({
                    "name": name,
                    "price": price,
                    "link": link,
                    "room_description": room_desc
                })

        except Exception as e:
            continue

    return hotels_data

# === MAIN SCRAPER LOOP ===
all_hotels = []
seen_links = set()
offset = 0
page = 1

while True:
    print(f"🔎 Scraping page {page} (offset {offset})...")
    driver.get(build_url(offset))

    # Accept cookies if prompted
    try:
        accept = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        accept.click()
    except:
        pass

    hotels = scrape_current_page()
    if not hotels:
        print("🚫 No more results or blocked.")
        break

    new_hotels = [h for h in hotels if h["link"] not in seen_links]

    if not new_hotels:
        print("✅ All pages scraped (no new listings found).")
        break

    for hotel in new_hotels:
        seen_links.add(hotel["link"])
        all_hotels.append(hotel)

    offset += 25
    page += 1
    time.sleep(2)

# === SAVE TO JSON ===
output_file = "port_angeles_hotels.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_hotels, f, indent=2, ensure_ascii=False)

print(f"\n✅ Finished. {len(all_hotels)} hotels saved to {output_file}")
driver.quit()
