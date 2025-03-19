# WAP to determine the grade a student gets based on marks.
marks = int(input("Please Put The Student's Marks Here:"))

phrase = "The student got a "

if (marks >= 100):
    print(phrase +  "A+!!")
elif (marks >= 90 and marks < 100):
    print(phrase + "A!")
elif (marks>=80 and marks < 90):
    print(phrase + "B!")
elif (marks>= 70 and marks < 80):
    print(phrase + "C!")
elif (marks < 70):
    print (phrase + "F.")