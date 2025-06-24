

# Import libraries for GUI and plotting
import tkinter as tk
from tkinter import messagebox as mb
import matplotlib.pyplot as plt # type: ignore
from dayClass import Day
from tkcalendar import Calendar # type: ignore
from tkinter import ttk

# Global variables
date: str = ''  # Currently selected date

# Initialize main application window
root = tk.Tk()
root.title('Weather Application')
root.geometry('300x400')

# Application state variables
dayCounter: int = 0  # Counter for tracking number of days recorded

# Debug mode: True = load sample data, False = start with empty data
debug: bool = True

# Initialize weather data storage
if not debug: 
    dayList: list[Day] = list()  # Empty list for production use

if debug: 
    # Sample data for testing and demonstration
    dayList: list[Day] = [
        Day("6/25/25", "65", "13", "57", "90"),
        Day("6/26/25", "65", "13", "57", "90"),
        Day("6/27/25", "65", "13", "57", "90"),
        Day("6/28/25", "65", "13", "57", "90"),
        Day("6/29/25", "65", "13", "57", "90"),
    ]

# =========================================================================
# FUNCTION DEFINITIONS
# =========================================================================

# This function adds a day to the data. This data will be used by plt to generate a graph.

def addDay():
    """
    Add a new day of weather data to the dayList variable.
    Retrieves data from the entry fields and creates a Day class inside dayList.
    Shows error message if the data validation fails.
    """
    global dayCounter, date, dateChanged
    # Get values from entry fields
    temp = temperatureEntry.get()
    humidity = humidityEntry.get()
    windSpeed = windEntry.get()
    rainFall = rainEntry.get()
        
    try:
        # Create new Day object with the collected data
        today: Day = Day(date, temp, humidity, windSpeed, rainFall)
        dayList.append(today)
    except Exception as e:
        # Show error message if Day creation fails (invalid data)
        mb.showerror('Error Constructing Date', message=e) # type: ignore

    # Clear fields only when not in debug mode
    if not debug: clearFields()

    return

def generateSummary():
    """
    Calculate and display statistical summaries of all weather data.
    Requires at least 5 days of data to generate meaningful statistics.
    Shows max, min, average values for temperature, humidity, wind, and rainfall.
    """
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
    
    return

def openGraphs(dates: list[str] = [], temperatures: list[int] = []):
    global dayList

    averageTemperature = sum(day.temp for day in dayList) / len(dayList) if dayList else 0
    averageHumidity = sum(day.humidity for day in dayList) / len(dayList) if dayList else 0
    averageWind = sum(day.wind for day in dayList) / len(dayList) if dayList else 0
    averageRain = sum(day.rain for day in dayList) / len(dayList) if dayList else 0

    averages: list[float] = [averageTemperature, averageHumidity, averageWind, averageRain]
    averagesLabels: list[str] = ['Avg Temp', 'Avg Humidity', 'Avg Wind Speed', 'Avg Rainfall']

    # Line plot in its own window
    plt.figure(figsize=(8, 4)) # type: ignore
    plt.plot(range(1, len(dates) + 1), temperatures, marker='o') # type: ignore
    plt.xticks(range(1, len(dates) + 1), dates)
    plt.title('Daily Temperature Trend') # type: ignore
    plt.xlabel('Day') # type: ignore
    plt.ylabel('Temperature (℉)') # type: ignore
    plt.tight_layout() # type: ignore
    plt.show(block=False) # type: ignore

    # Bar plot in its own window
    plt.figure(figsize=(8, 4)) # type: ignore
    plt.bar(range(1, len(dates) + 1), temperatures) # type: ignore
    plt.xticks(range(1, len(dates) + 1), dates)
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

    return

def plotGraphs():
    """
    Generate and display three types of visualizations:
    1. Line graph showing daily temperature trends
    2. Bar graph showing temperature comparison
    3. Pie chart showing weather averages distribution
    Requires at least 5 days of data.
    """
    if len(dayList) < 5:
        mb.showerror('Insufficient Data', 'Please add at least 5 days of data before plotting graphs.') # type: ignore
        return
    
    # Extract dates and temperatures for plotting
    dates = [day.dayDate for day in dayList]
    temperatures = [day.temp for day in dayList]
    openGraphs(dates, temperatures) # This will show all three plots in separate windows

    return

def selectDate():
    """
    Open a calendar modal for date selection.
    Updates the global 'date' variable with the selected date.
    Uses tkcalendar widget for user-friendly date picking.
    """
    global date, dateChanged
    # Create modal window
    import datetime
    modal = tk.Toplevel(root)
    modal.geometry("400x300")
    modal.title("Select Date")
    today = datetime.date.today()

    # Add Calendar
    cal = Calendar(modal, selectmode='day', year=today.year, month=today.month, day=today.day)
    cal.pack(pady=20)  # type: ignore

    def setDate():
        nonlocal cal, modal
        global date
        date = cal.get_date()
        modal.destroy()
        return

    # Add Select button to modal
    select_btn = tk.Button(modal, text='Select', command=setDate)
    select_btn.pack(pady=10)

    modal.grab_set()  # Make modal truly modal
    modal.wait_window()  # Wait until modal is closed
    dateChanged = False
    return

