class Employee:
    def __init__(self, first, last, phone, pay):
        self.first = first
        self.last = last
        self.phone = phone
        self.pay = pay

    @property
    def fullName(self):
        return f"{self.first} {self.last}"
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"


class Developer(Employee):
    def __init__(self, first, last, phone, pay, language):
        super().__init__(first, last, phone, pay)
        self.language = language


dev_1 = Developer("Mark", "Cuban", 214-732-2569, 60000, "python")

print(dev_1.email)