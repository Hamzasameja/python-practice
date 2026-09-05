class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def add_grade(self,grade):
        self.grade.append(grade)

    def calculate_average(self):
        return sum(self.grade) / len(self.grade)

    def report(self):
        print(self.name + "'s average grade is: " + str(self.calculate_average()))
        print("average grade is: " + str(self.calculate_average()))

student1 = student("Hamza", [85, 90, 78])
student1.report()

student1.add_grade(92)
student1.report()