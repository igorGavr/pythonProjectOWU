
## 4 Наслідування
## 5 Інкапсуляція
## 6 Полиморфизм
## 7 Абстрактні класи
## 8 Статичні та клас-методи
#

# 1 __repr__
class User:
    count = 0 # атрибут класу
    __slots__ = ('name', 'age', 'address', 'num')

    def __init__(self, name, age):
        self.name = name  # атрибут обєкту
        self.age = age
        self.num = 0

    @property
    def name_len(self):
        return len(self.name)

    @classmethod
    def get_len_name(cls, name):
        return len(name)

    # статік метод не залежить від класу та обєкту класу ,
    # це просто додатковий функціонал
    @staticmethod
    def get_upper_name(name):
        return name.upper()

    def __str__(self):
        return f'{self.name} __str__'
    def __repr__(self):
        return f'{self.name}~~{self.age} __repr__'
    def __len__(self):
        return len(self.name)
    def __call__(self):
        print('мене визвали!!!')
        return 10_000
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        if self.num >= len(self.name):
            raise StopIteration
        self.num += 1
        return self.num


print(User.count)  # 0
user = User('Pip', 12)
print(user.name, user.age)
users = [User('tim', 12), User('bob', 23)]
print(users)
print(user)
print(len(user))
user.address = 'Lviv' # 2 можливість динамічно додавати поля класу та виводити екземпляр класу
# відпрацювання методу __call__
user() # мене визвали!!!
print(user()) # 10_000

#  дандр-метод __slots__
# _ допомагає в визначенні полів (інші поля вписати неможливо
# крім тих які є в __slots__), а також економить память

print(next(user))
print(next(user))
print(next(user))
# raises StopIteration
# print(next(user))

print(user.name_len)
print(User.name_len)
print(user.get_len_name('dfhdhsfh'))
print(User.get_len_name('d3434hsfh'))
print(user.get_upper_name(user.name))
print(User.get_upper_name('popi'))





# 4 Наслідування
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Tools:
#     def greeting(self):
#         print('Hello')
# class Tools2:
#     def greeting(self):
#         print('Hello2')
#
# class User(Human, Tools2, Tools):
#     def __init__(self, name, age, house):
#         super().__init__(name, age)
#         self.house = house
#
#
# user = User('Max', 15, 88)
#
# user.greeting()
#
# print(user.name)
# print(user.age)
# print(user.house)


# 5 Інкапсуляція  Инкапсуляция позволяет ограничить доступ
# к какой-либо функции в классе. Благодаря такому подходу
# злоумышленники или же мы сами не сможем случайно или
# намерено вызвать или изменить метод.
# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def delete_name(self):
#         del self.__name
#
#
# user = User('Max')
#
# print(user.get_name())
# user.set_name('Kira')
# print(user.get_name())
# user.delete_name()
# print(user.get_name())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)


# 6 Полиморфизм - это способность выполнять действие над
# объектом независимо от его типа. Это обычно реализуется
# путем создания базового класса и наличия двух или более
# подклассов, которые все реализуют методы с одинаковой
# сигнатурой.

# class Shape:
#     def area(self):
#         pass
#
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * 0.5
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#
# shapes: list[Shape] = [Triangle(3, 4, 5), Rectangle(3, 4)]
#
# for i in shapes:
#     print(i.area())
#     print(i.perimetr())


# 7 Абстрактні класи - дозволяють реалізувати примусовість використання методів батьківського класу в дочірніх
# Плюси -
#       * не можна створити екземпляр абстрактного класу
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b / self.c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return self.a + self.b


# 8 Статичні та клас-методи
# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     # звичайний метод
#     def set_name(self, new_name):
#         self.name = new_name
#
#     @staticmethod
#     def greeting(name):
#         print(f'Hello, {name}')
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# user = User('Max', 15)
# User.greeting()
# user.greeting()
# User.set_name(user, 'Kira')
# User.get_count()
# print(user.name)


# 9 Перегрузка методів
# Сінгел Тон - патерн в програмуванні коли при створенні
# декількох екземплярів класу ми отримуємо один екземпляр
# __new__ -
# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# user1 = User('Max')
# user2 = User('Kira')
#
# print(user1.name)
# print(user2.name)
#
# user2.name = 'Max'
#
# print(user1.name)
# print(user2.name)
#
# print(id(user1))
# print(id(user2))


# class Test:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, multi):
#         return self.value * multi
#
#
# test = Test(5)
# print(test(3))
# print(test.value)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other):
#         return self.age * other.age
#
#     def __lt__(self, other):
#     # def __lte__(self, other):
#     # def __gt__(self, other):
#     # def __gte__(self, other):
#     # def __eq__(self, other):
#     # def __neq__(self, other):
#         return self.age + other.age
# #
# #
# user = User('Max', 15)
# user2 = User('Kira', 30)
# # print(len(user))
# # print(user + user2)
# # print(user - user2)
# print(user < user2)
