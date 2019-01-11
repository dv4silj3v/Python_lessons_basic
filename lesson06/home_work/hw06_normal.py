# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Persons:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_official_name(self):
        official_name = self.surname + ' ' + self.name[0] + '. ' + self.patronymic[0] + '.'
        return official_name

    def get_full_name(self):
        full_name = self.name + ' ' + self.patronymic + ' ' + self.surname
        return full_name


class Student(Persons):
    def __init__(self, name, surname, patronymic, class_room, parents):
        Persons.__init__(self, name, surname, patronymic)
        self.class_room = class_room
        self.parents = parents


class Teacher(Persons):
    def __init__(self, name, surname, patronymic, teach_subject):
        Persons.__init__(self, name, surname, patronymic)
        self.teach_subject = teach_subject


class ClassRoom:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachers = teachers


teachers = [Teacher('Мария', 'Быкова', 'Сергеевна', 'математика'),
            Teacher('Глафира', 'Васильева', 'Павловна', 'русский'),
            Teacher('Валерия', 'Князева', 'Алексеевна', 'сопромат')]

class_rooms = [ClassRoom('9 a', [teachers[0], teachers[2]]),
               ClassRoom('9 в', [teachers[0]])]

parents = [Persons('Антон', 'Петров', 'Потапович'),
           Persons('Сергей', 'Иванов', 'Васильевич'),
           Persons('Софья', 'Петрова', 'Алексеевна'),
           Persons('Анастасия', 'Иванова', 'Владимировна')]

students = [Student('Егор', 'Петров', 'Антонович', class_rooms[0], [parents[0], parents[2]]),
            Student('Светлана', 'Петрова', 'Сергеевна', class_rooms[1], [parents[1], parents[3]])]

print("Классы в школе:")
for cl in class_rooms:
    print(cl.class_room)

which_class_room = '9 a'
print("Ученики в классе {}:".format(which_class_room))
for st in students:
    if st.class_room.class_room == which_class_room:
        print(st.get_official_name())

which_student = 'Егор Петров'
print("Предметы ученика {}:".format(which_student))
for st in students:
    if st.surname == which_student.split()[1] and st.name == which_student.split()[0]:
        for teacher in st.class_room.teachers:
            print(teacher.teach_subject)

which_student = 'Егор Петров'
print("ФИО родителей ученика {}:".format(which_student))
for st in students:
    if st.surname == which_student.split()[1] and st.name == which_student.split()[0]:
        for parent in st.parents:
            print(parent.get_full_name())

which_class_room = '9 в'
print("Учителя в классе {}:".format(which_class_room))
for cl in class_rooms:
    if cl.class_room == which_class_room:
        for teacher in cl.teachers:
            print(teacher.get_full_name())
