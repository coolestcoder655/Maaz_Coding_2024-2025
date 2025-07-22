from datetime import date

class Exam:
    # Init Function: Initalizes A New Exam Object
    def __init__(self, subject: str, score: int, max_score: int = 100, exam_date: date = date.today()) -> None:
        self.subject = subject
        self.score = score
        self.max_score = max_score
        self.exam_date = exam_date


        # Checks if Score Less Than 0 or Greater than Max Score
        if score < 0:
            raise Exception(f'The score ({score}) cannot be less than 0.')
        
        if score > max_score:
            raise Exception(f'The score ({score}) cannot be greater than the max score ({max_score}).')
        return
        


class Student:
    # Init Function: Initalizes A New Student Object
    def __init__(self, name: str, exams: list[Exam]) -> None:
        self.name = name
        self.exams = exams
    

        # Finds Average Score
        temp = list()
        for exam in self.exams:
            temp.append(exam.score)
        
        self.grade = sum(temp) / len(temp)

        return


    # Creates a New Exam Inside the self.exams List.
    def addExam(self, toAdd: Exam):
        self.exams.append(toAdd)
        return