# class Student:
#     def __init__(self, tired, progress):
#         self.tired = tired
#         self.progress = progress
#
#
#     def study(self):
#         if self.tired < 85:
#             self.tired += 15
#         else:
#             self.tired = 100
#
#
#         self.progress += 10
#
#     def relax(self):
#         if self.tired > 5:
#             self.tired -= 5
#         else:
#             self.tired = 0
#
#     def is_done(self):
#         if self.progress >= 100:
#             print ("Студент выучился")
#         else:
#             print ("Нуждается в образовании")
#
#     def demotivated(self):
#         return self.tired > 100
#
#
# student_ilya = Student(tired=15, progress=10)
# student_dima = Student(tired=5, progress=20)
#
# print(student_ilya.tired)
# print(student_ilya.progress)
# student_ilya.study()
# student_ilya.study()
# print(student_ilya.tired)
# print(student_ilya.progress)
#
# print("######")
#
# print(student_dima.tired)
# print(student_dima.progress)
# student_dima.study()
# print(student_dima.tired)
# print(student_dima.progress)

# while student_dima.demotivated ():



# class Animal:
#
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def make_noice(self):
#         pass
#
# class Cat(Animal):
#     def make_noice(self):
#         print("Meow")
#
# class Dog(Animal):
#     def make_noice(self):
#         print("Gav")


# cat1 = Cat(name="Barsik", health=100)
# print(cat1.name)
# print(cat1.make_noice())

# dog = Dog(name="Barsik", health=100)
# cat = Cat(name="Sharik", health=200)
#
#
# dog.make_noice()
# cat.make_noice()






# class Animal:
#
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def _inner_method(self):
#         print ("Выполнился внутренний метод")
#
#
#     def get_name(self):
#         self.inner_method()
#         return self.name
#
#
# animal = Animal ("Барсик", 100)
#
# animal._inner_method()

























