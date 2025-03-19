student = {
    "name": "Maaz",
    "subjects": {
        "phy": 98,
        "math":100,
        "science": 96
    }
}
student2 = {
    "name": "Alice",
    "age": 12
}
print(student.keys())
print(len(student))
print(student.values())
print(student["subjects"]["math"])

print(list(student.keys()))

print(list(student.items())[0])

print(student.get("name2"))

# print(student["name2"])

student.update(student2)

print(student)