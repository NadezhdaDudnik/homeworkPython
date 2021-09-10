import random

#1
str1 = 'nadin'
str2 = 'student'

#2
a = 4
b = 6
c = 2
d = 4
e = 3

#3
k = 5.5
l = 3.8
m = 8.34

#4
'''Реализовать 15 варианта сравнения int
переменных с операторами >, <, >=, <=, !=. Pезультаты выввести в консоль.'''
if b == c:
    print('b =', b)
elif b >= d:
    print('b =', b)
elif b != a:
    print('b =', b)
elif d == e:
    print('d =', d)
elif d != a:
    print('d =', d)
elif d < b:
    print('d =', d)
elif e < c:
    print('e =', e)
elif b == e:
    print('e =', e)
elif e <= a:
    print('e =', e)
elif a <= c:
    print('a =', a)
elif a != d:
    print('a =', a)
elif a == e:
    print('a =', a)
elif c != d:
    print('c =', c)
elif c < b:
    print('c =', c)
elif c < e:
    print('c =', c)
else:
    print('no matches')

#5
'''Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. 
Pезультаты вывести в консоль.'''
if k == l or k <= m:
    print(k)
elif l < k and l <= m:
    print(m)
elif k == m and m < l:
    print(m)
else:
    print('no matches')

#6
''' Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и
 условными выражениями (end, or, not). Pезультаты весвести в консоль.'''
if b == c and b >= d:
    print('b =', b)
elif d == e and d != a:
    print('d =', d)
elif e < c or b == e:
    print('e =', e)
elif a <= c and a != d:
    print('a =', a)
elif c != d and c < b:
    print('c =', c)
else:
    print('no matches')

print("-------------------")
#7
'''Сделать скрипт используя функцию input().
Функция должна на вход принимать целое число.
2. Выводить должна "Вы вели число = (введённое число),
которое (меньше/больше/равно) 30" '''

print("Введите число")
num = int(input())
if num <= 30:
    print("Вы  ввели число =", num, ", которое меньше/равно) 30")
else:
    print("Число больше 30")

#8
'''делать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться
    рандомное целое число (import random)...(random.randint(1, 100))
    3. Выводить должна "Вы вели число = (введённое число)
    которое (меньше/больше/равно) сгенерированному числу" '''
print("-----------------------")
print("Введите число")
num1 = int(input())
num2 = random.randint(1, 100)
print(num2)
if num1 <= num2:
    print("Вы  ввели число =", num1, ", которое меньше/равно", num2)
else:
    print(num1, " больше, чем ", num2)

#9
''' Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться рандомных 2 целых числа
     (import random)...(random.randint(1, 100))
    3. Выводить должна "Вы вели число = (введённое число)
     которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"'''
print("-----------------------")
print("Введите число")
number1 = int(input())
number2 = random.randint(1, 100)
number3 = random.randint(1, 100)
if (number1 <= number2) and (number1 >= number3):
    print("Вы  ввели число =", number1, ", которое меньше/равно", number2, " и которое больше/равно ", number3)
else:
    print("нет совпадений")