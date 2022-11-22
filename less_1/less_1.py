# string

# string = 'text'
# string = "text"
# string = 'name = \'Vasyl\''
#
# print(string)

# st = "*"*50
#
# print(st)
# name = 'Max'
# age = 18
# weight = 70.5
#
# string = 'Hello, my name is Max, I`m 18 and my weight 70.5kg'
# string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + 'kg'
# string = 'Hello, my name is %s, I`m %d and my weight %fkg' % (name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight {}kg'.format(name, age, weight)
# string = 'Hello, my name is {name}, I`m {age} and my weight {weight}kg'.format(age=age, weight=weight, name=name)
# string = f'Hello, my name is {name}, I`m {age} and my weight {weight}kg'
# string = f'hello, my name is {name}, I`m ll {age} and my weight {weight}kg'

# print(string.index('ll', 3,10))
# print(string.find('llsss', 5))
# print(string.count('l'))
# string = string.capitalize()
# string = string.upper()
# string = string.isupper()
# string = string.lower()
# string = string.islower()
#
# print(string)

# print('hello world'.title())
# print('Hello world'.swapcase())
# print('asfd2'.isalpha())
# print('2'.isdigit())
# print('2sdf'.isalnum())
# print('hello'.endswith('lo'))
# print('hello'.startswith('lo'))
#
# print(['    sdfhg   '.strip()])
# print(['aaa    sdfhg  aaa'.strip('a ')])
# print(['  sdfhg  '.rstrip()])
# print(['  sdfhg  '.lstrip()])
# print('hello-world'.split('-'))
# # print('hello-world'.split(''))
#
# # print('hello'[2])
# # print(list('hello world'))
# # print('hello is hello'.partition('is'))
# print('hello'[::2])
#
# strs = ['hello', 'world']
#
# join = '-'.join(strs)
#
# print(join)

#
# name = 'vit'
# age = 23
# print('name = {n} \nage = {a}'.format(a = age, n = name))
# print(f'name = {name.center(5,"*")} \nage = {age+2}')
#
# print(list('hello'))  # ['h', 'e', 'l', 'l', 'o']
# l1 = [1, 2]
# l3 = l1
# print(l1)
# print(l3)   #[1,2] отримуємо два посилання на одний обєкт
#
# # при зміні елементів
# l3[0] = 0
# print(l1)  #[0,2]
# print(l3)  #[0,2]
#
# l4 = list(l1)    # тут створюється копія
# print(l4)   #[0, 2]
# l5 = l4[:]   # тут створюється копія
# print('l5 - ', l5)
#
# ##########################################
# # Methods of list
#
# #######################################
# print('------------# Methods of list------------------')
# print(min([1, 2, 3]))
# print(max([1, 2, 3]))
# print(sorted([1, 2, 3], reverse=True))  # сортує та повертає новий Ліст
#
# list = [1, 2, 3, 4]
# list.append(11)   # додаємо елемент в кінець
# list.insert(0, 'wew')  # додаємо елем в певне місце
# del list[0]    # видаляємо певний елем
# list.pop()   # видаляємо та повертаємо останній елем
# list.remove(3)  # видаляємо по значенню
# list.index(2)   # повертаємо індекс елем
# list_2 = ['qw', 'qww']
# list.extend(list_2)  # розширюємо ліст
# # list.sort()  працює лише з однотипними даними
# list.reverse()  # розвертаємо ліст
# print(list)
# print(list[:3])   # беремо зріз з 0 по 3 елем
# print(list[:3:2])  # беремо зріз з 0 по 3 елем з кроком 2
# print(list[::2])  # беремо зріз з 0 по останній елем з кроком 2
# print(list[::-1])  # реверс

# ##########################################
# # TUPLES
#
# #######################################
# # не можна змінювати розмір та значення
# # займає менше памяті ніж ліст
# tuple_1 = (1, 2, 3, 4)
# tuple_2 = 1, 2, 3, 4
# tuple_3 = tuple('hello')
# print(tuple_3)   # ('h', 'e', 'l', 'l', 'o')
#
# print(tuple_1[0])  # 1
# print(tuple_1.index(1))  # 0
# print(tuple_1.count(1))  # 1

