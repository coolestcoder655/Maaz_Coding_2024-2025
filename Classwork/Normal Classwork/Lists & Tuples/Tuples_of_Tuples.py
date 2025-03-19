# Question: You have a tuple of tuples representing student names and their scores:

# Write code to:
# 	1.	Convert the tuple of tuples into a list of lists.
# 	2.	Update Daisy’s score to 70.
# 	3.	Convert it back to a tuple of tuples and print the result.

students_scores = (("Alice", 88), ("Bob", 76), ("Charlie", 90), ("Daisy", 65))

studentScoresList = list(students_scores)

for student in studentScoresList:
    studentList = tuple(student)
    studentScoresList.pop(studentScoresList.index(student))
print(studentScoresList)

for student in studentScoresList:
    if student[0] == "Daisy":
        studentList = list(student)
        studentList[1] = 70
        studentTuple = tuple(studentList)
        studentScoresList.pop(studentScoresList.index(student))
        studentScoresList.append(studentTuple)
        studentScoresTuple = tuple(studentScoresList)


print(studentScoresTuple)