def clearFields():
    """
    Clear all input entry fields to prepare for new data entry.
    Removes text from temperature, humidity, wind, and rainfall fields.
    """
    temperatureEntry.delete(0, tk.END)
    humidityEntry.delete(0, tk.END)
    windEntry.delete(0, tk.END)
    rainEntry.delete(0, tk.END)
    return

def clearDays():
    """
    Reset all application data to initial state.
    Clears the dayList, resets counters, and clears input fields.
    Useful for starting fresh data collection.
    """
    global dayCounter, dayList, date
    dayCounter = 0
    dayList.clear()
    date = ''
    dateEntry.config(text='Select Date')
    clearFields()
    return


def viewAllData():
    """
    Display all recorded weather data in a scrollable modal window.
    Shows date, temperature, humidity, wind speed, and rainfall for each day.
    Uses grid layout with proper scrolling functionality.
    """
    global dayList
    modal = tk.Toplevel(root)
    modal.geometry("150x400")
    modal.title("View All Data")
    
    # Create a frame for scrollable content
    canvas = tk.Canvas(modal)
    scrollbar = tk.Scrollbar(modal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Use grid for canvas and scrollbar
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")
    
    # Configure grid weights
    modal.grid_rowconfigure(0, weight=1)
    modal.grid_columnconfigure(0, weight=1)
    
    row = 0
    for day in dayList:
        # Day header
        tk.Label(scrollable_frame, text=f'--- Day {row//6 + 1} ---', font=("Arial", 10, "bold")).grid(padx=10, pady=(10,5), column=0, row=row, columnspan=2)
        row += 1
        
        tk.Label(scrollable_frame, text=f'Date: {day.dayDate}').grid(padx=10, pady=2, column=0, row=row, sticky="w")
        row += 1
        
        tk.Label(scrollable_frame, text=f'Temperature: {day.temp}℉').grid(padx=10, pady=2, column=0, row=row, sticky="w")
        row += 1
        
        tk.Label(scrollable_frame, text=f'Humidity: {day.humidity}%').grid(padx=10, pady=2, column=0, row=row, sticky="w")
        row += 1
        
        tk.Label(scrollable_frame, text=f'Wind: {day.wind} km/h').grid(padx=10, pady=2, column=0, row=row, sticky="w")
        row += 1
        
        tk.Label(scrollable_frame, text=f'Rain: {day.rain} mm').grid(padx=10, pady=2, column=0, row=row, sticky="w")
        row += 1
        
        # Add separator using grid
        separator = ttk.Separator(scrollable_frame, orient='horizontal')
        separator.grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
        row += 1

    modal.grab_set()  # Make modal truly modal
    modal.wait_window()  # Wait until modal is closed
    return

# =========================================================================
# GUI LAYOUT AND WIDGET CREATION
# =========================================================================
# All GUI elements are arranged using grid layout manager
# Layout structure: Title at top, then input fields, then action buttons

# Main title header inside the window
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), fg="blue")
title_label.grid(column=1, row=0, columnspan=2, pady=(10, 20))

# Input Fields Section
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

# Action Buttons Section
# Row 6: Data entry and field management
addDayButton: tk.Button = tk.Button(root, text='Add Day', command=addDay)
addDayButton.grid(padx=10, pady=10, column=1, row=6)

clearFieldsButton: tk.Button = tk.Button(root, text='Clear Fields', command=clearFields)
clearFieldsButton.grid(padx=10, pady=10, column=2, row=6)

# Row 7: Analysis and visualization
generateSummaryButton: tk.Button = tk.Button(root, text='Generate Summary', command=generateSummary)
generateSummaryButton.grid(padx=10, pady=10, column=1, row=7)

plotGraphsButton: tk.Button = tk.Button(root, text='Plot Graphs', command=plotGraphs)
plotGraphsButton.grid(padx=10, pady=10, column=2, row=7)

# Row 8: Data management and viewing
clearDaysButton: tk.Button = tk.Button(root, text='Clear Days', command=clearDays)
clearDaysButton.grid(padx=10, pady=10, column=1, row=8)

viewAllDataButton: tk.Button = tk.Button(root, text='View All Data', command=viewAllData)
viewAllDataButton.grid(padx=10, pady=10, column=2, row=8)

# =========================================================================
# START APPLICATION
# =========================================================================
# Start the main event loop - keeps the window open and responsive
root.mainloop()