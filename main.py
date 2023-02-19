class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grades(self):
        buffer = 0
        count = 0
        for courses, grades in self.grades.items():
            for grade in grades:
                buffer += grade
                count += 1
        average_grade = buffer/count
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.get_average_grades()}' \
              f'\nКурсы в процессе изучения:{self.courses_in_progress}' \
              f'\nЗавершенные курсы:{self.finished_courses}'

        return res

    def student_comparison(self, foe):
        if isinstance(foe, Student):
            first = self.get_average_grades()
            second = foe.get_average_grades()
            if first > second:
                return f'{self.name} {self.surname} круче'
            else:
                return f'{foe.name} {foe.surname} круче'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def get_average_grades(self):
        buffer = 0
        count = 0
        for courses, grades in self.grades.items():
            for grade in grades:
                buffer += grade
                count += 1
        average_grade = buffer / count
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self.get_average_grades()}'
        return res

    def lectures_comparison(self, foe):
        first = self.get_average_grades()
        second = foe.get_average_grades()
        if isinstance(foe, Lecturer):
            if first > second:
                return f'{self.name} {self.surname} круче'
            else:
                return f'{foe.name} {foe.surname} круче'
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


patric_baitman = Student('Патрик', 'Бэйтман', 'мужской')
gunness_belle = Student('Ганнесс', 'Белль', 'женский')
vladimir_lenin = Reviewer('Владимир', 'Ленин')
lavrenty_beria = Reviewer('Лаврентий', 'Берия')
harry_potter = Lecturer('Гарри', 'Поттер')
ronald_wizly = Lecturer('Рональд', 'Уизли')

patric_baitman.courses_in_progress += ['Python']
patric_baitman.courses_in_progress += ['Git']
gunness_belle.courses_in_progress += ['Python']
gunness_belle.courses_in_progress += ['Git']

harry_potter.courses_attached += ['Python']
ronald_wizly.courses_attached += ['Git']

vladimir_lenin.courses_attached += ['Python']
vladimir_lenin.courses_attached += ['Git']
lavrenty_beria.courses_attached += ['Python']
lavrenty_beria.courses_attached += ['Git']

patric_baitman.finished_courses += ['Основы программирования']
gunness_belle.finished_courses += ['Основы программирования']

vladimir_lenin.rate_hw(patric_baitman, 'Python', 8)
lavrenty_beria.rate_hw(patric_baitman, 'Git', 9)
vladimir_lenin.rate_hw(gunness_belle, 'Python', 10)
lavrenty_beria.rate_hw(gunness_belle, 'Git', 6)

patric_baitman.rate_lecturer(harry_potter, 'Python', 9)
patric_baitman.rate_lecturer(ronald_wizly, 'Git', 8)
gunness_belle.rate_lecturer(harry_potter, 'Python', 5)
gunness_belle.rate_lecturer(ronald_wizly, 'Git', 4)

student_list = []
student_list.append(patric_baitman.__dict__)
student_list.append(gunness_belle.__dict__)
# print(student_list)
course_name = "Python"

lecturer_list = []
lecturer_list.append(harry_potter.__dict__)
lecturer_list.append(ronald_wizly.__dict__)
# print(lecturer_list)


def get_average_student_grade_on_course(student_list, course_name):
    buffer = 0
    count = 0
    for student_data in student_list:
        if course_name in student_data.get('courses_in_progress'):
           for grade in student_data.get('grades')[course_name]:
                buffer += grade
                count += 1
    average_grade = buffer/count
    return average_grade


def get_average_lecturer_grade_on_course(lecturer_list, course_name):
    buffer = 0
    count = 0
    for lecturer_data in lecturer_list:
       if course_name in lecturer_data.get('courses_attached'):
            for grade in lecturer_data.get('grades')[course_name]:
                buffer += grade
                count += 1
    average_grade = buffer / count
    return average_grade


print('Студенты:')
print(patric_baitman)
print('\n')
print(gunness_belle)
print('\n')

print('Эксперты:')
print(vladimir_lenin)
print('\n')
print(lavrenty_beria)
print('\n')

print('Лекторы:')
print(harry_potter)
print('\n')
print(ronald_wizly)
print('\n')

print('Сравним студентов и лекторов по средним оценкам:')
print(patric_baitman.student_comparison(gunness_belle))
print(harry_potter.lectures_comparison(ronald_wizly))
print('\n')


print('Выведем средние оценки среди студентов по курсу Python:')
print(get_average_student_grade_on_course(student_list, course_name))
print('Выведем средние оценки среди студентов по курсу Git:')
course_name = 'Git'
print(get_average_student_grade_on_course(student_list, course_name))
print('\n')

course_name = 'Python'
print('Выведем средние оценки среди лекторов по курсу Python:')
print(get_average_lecturer_grade_on_course(lecturer_list, course_name))
print('Выведем средние оценки среди лекторов по курсу Git:')
course_name = 'Git'
print(get_average_lecturer_grade_on_course(lecturer_list, course_name))
