import json
import random
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- Configurable Variables --- #
JOB_TITLE = "Software Engineer"
RESUME_PATH = "./resume.docx" # Path to your resume file

JOB_SITES = [
    "https://example-jobsite1.com",  # Replace with real sites
    "https://example-jobsite2.com",
    "https://example-jobsite3.com"
]

applied_jobs = []

# --- Setup Stealth Chrome --- #
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--incognito")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

# Fake user-agent (mimics a real user)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
)

driver = uc.Chrome(options=options)

# --- Helpers --- #
def random_sleep(min_t=1.0, max_t=3.0):
    time.sleep(random.uniform(min_t, max_t))

def scroll_like_human():
    for i in range(random.randint(2, 5)):
        driver.execute_script("window.scrollBy(0, 300);")
        random_sleep(0.5, 1.2)

def apply_to_job_site(site_url):
    try:
        driver.get(site_url)
        random_sleep(2, 4)

        # Search for job
        search_input = driver.find_element(By.NAME, "q")  # ← Change selector
        search_input.send_keys(JOB_TITLE)
        search_input.send_keys(Keys.RETURN)

        random_sleep(3, 6)
        scroll_like_human()

        job_cards = driver.find_elements(By.CLASS_NAME, "job-card")[:3]  # ← Update class
        for card in job_cards:
            try:
                job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
                job_title = card.find_element(By.CLASS_NAME, "job-title").text
                company_name = card.find_element(By.CLASS_NAME, "company").text
                salary = "Not listed"
                try:
                    salary = card.find_element(By.CLASS_NAME, "salary").text
                except:
                    pass

                if job_link is not None:
                    driver.get(job_link)
                    random_sleep(3, 5)
                    scroll_like_human()
                else:
                    print(f"[!] job_link is None for card: {job_title} at {company_name}")

                # Try to upload resume
                try:
                    upload = driver.find_element(By.XPATH, "//input[@type='file']")
                    upload.send_keys(RESUME_PATH)
                except:
                    print(f"[!] Could not upload resume at {job_link}")

                # Try to click Apply
                try:
                    apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
                    apply_button.click()
                except:
                    print(f"[!] Could not click Apply at {job_link}")

                applied_jobs.append({
                    "name": company_name,
                    "job_title": job_title,
                    "expected_salary": salary,
                    "job_link": job_link
                })

                random_sleep(2, 4)
            except Exception as e:
                print("[!] Error in job card:", e)

    except Exception as e:
        print("[!] Error loading site:", site_url, "=>", e)
        input("[!] CAPTCHA might have appeared. Solve it and press Enter...")

# --- Run --- #
for site in JOB_SITES:
    apply_to_job_site(site)

# --- Save JSON --- #
with open("applied_jobs.json", "w") as f:
    json.dump(applied_jobs, f, indent=4)

print("[✓] Applied to jobs. Results saved to applied_jobs.json")
driver.quit()
