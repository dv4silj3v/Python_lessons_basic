# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import json

class Timetable:
    def __init__(self, name, surname, hours_worked):
        self.name = name
        self.surname = surname
        self.hours_worked = hours_worked

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name


class Workers(Timetable):
    def __init__(self, name, surname, hours_worked, salary, hours_month):
        Timetable.__init__(self, name, surname, hours_worked)
        self.salary = salary
        self.hours_month = hours_month

    def calc_hours_diff(self):
        hours_diff = int(self.hours_month) - int(self.hours_worked)

    def calc_worker_salary(self):


statement = []
with open('data/workers', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i >= 1:
            line_column = line.strip('\n').split()
            statement.append(Workers(line_column[0], line_column[1], line_column[2], line_column[4]))

hoursof = []
with open('data/hours_of', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i >= 1:
            line_column = line.strip('\n').split()
            hoursof.append(Timetable(line_column[0], line_column[1], line_column[2]))

payroll = []
for worker_line in hoursof:
    for worker_payroll in statement:
        if worker_line.name == worker_payroll.name and worker_line.surname == worker_payroll.surname:
            if int(worker_payroll.hours_month) >= int(worker_line.hours_worked):
                payroll_salary = int(worker_payroll.salary) * int(worker_line.hours_worked) / int(worker_payroll.hours_month)
                payroll.append({worker_line.name, worker_line.surname, payroll_salary})
            if int(worker_payroll.hours_month) < int(worker_line.hours_worked):
                payroll_salary = int(worker_payroll.salary) + 2 * (int(worker_payroll.salary)/int(worker_payroll.hours_month)) *(int(worker_line.hours_worked) - int(worker_payroll.hours_month))

with open('data/payroll.json', 'w', encoding='UTF-8', ) as f:
    json.dump(payroll, f, ensure_ascii=False)