# ##########################################
# # DICT
#
# #######################################
# d1 = {'name' : 'Bob', 'age' : 23}
# print(d1['age'])
# d2 = dict(name = 'Bob', age = 23)
# print(d2)
# d3 = dict([('name', 'Bob'), ('age', 34)])
# d3['email'] = 'gam.com'
# print(d3)  # {'name': 'Bob', 'age': 34, 'email': 'gam.com'}
# d = dict.fromkeys([1, 2, 'df'], 1)
# print(d)
# print('df' in d) # True
# print(d3.get('name'))   # Bob якщо ключа не існує то поверне None
# print(d3.get('nam', 'gil'))   # якщо ключа не знайдено то повертається дефолтне значення
#
# print(d3.items())   # dict_items([('name', 'Bob'), ('age', 34), ('email', 'gam.com')])
# print(d3.keys())    # dict_keys(['name', 'age', 'email'])
# print(d3.values())  # dict_values(['Bob', 34, 'gam.com'])
# print(list(d3.items()))  #  [('name', 'Bob'), ('age', 34), ('email', 'gam.com')]
# print(list(d3.keys()))    #  ['name', 'age', 'email']
# print(list(d3.values()))    #  ['Bob', 34, 'gam.com']
#
# pop = d3.pop('name')  # видаляємо ключ і повертаємо його значення
# print(pop)   # Bob
# print(d3)    # {'age': 34, 'email': 'gam.com'}
# popitem = d3.popitem()  # видаляємо останю пару ключ-значення
# print('popitem - ',popitem)   # popitem -  ('email', 'gam.com')
# print(d3)  # {'age': 34}
# d3.setdefault('age', 100) # нічого не зміниться бо такий ключ вже є
# d3.setdefault('farm', True)  # додаємо нову пару ключ значення
# d3.update({'house': 2})
# print(d3)  # {'age': 34, 'farm': True, 'house': 2}
# d3 |= {'big' : True}   # теж саме що update

# ##########################################
# # SET
#
# #######################################
# print('_______________++++________________')
# s = {1, 1, 2, 3, 2, 4}    # залишаться лише унікальні дані
# print(s)  # {1, 2, 3, 4}
# s.add(5)  # додаємо до Сету елем
# set_1 = {1, 2, 31, 41, 51}
# set_2 = {1, 2, 3, 4, 5}
#
# print(set_1.symmetric_difference(set_2)) # виведуться ті які не повторюються
# # {3, 4, 5, 51, 41, 31}
# set_1.symmetric_difference_update(set_2)
# print('symmetric_difference_update, set_1 -   ',set_1)  # {3, 4, 5, 41, 51, 31}
# # Апдейтимо периший Сет значеннями які не повторюються в обох Сетах
#
#
# print(set_1.issuperset(set_2))  #  перевіряємо чи входить один Сет в інший
# print(set_2.issubset(set_1))    # False
# print(set_1.isdisjoint(set_2))  # повертає True якщо Сети не мають спільних елем
# print(set_1.intersection(set_2))  # повертає переріз спільних елем
#
# print(set_1.difference(set_2))    # повертає новий Сет елементи якого не присутні в другому Сеті
# set_1.difference_update(set_2)    # змінюємо перший Сет , якщо елем повторюються , то їх не записуємо
# print('set_1 after difference_update -',set_1)  # {41, 51, 31}
# set_1.update(set_2)  # розширюємо перший Сет обєднавши з другим
# print(set_1)
# print(set_1.pop())   # витягуємо random  елем
# set_1.remove(31)   # видаляємо елем , якщо його не існує то буде помилка
# set_1.discard(3)  # видаляємо елем, якщо його не існує то помилки Не буде
# print('set_1 -',set_1)  # {2, 1, 4, 5, 41, 51}
# print('set_2 -',set_2)  # {1, 2, 3, 4, 5}
# set_1.intersection_update(set_2)  # апдейтимо перший Сет та записуємо переріз Обох Сетів
# print('set_1 after intersection_update -', set_1)  # {1, 2, 4, 5}
# print(set_1.union(set_2)) # повертає новий обєднаний Сет

