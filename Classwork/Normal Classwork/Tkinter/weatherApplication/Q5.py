# You are building a Weather Monitoring Tool for a small meteorology research team. The app will be used to record daily weather data for a specific location and generate visualizations based on that data.
# You need to develop a full application with a Tkinter GUI to:
# Calculate statistical summaries such as max, min, and average for each weather element.
# Visualize the data using:
# Line graph (daily temperature trend)
# Bar graph (rainfall comparison)
# Pie chart (distribution of weather focus – temp, humidity, etc.)

import tkinter as tk
from tkinter import messagebox as mb
import matplotlib.pyplot as plt # type: ignore
from dayClass import Day
from tkcalendar import Calendar # type: ignore

date: str = ''

root = tk.Tk()
root.title('Weather Application')
root.geometry('500x500')

dayCounter: int = 1

dayList: list[Day] = []

debug: bool = True  # Set to True for debugging purposes

# This function adds a day to the data. This data will be used by plt to generate a graph.

def addDay():
    global dayCounter, date
    
    dayCounter += 1
    temp = temperatureEntry.get()
    humidity = humidityEntry.get()
    windSpeed = windEntry.get()
    rainFall = rainEntry.get()

    try:
        today: Day = Day(date, temp, humidity, windSpeed, rainFall)
        dayList.append(today)
    except Exception as e:
        mb.showerror('Error Constructing Date', message=e) # type: ignore

    if not debug: clearFields()

def generateSummary():
    if len(dayList) < 5:
        mb.showerror('Insufficient Data', 'Please add at least 5 days of data before generating a summary.') # type: ignore
        return
    
    max_temp = max(day.temp for day in dayList)
    min_temp = min(day.temp for day in dayList)
    avg_temp = sum(day.temp for day in dayList) / len(dayList)

    max_humidity = max(day.humidity for day in dayList)
    min_humidity = min(day.humidity for day in dayList)
    avg_humidity = sum(day.humidity for day in dayList) / len(dayList)

    max_wind = max(day.wind for day in dayList)
    min_wind = min(day.wind for day in dayList)
    avg_wind = sum(day.wind for day in dayList) / len(dayList)

    max_rain = max(day.rain for day in dayList)
    min_rain = min(day.rain for day in dayList)
    avg_rain = sum(day.rain for day in dayList) / len(dayList)
    
    total_rainfall = sum(day.rain for day in dayList)
    highest_wind_speed_day = max(dayList, key=lambda d: d.wind)

    summary = (
        f"Max Temperature: {max_temp}℉\n"
        f"Min Temperature: {min_temp}℉\n"
        f"Average Temperature: {avg_temp:.2f}℉\n"
        f"Total Rainfall: {total_rainfall} mm\n"
        f"\n\nMax Humidity: {max_humidity}%\n"
        f"Min Humidity: {min_humidity}%\n"
        f"Average Humidity: {avg_humidity:.2f}%\n"
        f"Max Wind Speed: {max_wind} km/h\n"
        f"Min Wind Speed: {min_wind} km/h\n"
        f"Average Wind Speed: {avg_wind:.2f} km/h\n"
        f"Max Rainfall: {max_rain} mm\n"
        f"Min Rainfall: {min_rain} mm\n"
        f"Average Rainfall: {avg_rain:.2f} mm"
        f"Highest Wind Speed Day: {highest_wind_speed_day.dayDate} with {highest_wind_speed_day.wind} km/h"
    )
    
    mb.showinfo('Weather Summary', summary) # type: ignore

def openGraphs(dates: list[str] = [], temperatures: list[int] = []):
    global dayList

    averageTemperature = sum(day.temp for day in dayList) / len(dayList) if dayList else 0
    averageHumidity = sum(day.humidity for day in dayList) / len(dayList) if dayList else 0
    averageWind = sum(day.wind for day in dayList) / len(dayList) if dayList else 0
    averageRain = sum(day.rain for day in dayList) / len(dayList) if dayList else 0

    averages = [averageTemperature, averageHumidity, averageWind, averageRain]
    averagesLabels = ['Avg Temp', 'Avg Humidity', 'Avg Wind Speed', 'Avg Rainfall']

    # Line plot in its own window
    plt.figure(figsize=(8, 4)) # type: ignore
    plt.plot(range(1, len(dates) + 1), temperatures, marker='o') # type: ignore
    plt.title('Daily Temperature Trend') # type: ignore
    plt.xlabel('Day') # type: ignore
    plt.ylabel('Temperature (℉)') # type: ignore
    plt.tight_layout() # type: ignore
    plt.show(block=False) # type: ignore

    # Bar plot in its own window
    plt.figure(figsize=(8, 4)) # type: ignore
    plt.bar(range(1, len(dates) + 1), temperatures) # type: ignore
    plt.title('Temperature Bar Graph') # type: ignore
    plt.xlabel('Day') # type: ignore
    plt.ylabel('Temperature (℉)') # type: ignore
    plt.tight_layout() # type: ignore
    plt.show(block=False) # type: ignore

    # Pie chart in its own window
    plt.figure(figsize=(6, 6)) # type: ignore
    plt.pie(averages, labels=averagesLabels, autopct='%1.1f%%') # type: ignore
    plt.title('Weather Averages Distribution') # type: ignore
    plt.tight_layout()  # type: ignore
    plt.axis('equal')  # type: ignore
    plt.show(block=False) # type: ignore

