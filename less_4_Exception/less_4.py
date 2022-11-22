## 1 Exception
## 2 Generators
## 3 Робота з файлами
## 4 match

## 1 Exception
# try:
#     kjshfkshf
# except NameError:
#     print('Error')
#
# print('next')

# def div(a, b):
#     return a / b

# try:
#     # input()
#     # print(div(3, 0))
#     raise ZeroDivisionError
# except ZeroDivisionError as err:
#     print('sssss')
#     print(err)
# except KeyboardInterrupt:
#     print('keyError')
# except Exception:
#     print('My Error')
# else:
#     print('Ok')
# finally:
#     print('finish')
#
#
# print('next')

# class MyCustomError(Exception):
#     pass


## 2 Generators
# l = [i for i in range(50000000)]
# input()


# g = (i for i in range(5))
#
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
#
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# Генератори у вигляді функції
# def gen(name):
#     for ch in name:
#         print('start')
#         yield ch
#         print('finish')
#
#
# g = gen('Maxi')
#
# print(next(g))
# print(next(g))
# print(type(g))
# # #
# print(next(g))
# print('jshfsghfkj')
# print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'finish!!!!!!!!!!!'
#
#
#
# g = gen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'worker {i}-Team1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'worker {i}-Team2'
#
#
# teams = [gen1(4), gen2(6)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


# import uuid
#
# print(uuid.uuid1())
# def gen_jpg_file_name():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
# g = gen_jpg_file_name()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.__count < self.__length:
#             res = self.__count
#             self.__count+=1
#             return res
#         raise StopIteration
#
# my_range = MyRange(5)
# # for i in my_range:
# #     print(i)
# # for i in my_range:
# #     print(i)
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# 3 Робота з файлами
# file  = open('1.txt')
# print(file.read())

# try:
#     with open('1.txt') as file:
#         # print(file.read(3))
#         # print(file.tell())
#         # print(file.readline())
#         print(file.readlines())
# except (Exception,):
#     pass

# при -- mode='w' -- якщо такого файлу немає то він створиться,
# якщо такий файл є то він перезапишеться
# при -- mode='a' -- дописуємо файл, якщо файл не існує то створить його
# try:
#     with open('files/1.txt', mode='r+') as file:
#         print(file.readline())
#         print(file.tell())      # показує де ми знаходимся
#         file.seek(file.tell())  # ставимо курсор в це місце
#         file.write('1, 2, 3')
#         # file.write('hello1\nHi\n')
#         # file.writelines(['hello\n', 'Hi\n'])
# except (Exception,):
#     pass


# file_name = 'pes.jpg'
# try:
#     with open(file_name, 'rb') as file, open('my_python.jpg', 'wb') as res:
#         image = file.read()
#         res.write(image)
# except (Exception,):
#     pass


from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int, 'status': bool})

user:User = {'name': 'Max', 'age': 12, 'status': True}
import json
import pickle
# try:
#     with open('user.json', 'w') as file:
#         json.dump(user, file)
# except (Exception,):
#     pass

# try:
#     with open('user.json', 'r') as file:
#         user:User = json.load(file)
#         print(user['name'])
# except (Exception,):
#     pass


# try:
#     with open('user.db', 'wb') as file:
#         pickle.dump(user, file)
# except (Exception,):
#     pass
# try:
#     with open('user.db', 'rb') as file:
#         user:User = pickle.load(file)
#         print(user['name'])
# except (Exception,):
#     pass


## 4 match
# num = input('Enter num: ')
# match num:
#     case '1':
#         print('1')
#     case '2':
#         print('2')
#     case _:
#         print('default')


# source = ['down', 500]
#
# match source:
#     case 'top' | 'left' as action, value:
#         print(action, value)
#     case 'down', 500 as value:
#         print('down case', f'{value=}')
#     case _:
#         print('default')