# ##########################################
# # FUNCTION
#
# #######################################
#
# def func(name, age = 12, *args, **kwargs):
#     print('hello', name, age, sep='_+_', end='\n')
#     print(args)
#     print(kwargs)
#     return 4
# func('Boby', 18, 'sdf', 21, 12, house = 12, status = False)
# # hello_+_Boby_+_18
# # ('sdf', 21, 12)
# # {'house': 12, 'status': False}
#
# def func_2(*args):
#     print(args)
# list_01 = [1, 2, 3]
# func_2(list_01)      # ([1, 2, 3],)
# func_2(*list_01)     # (1, 2, 3)
# tuple_01 = (1, 2, 3)
# func_2(*tuple_01)    # (1, 2, 3)
# dict_01 = {'pet_name': 'Lona', 'age': 12}
# func_2(dict_01)   # ({'pet_name': 'Lona', 'age': 12},)
# func_2(*dict_01)  # ('pet_name', 'age')
#
#
# def connect(**kwargs):
#     print(kwargs)
# config = {'server': 'localhost',
#         'port': 3306,
#         'user': 'root',
#         'password': 'Py1thon!Xt12'}
# connect(**config)

# ##########################################
# # LOOPS
#
# #######################################
# print('---------->-LOOPS-<------------')
# config = {'server': 'localhost',
#         'port': 3306,
#         'user': 'root',
#         'password': 'Py1thon!Xt12'}
# i = 4
# while i > 0:
#     i -=1
#     print(i)
# else:
#     print('finish')
#
# for i in range(1, 23, 3):
#     print(i)
# list_5 = [2, 1, 3, 4, 5, 6]
# for i, v in enumerate(list_5):
#     print('list_5', list_5)
#     print(i, v)
#
# for k, v in config.items():
#     print(k, v)
#
# for key, value in config.items():
#     print(f'{key=}')
#     print(f'{value=}')
#
# compreh = [i for i in range(21)]
# print(compreh)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# compreh_2 = [i**2 for i in compreh if i%2 == 0]
# print('compreh_2', compreh_2)
# compreh_3 = [i**2 if i==4 else i for i in compreh if i%2 == 0]
# print('compreh_3', compreh_3)
#
# print(['even' if i%2==0 else 'odd' for i in range(10)])
#
# dict_02 = {k.upper():v for k,v in config.items()}
# print('dict_02', dict_02)
#
# l = [
#     [1, 2, 3],
#     [4, 5]
# ]
# res = [i for j in l for i in j]
# print(res)
#
# res2 = []
# for j in l:
#     for i in j:
#         res2.append(i)
# print(res2)

# ##########################################
# # HOME WORK
#
# #######################################
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'sdfa2434k4lk 43l 43 lews'
print(st)
print([i for i in st if i.isdigit()]) # ['2', '4', '3', '4', '4', '4', '3', '4', '3']

print('*'.join(i for i in st if i.isdigit()))  # '2*4*3*4*4*4*3*4*3'
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
print([i if i.isdigit() else ' ' for i in st])  # [' ', ' ', ' ', ' ', '2', '4', '3', '4', ' ', '4', ' ', ' ', ' ', '4', '3', ' ', ' ', '4', '3', ' ', ' ', ' ', ' ', ' ']

print(''.join(i if i.isdigit() else ' ' for i in st))  # '    2434 4   43  43     '

print(''.join(i if i.isdigit() else ' ' for i in st).split())  # ['2434', '4', '43', '43']

print(','.join(''.join(i if i.isdigit() else ' ' for i in st).split()))  # '2434,4,43,43'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello , world'
print([i.upper() for i in greeting])  # ['H', 'E', 'L', 'L', 'O', ' ', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
print([i**2 for i in range(30) if i%2])  # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]

def swap_to_x():
    l = [1, 2, 43, 54, 65, 4]
    print(['xx' if not (i+1)%3 else v for i,v in enumerate(l)])
swap_to_x()   # [1, 2, 'xx', 54, 65, 'xx']

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1 :
            print('* '*n)
        else:
            print('*'+' '*2*(n-2)+' *')
square(5)

def multi_table(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            res = j*i
            print(f'{res:6}', end='')
            j+=1
        i+=1
        print()
multi_table(4)