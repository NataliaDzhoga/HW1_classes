class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if grade < 0 or grade > 10:
            return 'Ошибка'
        elif (isinstance(lecturer, Lecturer) and
              course in lecturer.courses_attached and
              (course in self.courses_in_progress or
               course in self.finished_courses)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Alex', 'King')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Mike', 'Fisher')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

print(f'Студент {best_student.name} {best_student.surname} '
      f'имеет следующие оценки: {best_student.grades}')
print(f'Лектор {cool_lecturer.name} {cool_lecturer.surname} '
      f'имеет оценки по курсам: {cool_lecturer.grades}')
