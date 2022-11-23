import math
def cot_braila():
    print('#⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
    print('#       ⢰⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
    print('#     ⣠⣾⣿⣿⣷⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
    print('#    ⣠⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
    print('#    ⠛⠿⣿⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⣴⣿⣿⣆⠄⠄⠄')
    print('#     ⣰⣿⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⣿⣿⠛⠉⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠄⠘⣿⡆⠄⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠸⣿⡀⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⣿⡇⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⠄⢸⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣿⠇⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⢀⣸⡿⢁⣘⣿⣿⣿⣿⣿⣿⣿⣇⣼⠋⠄⠄⠄⠄')
    print('#⠄⠄⠄⠄⠄⠻⠿⠓⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠁⠄⠄⠄⠄⠄')

def cotik():
    print('#　　　　　 ／＞　 フ')
    print('#　　　　　| 　O　 O|')
    print('#　 　　　／`ミ _x 彡')
    print('#　　 　 /　　　 　 |')
    print('#　　　 /　 ヽ　　 ﾉ')
    print('#　／￣|　　 |　|　|')
    print('#　| (￣ヽ＿_ヽ_)_)')
    print('#　＼二つ')


# a=2
# print(28 if a == 2 else 30 if a in (4, 6, 9, 11) else 31)
# print(30 if a in (4, 6, 9, 11) else 28 if a==2 else 31)
# print(31 if a in (1, 3, 5, 7, 10, 12) else 28 if a==2 else 30)


# a, b, op = input(), input(), input()
# if op not in ('+', '-', '*', '/'):
#     print("Неверная операция")
# else:
#     print("На ноль делить нельзя!" if op == '/' and b == '0' else eval(a + op + b))

# x, y, operator = input(), input(), input()
# match operator:
#     case '+' | '-' | '*' | '/':
#         if y == '0' and operator == '/':
#             print('На ноль делить нельзя!')
#         else:
#             print(eval(x + operator + y))
#     case _:
#         print('Неверная операция')
#
# class Calculator:
#     def __init__(self, first_number: int, second_number: int, operator: str) -> None:
#         self.first_number = first_number
#         self.second_number = second_number
#         self.operator = operator
#
#     def calculate(self):
#         actions = {
#             "*": self.multiplication(),
#             "/": self.division(),
#             "+": self.addition(),
#             "-": self.subtraction()
#         }
#         if self.operator not in "+-*/":
#             print("Неверная операция")
#         else:
#             print(actions[self.operator])
#
#     def multiplication(self):
#         return self.first_number * self.second_number
#
#     def division(self):
#         try:
#             return self.first_number / self.second_number
#         except ZeroDivisionError:
#             return "На ноль делить нельзя!"
#
#     def addition(self):
#         return self.first_number + self.second_number
#
#     def subtraction(self):
#         return self.first_number - self.second_number
#
#
# num1 = int(input('Введіть перше число - '))
# num2 = int(input('Введіть друге число - '))
# oper = input('Введіть операцію +, -, * або / ')
# calc = Calculator(num1, num2, oper)
# calc.calculate()


# Вивести крайні за довжиною стрічки
# print(sorted([input() for i in range(3)], key=len)[0::2], sep='\n')
# print(*{'a':1, 'b': 2})

# Чи може це бути арифметичною прогресією
# z, x, c = 'as', 'sdfad', 'sdssdsds'
# lst = sorted([len(input()) for i in range(3)])
# print('YES' if lst[2]==lst[1]-lst[0]+lst[1] else 'NO')


# На вход программе подается натуральное число nn.
# Напишите программу, которая для каждого из чисел от 00 до nn (включительно)
# выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
# [print(f'Квадрат числа {i} равен {i**2}') for i in range(int(input())+1)]
# [[print(f'Квадрат числа {i} равен {i**2}') for i in range(n+1)] for n in [int(input())]]
from math import *

# На вход программе подается натуральное число n ,
# (n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# [[print('*'*(n-i)) for i in range(n)] for n in [int(input())]]
# [print('*' * i) for i in range(int(input()) + 1)[::-1]]

# На вход программе подается три натуральных числа m, \, p, \, nm,p,n:
# m:m: стартовое количество организмов;
# p:p: среднесуточное увеличение в %;
# n:n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день,
# начиная с 11 и заканчивая nn-м днем.
# m, p, n = 1, 2, 23
# for i in range(n):
#     print(i+1, m*(1+p/100)**i)
#
# [print(i + 1, m * (1 + p / 100) ** (i)) for i in range(n)]

# Даны два целых числа mm и nn ( m \le nm≤n).
# Напишите программу, которая выводит все числа от mm до nn включительно.
# print(*range(int(input()), int(input()) + 1), sep='\n')

# Даны два целых числа mm и nn. Напишите программу,
# которая выводит все числа от mm до nn включительно
# в порядке возрастания, если m < nm<n, или в порядке убывания в противном случае.
# m, n = int(input()), int(input())
# print(*[range(m, n - 1, -1), range(m, n + 1)][m < n], sep='\n')

# linearly_pattern = range(m, n + 1)
# reverse_pattern = range(m, n -1, -1)
#
# for i in linearly_pattern if m < n else reverse_pattern:
#     print(i)


# Даны два целых числа mm и nn (m > nm>n).
# Напишите программу, которая выводит все нечетные числа
# от mm до nn включительно в порядке убывания.
# m, n = 77, 62
# [print(i) for i in range(int(input()), int(input()) - 1, -1) if i%2]
# 　　　　　 ／＞　 フ
# 　　　　　| 　_　 _|
# 　 　　　／`ミ _x 彡
# 　　 　 /　　　 　 |
# 　　　 /　 ヽ　　 ﾉ
# 　／￣|　　 |　|　|
# 　| (￣ヽ＿_ヽ_)_)
# 　＼二つ

# Даны два натуральных числа mm и nn ( m \le nm≤n).
# Напишите программу, которая выводит все числа от mm до nn включительно
# удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.
# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
#         print(i)
# [print(_) for _ in range(int(input()), int(input())+1) if not _%17 or _%10==9 or not _%15]


# Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.
# [[print(f'{i} x {j} = {i*j}') for j in range(1,11)] for i in [int(input())]]
# (lambda n: [print(f'{n} x {i} = {n*i}') for i in range(1, 11)])(int(input()))

# На вход программе подаются два целых числа aa и bb (a \le b)(a≤b).
# Напишите программу, которая подсчитывает количество чисел в
# диапазоне от aa до bb включительно, куб которых оканчивается на 44 или 99.
# count = 0
# a, b = int(input()), int(input())
# for i in range(a, b+1):
#     if i**3%10==4 or i**3%10==9:
#         count+=1
# print(count)
# print(len([a for a in range(int(input()), int(input())+1) if str(a**3)[-1] in "49"]))
# print(len([n for n in range(3, 7 + 1) if n**3 % 10 in [4, 9]]))
# print([n for n in range(3, 7 + 1) if n**3 % 10 in [4, 9]])
# print(sum([1 for i in range(1, 12) if i**3%10 in [4,9]]))
# print([1 for i in range(1, 12) if i**3%10 in [4,9]])


# На вход программе подается натуральное число n
# , а затем nn целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
# n = int(input())
# num = 0
# for i in range(n):
#     num+=int(input())
# print(num)
# print(sum(int(input()) for _ in range(int(input()) )))


# На вход программе подается натуральное число n. Напишите программу,
# которая подсчитывает сумму тех чисел от 11 до n (включительно)
# квадрат которых оканчивается на 2, \, 52,5 или 88.
# n = int(input())
# sum = 0
# for i  in range(1, n+1):
#     if i**2%10 in [2, 5, 8]:
#         sum+=i
# print(sum)
# print(sum([i for i in range(1,int(input())+1) if i**2%10 in (2,5,8)]))

# ФАКТОРІАЛ
from math import *
# n = int(input())
# math.factorial(n)
# fact = lambda n: 1 if n == 0 else n * fact(n - 1)

# def fct(i):
#     return i * fct(i - 1) if i else 1
# print(fct(int(input())))

#Напишите программу, которая считывает 10 чисел и
# выводит произведение отличных от нуля чисел.
# total = 1
# for i in range(10):
#     num = int(input())
#     if num!=0:
#         total*=num
# print(total)
# print(eval('*'.join(map(str, filter(bool, (int(input()) for _ in range(10)))))))
# nums = [i for i in [int(input()) for _ in range(10)] if i != 0]
# print(prod(nums))

#На вход программе подается натуральное число nn.
# Напишите программу, которая вычисляет сумму всех его делителей.
# n = int(input())
# count=0
# for i in range(1, n+1):
#     if n%i==0:
#         count+=i
# print(count)

# n = int(input())
# print(sum([i for i in range(1, n + 1) if n % i == 0]))

# print((lambda n: sum([i for i in range(1, n + 1) if n % i == 0]))(int(input())))

# n = int(input())
# print(sum(i * (not n % i) for i in range(1, n + 1)))

#На вход программе подается натуральное число nn.
# Напишите программу вычисления знакочередующей суммы
# 1-2+3-4+5-6 + ... + (-1)^(n+1)*n.
# n = int(input())
# count = 0
# for i in range( 1, n+1):
#     if i%2==0:
#         count+=-i
#     else:
#         count+=i
# print(count)
#
# print(sum([i if i % 2 != 0 else -i for i in range(1, int(input()) + 1)]))


#На вход программе подается натуральное число nn,
# а затем nn различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее
# и второе наибольшее число последовательности.

# n = int(input())
# max_1 = 0
# max_2 = 1
# for i in range(1, n+1):
#     num = int(input())
#     if num>max_1:
#         max_2 = max_1
#         max_1 = num
#     elif num>max_2:
#         max_2 = num
# print(max_1)
# print(max_2)
#
# s = [int(input()) for _ in range(int(input()))]
# print(max(s))
# s.remove(max(s))
# print(max(s))

# numbers = sorted([int(input()) for i in range(int(input()))])
# print(numbers[-1], numbers[-2], sep='\n')

# print(*sorted(int(input()) for i in range(int(input())))[-2:][::-1], sep='\n')
# print(*[1, 2, 3, 4][-2:][::-1], sep='\n')
#print(*sorted([int(input()) for i in range(int(input()))], reverse=True)[:2], sep='\n')

#Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет.
# count = 0
# for i in range(1, 11):
#     n = int(input())
#     if n%2==0:
#         count+=1
# if count==10:
#     print('YES')
# else:
#     print('NO')

# print('NO' if sum(int(input()) % 2 for i in '1234567890') else 'YES')

# print(('YES', 'NO')[any(int(input()) % 2 for _ in range(10))])


# Последовательность Фибоначчи
# n = int(input())
# if n>1:
#     f1 = 1
#     f2 = 1
#     print(f1, f2, end=' ')
#     for i in range(2, n):
#         f1, f2 = f2, f1+f2
#         print(f2, end=' ')
# else:
#     print(1)

# def fib(n):
#     if n<0:
#         print('Incorrect input ')
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(4))


# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# l = []
# [l.append(l[i-1]+l[i-2]) if i>1 else l.append(1) for i in range(int(input()))]
# print(*l)

# n, a, b = int(input()), 1, 0
# for i in range(n):
#     print(a, end=' ')
#     a+=b
#     b=a-b


#На вход программе подается последовательность слов,
# каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# Напишите программу, которая выводит члены данной последовательности.
# s = input()
# count = 0
# while s!='стоп' and s!='хватит' and s!='достаточно':
#     count+=1
#     s = input()
# print(count)
#
# print(*iter(input, 'КОНЕЦ'), sep='\n')



#На вход программе подается последовательность целых чисел от 11 до 55,
# характеризующее оценку ученика, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число,
# либо число большее 55. Напишите программу, которая выводит количество пятерок.
# n = int(input())
# total = 0
# while n>=0 and n<=5:
#     if n==5:
#         total+=1
#     n = int(input())
# print(total)
#
# n, k = int(input()), 0
# while 1 <= n <= 5:
#     k += n == 5
#     n = int(input())
# print(k)

#Дано натуральное число. Напишите программу,
# которая выводит его цифры в столбик в обратном порядке
# num = int(input())
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10
#
# [print(i) for i in input()[::-1]]
#
# print(*reversed(input()), sep='\n')
#
# print(*input()[::-1],sep='\n')

#Дано натуральное число. Напишите программу,
# которая определяет, состоит ли указанное число из одинаковых цифр.
# n = int(input())
# l = n%10
# flag = True
# while n!=0:
#     if l!=n%10:
#         flag = False
#     n//=10
# if flag:
#     print('YES')
# else:
#     print('NO')
#
# x = input()
# print('YES' if max(x) == min(x) else 'NO')
#
# numbers = input()
# print('YES' if numbers.count(numbers[0]) == len(numbers) else 'NO')
#
# print("YES" if len(set(input())) == 1 else "NO")

#Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность
# его цифр при просмотре справа налево упорядоченной по неубыванию.
# n = int(input())
# flag = 'YES'
# l = n%10
# while n!=0:
#     num1 = n%10
#
#     if num1<l:
#         flag = 'NO'
#     else:
#         l=num1
#     n//=10
# print(flag)

# n = '1234'
# print(n)
# print(('NO', 'YES')[n == sorted(n, reverse=True)])

# l = list(input()); print('YES' if l == sorted(l)[::-1] else 'NO')

print('ಠ_ಠ')

# На вход программе подается число n > 1n>1.
# Напишите программу, которая выводит его наименьший отличный от 11 делитель.
# n = int(input())
# for i in range(2, n+1):
#     if n%i==0:
#         print(i)
#         break
#
# print(next((lambda x: (i for i in range(2, x + 1) if not x % i))(int(input()))))

# Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 11 до nn в соответствии с примером
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()
#
# (lambda x: [[print(f'{j} + {i} = {j + i}') for i in range(1, 10)] and print() for j in range(1, x + 1)])(int(input()))
#
# [[print(f'{j} + {i} = {j+i}') for i in range(1,10)]and print() for j in range(1,a+1)]

n = int(input())
for j in range(n-1):
    print('*'*j)
print('--')
for i in range( n-3,0, -1):
    print('*'*i)