# 7.	Manage Student Records:
# Create a nested dictionary to store student records. Each student should have their name, age, and marks in a subject.

records = {
    "student1": {
        "name": "Alice",
        "age": 13,
        "subjects": {
            "math": 100,
            "english": 100,
            "history": 100,
            "science": 100
        }
    },
    "student2": {
        "name": "James",
        "age": 12,
        "subjects": {
            "math": 78,
            "english": 54,
            "history": 87,
            "science": 94
        }
    },
    "student3": {
        "name": "47",
        "age": 14,
        "subjects": {
            "math": 85,
            "english": 87,
            "history": 86,
            "science": 89
        }
    }
}

print(list(records.values()))


print(records.get("student2")["subjects"]["english"])

print(records["student2"]["subjects"]["english"])