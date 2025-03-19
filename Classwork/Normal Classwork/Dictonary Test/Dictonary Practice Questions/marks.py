# 5.	Store Marks from User Input:
# Write a program to input marks of three subjects from the user and store them in a dictionary. Use the subject name as the key and marks as the value.

marks = {

}

for x in range(3):
    subject = input("Enter the Subject: \n ")
    marksInt = input("Enter the Marks: \n ")
    marks[subject] = int(marksInt)

print(marks)