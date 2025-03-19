# WAP to count the number of students with the "A” grade in the following tuple. Store the above values in a list & sort them from "A” to "D” . [”C” , "D” , "A” , "A” , "B” , "B” , "A”]

grades = ["C", "D", "A", "A", "B", "B", "A"]
gradesToSort = ["A", "B", "C", "D"]

for x in gradesToSort:
    print(f"{x}: {grades.count(x)} Found")

grades.sort()
grades.reverse()
print(grades)