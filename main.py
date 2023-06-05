class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lk(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{self.grades}\n{self.grades}\nКурсы в процессе изучения:{', '.join(self.courses_in_progress)}\nЗавершенные курсы:{', '.join(self.finished_courses)}"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __lt__(self, other):
        return self.grades < other.grades

    def __eq__(self, other):
        return self.grades == other.grades

    def __le__(self, other):
        return self.grades <= other.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.grades}"

    def __lt__(self, other):
        return self.grades < other.grades

    def __eq__(self, other):
        return self.grades == other.grades

    def __le__(self, other):
        return self.grades <= other.grades

    def avg_grades(self, student, course, grade):
        if course in student.grades:
            student.grades[course] += [grade]
        # else:
        #         student.grades[course] = [grade]
        return self.grades

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_reviewer = Reviewer('Mark', 'Tven')
some_reviewer1 = Reviewer('Den', 'Dava')
some_reviewer.courses_attached += ['Python']
some_reviewer1.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy', )
some_lecturer1 = Lecturer('Brus', 'Li', )
some_lecturer.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', )
some_student1 = Student('Nata', 'Serg', )
some_student.courses_in_progress += ['Python', 'Git']
some_student1.courses_in_progress += ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student1.finished_courses = ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer1.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer1.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer1.rate_hw(some_student, 'Python', 9)

some_student.rate_lk(some_lecturer, 'Python', 9)
some_student1.rate_lk(some_lecturer, 'Python', 9)
some_student.rate_lk(some_lecturer, 'Python', 9)
some_student1.rate_lk(some_lecturer, 'Python', 9)
some_student.rate_lk(some_lecturer, 'Python', 9)
some_student1.rate_lk(some_lecturer, 'Python', 9)

student_list = [some_student, some_student1]
lecturer_list = [some_student, some_student1]
reviewer_list = [some_student, some_student1]


def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(some_student)
print(some_student1)
print(some_lecturer1)
print(some_lecturer)