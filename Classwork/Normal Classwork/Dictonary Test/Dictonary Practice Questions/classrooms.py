# 4.	Count Classrooms Needed:
# Given a list of subjects for students, count how many unique classrooms are needed:

subjects = ["python", "math", "science", "math", "java", "c++", "c", "javascript", "science", "PE", "science"]


"""
subjects2 = []

for x in subjects:
    if x not in subjects2:
        subjects2.append(x)

print(len(subjects2))

print(subjects2)
"""
# Another Approach

print(len(set(subjects)))