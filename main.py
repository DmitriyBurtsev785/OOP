# Задача 1

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


print(best_student.grades)


# Задача 2

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_of_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 9)
best_student.rate_of_lecturer(cool_lecturer,'Python', 10)


print(cool_lecturer.grades)
print(best_student.grades)


# Задача 3

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_of_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        for unpacking in list(best_student.grades.values()):
            average_mark = sum(unpacking)/len(unpacking)

        in_progress = ', '.join(best_student.courses_in_progress)
        finished_courses = ', '.join(best_student.finished_courses)
        students = (f'Студенты:\nИмя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {round(average_mark, 2)}\n'
                    f'Курсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished_courses}')
        return students


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        for unpacking in list(cool_lecturer.grades.values()):
            average_mark = sum(unpacking)/len(unpacking)

        lecturers = (f'Лекторы:\nИмя: {self.name}\n'
                     f'Фамилия: {self.surname}\nСредняя оценка за лекции: {round(average_mark, 2)}')
        return lecturers


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rewiewers = f'Ревьюеры:\nИмя: {self.name}\nФамилия: {self.surname}'
        return rewiewers


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 9)
best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 8)


some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

some_lecturer = Lecturer('Some', 'Buddy')
print(some_lecturer)


some_student = Student('Ruoy', 'Eman', 'your_gender')
print(some_student)


# Задача 3(2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []


    def rate_of_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def mid_grade(self):
      grades_all = []
      for key, value in self.grades.items():
        for grade in value:
          grades_all.append(grade)
      mid_grade = round(sum(grades_all)/len(grades_all), 2)
      return mid_grade


    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        students = (f'Студенты:\nИмя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {self.mid_grade()}\n'
                    f'Курсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished_courses}')
        return students


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.mid_grade() < other.mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def mid_grade(self):
      grades_all = []
      for key, value in self.grades.items():
        for grade in value:
          grades_all.append(grade)
      mid_grade = round(sum(grades_all)/len(grades_all), 2)
      return mid_grade


    def __str__(self):
        lecturers = (f'Лекторы:\nИмя: {self.name}\n'
                     f'Фамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}')

        return lecturers


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.mid_grade() < other.mid_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        rewiewers = f'Ревьюеры:\nИмя: {self.name}\nФамилия: {self.surname}'
        return rewiewers


cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JS']
best_student.courses_attached += ['Python', 'JS']
best_student.finished_courses += ['Введение в программирование']


best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 9)
best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 8)


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)


cool_lecturer_2 = Lecturer('Petr', 'Petrov')
cool_lecturer_2.courses_attached += ['Python']


average_student = Student('Vladimir', 'Vladimirov', 'your_gender')
average_student.courses_in_progress += ['Python', 'JS']
average_student.courses_attached += ['Python', 'JS']
average_student.finished_courses += ['Введение в программирование']


average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)


cool_reviewer_2 = Reviewer('Some_1', 'Buddy_1')
cool_reviewer_2.courses_attached += ['Python']


cool_reviewer_2.rate_hw(average_student, 'Python', 5)
cool_reviewer_2.rate_hw(average_student, 'Python', 5)
cool_reviewer_2.rate_hw(average_student, 'Python', 5)


print(cool_reviewer)
print(cool_lecturer)
print(best_student)


print(average_student < best_student)
print(cool_lecturer_2 < cool_lecturer)



# Задача 4


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.list_student_grades =[]


    def rate_of_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def mid_grade(self):
      grades_all = []
      for key, value in self.grades.items():
        for grade in value:
          grades_all.append(grade)
      mid_grade = round(sum(grades_all)/len(grades_all), 2)
      return mid_grade


    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        students = (f'Студенты:\nИмя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {self.mid_grade()}\n'
                    f'Курсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished_courses}')
        return students


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.mid_grade() < other.mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def mid_grade(self):
      grades_all = []
      for key, value in self.grades.items():
        for grade in value:
          grades_all.append(grade)
      mid_grade = round(sum(grades_all)/len(grades_all), 2)
      return mid_grade


    def __str__(self):
        lecturers = (f'Лекторы:\nИмя: {self.name}\n'
                     f'Фамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}')

        return lecturers


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.mid_grade() < other.mid_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        rewiewers = f'Ревьюеры:\nИмя: {self.name}\nФамилия: {self.surname}'
        return rewiewers


cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JS']
best_student.courses_attached += ['Python', 'JS']
best_student.finished_courses += ['Введение в программирование']


best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 9)
best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 8)


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)


cool_lecturer_2 = Lecturer('Petr', 'Petrov')
cool_lecturer_2.courses_attached += ['Python']


average_student = Student('Vladimir', 'Vladimirov', 'your_gender')
average_student.courses_in_progress += ['Python', 'JS']
average_student.courses_attached += ['Python', 'JS']
average_student.finished_courses += ['Введение в программирование']


average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)
average_student.rate_of_lecturer(cool_lecturer_2,'Python', 5)


cool_reviewer_2 = Reviewer('Some_1', 'Buddy_1')
cool_reviewer_2.courses_attached += ['Python']


cool_reviewer_2.rate_hw(average_student, 'Python', 5)
cool_reviewer_2.rate_hw(average_student, 'Python', 5)
cool_reviewer_2.rate_hw(average_student, 'Python', 5)


students = (best_student, average_student)
lecturers = (cool_lecturer, cool_lecturer_2)

def student():
    grades_all = []
    for current_student in students:
        for key, value in current_student.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    mid_grade = round(sum(grades_all) / len(grades_all), 2)
    print(f'Средняя оценка за ДЗ у студентов по курсу "Python" {mid_grade} ')


def lecturer():
    grades_all = []
    for current_lecturer in lecturers:
        # print(g)
        for key, value in current_lecturer.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    mid_grade = round(sum(grades_all) / len(grades_all), 2)
    print(f'Средняя оценка за ДЗ у лекторов по курсу "Python" {mid_grade} ')


student()
lecturer()
