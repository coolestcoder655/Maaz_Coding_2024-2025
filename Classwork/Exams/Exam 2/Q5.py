# • Question: You are given a list of lists containing students’ 
# names and their grades:
# students = [["Alice", 85], ["Bob", 76], ["Charlie", 
# 90], ["David", 60]]
#   Write a function that:
# 1. Calculates the average grade of the students. 
# 2. Prints the names of students who scored above average.

students = [
    ("Alice", 85), ("Bob", 76), ("Charlie", 90), ("David", 60)
]

def averageCalculator():
    grades = []
    average = 0
    for x in students:
        grades.append(x[1])
    for y in grades:
        average = average + y
    
    average = average / len(students)

    print("You students have an average of: ", average)
    print("The Following Students Passed: ")
    for z in students:
        if z[1] >= 70:
            print(z[0])

averageCalculator()