def plotGraphs():
    if len(dayList) < 5:
        mb.showerror('Insufficient Data', 'Please add at least 5 days of data before plotting graphs.') # type: ignore
        return
    
    dates = [day.dayDate for day in dayList]
    temperatures = [day.temp for day in dayList]
    openGraphs(dates, temperatures) # This will show all three plots in separate windows

def selectDate():
    global date
    # Create modal window
    import datetime
    modal = tk.Toplevel(root)
    modal.geometry("400x300")
    modal.title("Select Date")
    today = datetime.date.today()

    dayToday = today.day + dayCounter

    # Add Calendar
    cal = Calendar(modal, selectmode='day', year=today.year, month=today.month, day=dayToday)
    cal.pack(pady=20)  # type: ignore

    def setDate():
        nonlocal cal, modal
        global date
        date = cal.get_date()
        modal.destroy()

    # Add Select button to modal
    select_btn = tk.Button(modal, text='Select', command=setDate)
    select_btn.pack(pady=10)

    modal.grab_set()  # Make modal truly modal
    modal.wait_window()  # Wait until modal is closed

def clearFields():
    temperatureEntry.delete(0, tk.END)
    humidityEntry.delete(0, tk.END)
    windEntry.delete(0, tk.END)
    rainEntry.delete(0, tk.END)

def clearDays():
    global dayCounter, dayList, date
    dayCounter = 0
    dayList.clear()
    date = ''
    dateEntry.config(text='Select Date')
    clearFields()

# Date Entry Field
tk.Label(root, text='Date: ',).grid(padx=10, pady=10, column=1, row=1)
dateEntry: tk.Button = tk.Button(root, command=selectDate, text=date if date != '' else 'Select Date')
dateEntry.grid(column=2, row=1)

# Temperature Entry Field
tk.Label(root, text='Temperature (℉): ',).grid(padx=10, pady=10, column=1, row=2)
temperatureEntry: tk.Entry = tk.Entry(root)
temperatureEntry.grid(column=2, row=2)

# Humidity Entry Field
tk.Label(root, text='Humidity (%): ',).grid(padx=10, pady=10, column=1, row=3)
humidityEntry: tk.Entry = tk.Entry(root)
humidityEntry.grid(column=2, row=3)

# Wind-Speed Entry Field
tk.Label(root, text='Wind-Speed (km/h): ',).grid(padx=10, pady=10, column=1, row=4)
windEntry: tk.Entry = tk.Entry(root)
windEntry.grid(column=2, row=4)

# Rainfall Entry Field
tk.Label(root, text='Rainfall (mm): ',).grid(padx=10, pady=10, column=1, row=5)
rainEntry: tk.Entry = tk.Entry(root)
rainEntry.grid(column=2, row=5)

# Add Day Button
addDayButton: tk.Button = tk.Button(root, text='Add Day', command=addDay)
addDayButton.grid(padx=10, pady=10, column=1, row=6)

# Clear Fields Button
clearFieldsButton: tk.Button = tk.Button(root, text='Clear Fields', command=clearFields)
clearFieldsButton.grid(padx=10, pady=10, column=2, row=6)

# Generate Summary Button
generateSummaryButton: tk.Button = tk.Button(root, text='Generate Summary', command=generateSummary)
generateSummaryButton.grid(padx=10, pady=10, column=1, row=7)

# Plot Graphs Button
plotGraphsButton: tk.Button = tk.Button(root, text='Plot Graphs', command=plotGraphs)
plotGraphsButton.grid(padx=10, pady=10, column=2, row=7)

# Clear Days Button
clearDaysButton: tk.Button = tk.Button(root, text='Clear Days', command=clearDays)
clearDaysButton.grid(padx=10, pady=10, column=1, row=8)


root.mainloop()