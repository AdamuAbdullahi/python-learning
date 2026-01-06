from person import Person

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"Course: {self.course}")