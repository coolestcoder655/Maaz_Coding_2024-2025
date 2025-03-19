info = {
    "name": "Maaz",
    "age": 12,
    "nameofSchool": "Forestwood",
    "marks": [97, 95, 100],
    "learningPython": True,
    "weatherinDecimals": 97.68,
    "topicsOfToday'sClass": ("dictionaries", ),
    True: "meansYes",
    (97, 95, 100): "theBestMarks",
    97.69: "notTheWeatherInDecimals",
    "name": "Jonathan"
}

# 2 Methods

print(info["name"])

print(info.get("name", "Nope."))

# Print Entire Dictonaries

for key, value in info.items():
    print(f"Key: {key}, Value: {value}")

info["age2"] = 13

print(info["age2"])
