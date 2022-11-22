# # destructuring
# l = [1, 2, 3, 4]
# a, _, b, c = l
# print(a, b, c)  # 1 3 4
# d, *_, f = l
# print(d, f, _)  # 1 4 [2, 3]
# *_, g = l
# print(g)  # 4
#
# # unpacking
# l2 = [*l]
# print(l2)  # [1, 2, 3, 4]
#
# d = {
#     'name': 'Pole',
#     'age': 12,
#     'house': 23
# }
#
#
# def test(name, age, **kwargs):
#     print(name, age)  # Pole 12
#     print(kwargs)  # {'house': 23}
#
#
# test(**d)
#
#
# def test2(**kwargs):
#     print(kwargs)
#
#
# test2(**d)  # {'name': 'Pole', 'age': 12}
#
#
# def test3(name, age, house):
#     print(name, age, house)
#
#
# test3(*d)  # name age house
# test3(**d)  # Pole 12 23
#
#
# # decorators
# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 12)
#         func(*args, **kwargs)
#         print('*' * 12)
#
#     return inner
#
#
# @decor
# def greeting():
#     print('Hello )')
#
#
# greeting()
#
# import time
#
# def time_decor(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print('---->.....')
#         print(time.time() - start_time, 's')
#     return inner
#
# @time_decor
# def gen_list(n):
#     return [i for i in range(n)]
# list_3 = gen_list(10000000)
#
# # scope
# name = 'Bob'
#
#
# def a():
#     global name  # за допомогою цього слова показуємо що ми будемо
#     # використовувати зміну за межами нащої функції
#     name = 'Kira'
#     print(name)
#
#
# a()
# print(name)
# print(globals())
# # з global виводиться Kira Kira
# # без виводиться Kira Bob
#
#
# var = 'global'
#
#
# def a():
#     var = 'a'
#     print(locals())  # {'var': 'a'}
#
#     def b():
#         var = 'b'
#         print(locals())  # {'var': 'b'}
#
#         def c():
#             var = 'c'
#             print(locals())  # {'var': 'c'}
#
#         c()
#
#     b()
#
#
# a()
# print(var, '1')  # global
#
#
# def a1():
#     var = 'a'
#
#     def b1():
#         var = 'b'
#
#         def c1():
#             var = 'c'
#             print(var)
#
#         c1()
#         print(var)
#
#     b1()
#     print(var)
#
#
# a1()
# print(var, '2')  # global
#
#
# # послідовність виконання c b a
#
# @decor
# def a2():
#     var = 'a'
#
#     def b2():
#         var = 'b'
#
#         def c2():
#             nonlocal var  # за допомогою цієї команди зміна var стає не локальною
#             # та впливає на роботу вкладеності на рівень вище,
#             # тобто var буде дорівнювати c в функції b2()
#             var = 'c'
#             print(var)
#
#         c2()
#         print(var)
#
#     b2()
#     print(var)
#
#
# a2()
# print(var, '3')
#
#
# # послідовність виконання c c a
#
# @decor
# def a2():
#     var = 'a'
#
#     def b2():
#         # var='b'
#         def c2():
#             nonlocal var  # за допомогою цієї команди зміна var стає не локальною,
#             # шукає зміну var, не знайшовши її в функції b2(),  йде на одну вкладеність вище
#             # , тобто var буде дорівнювати c в функції b2() та a2()
#             var = 'c'
#             print(var)
#
#         c2()
#         print(var)
#
#     b2()
#     print(var)
#
#
# a2()
# print(var, '4')
# # послідовність виконання c c c
#
# var = 'var'
#
#
# @decor
# def a2():
#     global var
#     var = 'a'
#
#     def b2():
#         # var='b'
#         def c2():
#             # global var  #
#             var = 'c'
#             print(var)
#
#         c2()
#         print(var)
#
#     b2()
#     print(var)
#
#
# a2()
# print(var, '5')
# # послідовність виконання c a a a 5
#
# var = 'var'
#
#
# @decor
# def a2():
#     var = 'a'
#
#     def b2():
#         def c2():
#             # global var  #
#             var = 'c'
#             print(var)
#
#         c2()
#         print(var)
#
#     b2()
#     print(var)
#
#
# a2()
# print(var, '6')
#
#
# # з global послідовність виконання c a a с 6
# # без global послідовність виконання c a a var 6
#
# # closure
#
# def closure():
#     password = 1234
#
#     def get_password():
#         return password
#
#     def set_password(new_password):
#         nonlocal password
#         password = new_password
#
#     return [get_password, set_password]
#
#
# get_password, set_password = closure()
# print(get_password())
# set_password(1000)
# print(get_password())
#
from typing import Callable, NewType, TypedDict

# t: tuple[str, ...] = ('1', '2')
#
# User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)
# user_2 : User = { 'name': 'Bob', 'age':23}
#
# def test(name: list[int]) -> str:
#     return 'sd'
#
#
# test([1])
#
#
# def pro(a: str | int | bool) -> str | None:
#     return None
#
#
# def counter() -> Callable[[], int]:
#     count = 0
#
#     def inner() -> int:
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# count_1 = counter()
# count_2 = counter()
# print(count_1())
# print(count_1())
# print(count_2())
# print(count_2())
#
# UserId = NewType('UserId', int)
#
#
# def func(user_id: UserId):
#     print(user_id, 'UserID')
#
#
# func(UserId(12))


# # lambda
# print('********************* LAMBDA *****************')
# user = [
#     {'name': 'Pole', 'age': 12},
#     {'name': 'Ann', 'age': 22},
#     {'name': 'Fes', 'age': 42},
#     {'name': 'Pole', 'age': 32},
#     {'name': 'Pole', 'age': 1},
# ]
#
#
# def sort_by_age(item):
#     return item['age']
#
#
# print(sorted(user, key=sort_by_age), end='\n')
# user.sort(key=lambda item: item['age'], reverse=True)
# print('sort --->>>>', user)
# print(sorted(user, key=lambda item: item['age'], reverse=True))
# # filter
# f = filter(lambda x: x['age'] < 20, user)
# print(list(f))
#
# user.sort(key=lambda value: value['name'], reverse=True)
# print(user)
# # map
# arr = [1, 2, 3, 4]
# map = map(lambda a: a + 1, arr)
# res = list(map)
# print(res)


# це своєрідна моделька
# UserP = TypedDict('UserP', {'name': str, 'age': int, 'status': bool}, total=False)
# user: UserP = {'name': 'Lis', 'age': 23, 'status': True}


##########################################
# HOME WORK

#######################################
def note_book() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


add, all = note_book()
add('wake up')
add('poo')
add('drink water')
print(all())


# розбити по розрядах число
def expanded_form(num: int) -> str:
    st = str(num)
    zero_count = len(st) - 1
    return ' + '.join(v + '0' * (zero_count - i) for i, v in enumerate(st) if v != '0') + f' = {st}'


print(expanded_form(232))


# зробити декоратор який буде рахувати кількість запусків функції
def decor_f(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print('-=-' * 12)
        print(f'{count=}')
        func(*args, **kwargs)
        print('-=-' * 12)
        count += 1

    return inner


@decor_f
def func1():
    print('func1')


@decor_f
def func2():
    print('func2')


func1()
func1()

func2()
func2()
func2()
