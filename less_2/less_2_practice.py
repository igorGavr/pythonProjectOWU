# числа Фібоначі
def func_fib(n):
    f1 = f2 = 1
    print(f1, f2, end=' ')
    while n>2:
        f1, f2 = f2, f1+f2
        print(f2, end=' ')
        n -= 1
    print()
func_fib(5)

def func_fib2(n):
    f1 = f2 = 1
    print(f1, f2, end=' ')
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        print(f2, end=' ')
        n -= 1
    print()
func_fib2(5)

# вивести остранній елемент послідовності Фібоначі
def last_el_fib(n):
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    print(f2)
last_el_fib(7)

# вивести елементи послідовності Фібоначі які менші за певне число
def func_fib3(n):
    f1 = f2 = 1
    print(f1, f2, end=' ')
    while f2<n:
        print(f2, end=' ')
        f1, f2 = f2, f1+f2
    print()
func_fib3(23)

# порахувати кількість парних і непарних цифр числа
def even_odd_figures(n):
    even = odd = 0
    while n>0:
        digit = n%10
        if digit%2==0:
            even+=1
        else:
            odd+=1
        n//=10
    print('even - ',even,'odd - ', odd)
even_odd_figures(12312)

def even_odd_figures2(n):
    even = odd = 0
    while n>0:
        n, digit = divmod(n, 10)
        if digit%2==0:
            even+=1
        else:
            odd+=1
    print('even - ',even,'odd - ', odd)
even_odd_figures2(12312)

# перевернути стрічку
def reversed_string(string):
    result_string = ''
    for i in range(len(string)-1, -1, -1):
        result_string += string[i]
    print(result_string)
    return result_string
reversed_string('posddfddd')

def reversed_string2(string):
    new_string = string[::-1]
    return new_string
print(reversed_string2('sdga'))

def reversed_string3(string):
    new_string = list(string)
    new_string.reverse()
    print(new_string)
    return ''.join(new_string)
print(reversed_string3('sdga'))

# функція приймає дві стрічки .
# Якщо це дві букви то повернути 1, якщо букви ,
# але одна велика та маленька то повертається 0
# і якщо хоча б одна стрічка скл не з букв то -1
def same_case(a:str, b:str)->int:
    if not a.isalpha() or not b.isalpha():
        return -1
    if a.isupper() == b.isupper():
        return 1
    else:
        return 0
print(same_case('a', 'h'))

def same_case2(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1
print(same_case2('s', 'a'))


def isPrime(n):
    for i in range(2, n//2+1):
        print('i2- ', i)
        if(not (n%i)):
            print('isPrime- ', 0)
            return 0
    print('isPrime- ', 1)
    return 1
numPrimes = 0
for i in range(2, 5):
    numPrimes+=isPrime(i)
    print('i- ', i)
    print('numPrimes- ', numPrimes)
print(str(numPrimes), 'numPrimes')


