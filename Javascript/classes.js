class Employee {
    constructor(firstName, lastName, age, salary, jobTitle) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.salary = salary;
        this.jobTitle = jobTitle;
    }

    getFullName() {
        return `${this.firstName} ${this.lastName}`
    }
    raise(percentage) {
        this.salary *= 1 + percentage;
    }

}

obj = new Employee("Maaz", "Khan", 25, 100000, "Software Engineer");


