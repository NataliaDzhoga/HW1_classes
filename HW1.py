class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_grades = 0
        self.mean_grade = 0

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

    def get_mean_grade(self):
        self.mean_grade = 0
        for grade in self.grades.values():
            self.sum_grades += float(*grade)
        self.mean_grade = self.sum_grades/len(self.grades.values())
        return self.mean_grade

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_mean_grade()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')

    def __eq__(self, other):
        return(self.get_mean_grade() == other.get_mean_grade())

    def __lt__(self, other):
        return (self.get_mean_grade() < other.get_mean_grade())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.sum_grades = 0
        self.mean_grade = 0

    def get_mean_grade(self):
        self.mean_grade = 0
        for grade in self.grades.values():
            self.sum_grades += float(*grade)
        self.mean_grade = self.sum_grades/len(self.grades.values())
        return self.mean_grade

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_mean_grade()}\n')

    def __eq__(self, other):
        return(self.get_mean_grade() == other.get_mean_grade())

    def __lt__(self, other):
        return (self.get_mean_grade() < other.get_mean_grade())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached
                and (course in student.courses_in_progress
                     or course in student.finished_courses)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Ksenia', 'Chap', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Alex', 'King')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Введение в программирование']

cool_lecturer2 = Lecturer('Nil', 'Cooper')
cool_lecturer2.courses_attached += ['Python']

cool_reviewer = Reviewer('Mike', 'Fisher')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['Введение в программирование']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9.7)
cool_reviewer.rate_hw(best_student, 'Введение в программирование', 10)

cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Git', 9.8)
cool_reviewer.rate_hw(best_student2, 'Введение в программирование', 9.9)

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Git', 9.8)
best_student.rate_lecture(cool_lecturer, 'Введение в программирование', 9.9)
best_student.rate_lecture(cool_lecturer2, 'Python', 8)

# print(f'Студент {best_student.name} {best_student.surname} '
      # f'имеет следующие оценки: {best_student.grades}')
# print(f'Лектор {cool_lecturer.name} {cool_lecturer.surname} '
      # f'имеет оценки по курсам: {cool_lecturer.grades}')
# print(cool_reviewer)
# print(cool_lecturer)
# print(cool_lecturer2)
# print(best_student)
# print(best_student2)

if cool_lecturer == cool_lecturer2:
    print('Средние оценки двух лекторов одинаковые')
elif cool_lecturer < cool_lecturer2:
    print('Оценки второго лектора выше')
else:
    print('Оценки первого лектора выше')

if best_student == best_student2:
    print('Средние оценки двух студентов одинаковые')
elif best_student < best_student2:
    print('Оценки второго студента выше')
else:
    print('Оценки первого студента выше')
