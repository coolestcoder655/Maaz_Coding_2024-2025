from datetime import date

class Exam:
    def __init__(self, subject: str, score: int, max_score: int = 100, exam_date: date = date.today()) -> None:
        self.subject = subject
        self.score = score
        self.max_score = max_score
        self.exam_date = exam_date

        if score < 0:
            raise Exception(f'The score ({score}) cannot be less than 0.')
        
        if score > max_score:
            raise Exception(f'The score ({score}) cannot be greater than the max score ({max_score}).')
        return
        

class Student:
    def __init__(self, name: str, exams: list[Exam]) -> None:
        self.name = name
        self.exams = exams
    
        temp = list()
        for exam in self.exams:
            temp.append(exam.score)
        
        self.grade = sum(temp) / len(temp)
        return


    def addExam(self, toAdd: Exam):
        self.exams.append(toAdd)
        return