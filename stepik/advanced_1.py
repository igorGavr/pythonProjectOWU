import re
from math import *
# Задача Иосифа Флавия 🌶️🌶️
# n человек, пронумерованных числами от 11 до nn,
# стоят в кругу. Они начинают считаться, каждый kk-й
# по счету человек выбывает из круга, после чего счет
# продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека,
# который останется в кругу последним.
n = 5
k = 2
# res = 0
# for i in range(1, n+1):
#     res = (res+k)%i
#     print(res)
# print(res+1)
# print(2%3)


# list = [i for i in range(1, n + 1)]
# print(list)
#
# while len(list) != 1:
#     for i in range(0, k-1):
#         list.append(list[i])
#         print(list, '-->')
#     del list[0:k]
#
# print(list)

# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек,
# лежащих в каждой координатной четверти.
# n = int(input())
# ch1 = 0
# ch2 = 0
# ch3 = 0
# ch4 = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x>0 and y>0:
#         ch1+=1
#     if x<0 and y>0:
#         ch2+=1
#     if x<0 and y<0:
#         ch3+=1
#     if x>0 and y<0:
#         ch4+=1
# print(f'Первая четверть: {ch1}')
# print(f'Вторая четверть: {ch2}')
# print(f'Третья четверть: {ch3}')
# print(f'Четвертая четверть: {ch4}')


# st = list(map(int, input().split()))
#
# count = 0
# for i in range(1, len(st)):
#     if st[i]>st[i-1]:
#         count+=1
# print(count)

# st = list(map(int, input().split()))
# for i in range(0, len(st)-1, 2):
#     st[i],st[i+1]=st[i+1],st[i]
# print(*st)

# st = list(map(int, input().split()))
# t = []
# count = 1
# for i in st:
#     if i not in t:
#         t.append(i)
# print(len(t))

# n = int(input())
# nums = [int(input()) for i in range(n)]
# print(nums)
# big = int(input())
# flag = 'НЕТ'
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)):
#         if len(nums)>1 and nums[i]*nums[j]==big and i!=j:
#             flag = 'ДА'
#             break
# print(flag)

# x, y = input(), input()
# var = ['r', 'p', 's']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(var.index(x))
# print(var.index(y))
# print(ans[var.index(x) - var.index(y)])

# list = ["ножницы", "ящерица", "Спок",  "камень", "ножницы", "бумага", "камень", "ящерица", "бумага", "Спок", "ножницы"]
# t , r = input(), input()
# x = 0
# for i in range(len(list)-1):
#     if t == r:
#         break
#     if t == list[i] and r == list[i+1]:
#         x=1
#         break
#     else:
#         x=2
# list_2 = ['ничья', 'Тимур', 'Руслан']
# print(list_2[x])

# res = input()
# tmp = ''
# while tmp in res:
#     tmp += 'p'
#     print(tmp)
# print(len(tmp) - 1)
# print('' in 'opo')
#
# print(max([len(seq) for seq in 'opopopopppo'.split('o')]))
# print([len(seq) for seq in 'opopopopppo'.split('o')])


# n = int(input())

# pattern = r'\w*a\w*n\w*t\w*o\w*n\w*'
# result = [i+1 for i in range(int(input())) if re.search(pattern, input())]
# print(*result)

# for i in range(int(input())):
#     s, virus, x  = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break

# s = ''
# for i in range(int(input())):
#     for j in input():
#         if s + j in ['a','an','ant','anto','anton']:
#             s += j
#     if s == 'anton':
#         print(i + 1, end=' ')
#     s = ''


# print(*[k + 1 for k in range(int(input())) if __import__('re').match(".*a.*n.*t.*o.*n.*", input())])
#
# pattern = ".*a.*n.*t.*o.*n.*"
# num_strings = int(input())
# results = []
# for k in range(num_strings):
#     string = input()
#     if re.match(pattern, string):
#         results.append(k + 1)
# print(*results)


# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# word = input()+' запретил букву'
# for char in alphabet:
#     if char in word:
#         print(word, char)
#         word = word.replace(char, '')
#         word = ' '.join(word.split())
#         if len(word)<1:
#             break


# n = 4                                          # количество строк (элементов)
# my_list = []
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)




# n = int(input())
# print(*[[i for i in range(1, n+1)] for i in range(1, n+1)], sep = "\n")

# list1 = [list(range(1, i+1)) for i in range(1, n+1)]
# for i in list1:
#     print(i)


# n = int(input())
#
# li = [1]
# for i in range(n):
#     print('i ---> ', i)
#     print('li --->', li)
#     for j in range(len(li) - 1):
#         print('j --> ', j)
#         li[j] = li[j] + li[j + 1]
#         print(li)
#     li.insert(0, 1)
#     print(li)
#     print('----------==========----------')
#
# print(li)

# n = int(input())
# li = [1]
# for i in range(n):
#     print(*li)
#     for j in range(len(li) - 1):
#         li[j] = li[j] + li[j + 1]
#     li.insert(0, 1)

n = input().split()
l = []
l.append(n[0])
for i in range(1, len(n)):
    if n[i]