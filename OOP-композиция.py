# MONTHS_IN_YEAR = 12
#
# class Salary:
#
#     def __init__(self, month_pay):
#         self.month_pay = month_pay
#
#     def get_year_salary (self):
#         return self.month_pay * MONTHS_IN_YEAR
#
#     def unsed_method ():
#         print ("Этой строки никогда не должно быть")
#
#
# class Employee:
#
#     def __init__(self, month_pay, bonus):
#         self.bonus = bonus
#         self.salary = Salary(month_pay)
#
#     def annual_salary (self):
#         return self.salary.get_year_salary() + self.bonus
#
#
# employee = Employee(month_pay=50000, bonus=10000)
# annual_salary = employee.annual_salary()
# print(annual_salary)



class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** (1/2)

point = Point(x=5, y=7)
print (point.distance())

point = Point(x=9, y=9)
print (point.distance())

point = Point(x=15, y=17)
print (point.distance())

