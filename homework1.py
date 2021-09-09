#first homework
#1
st = "20 sm"
print('length =', st, type(st))
#2
a = 1
print('a =', a, type(a))
#3
b = 5.6
print('b =', b, type(b))
#4
byte_1 = b'6,67,8'
print('byte_1 =', byte_1, type(byte_1))

bol = True
print('bol =', bol, type(bol))
#5
list_1 = [1, 2]
print('list1 =', list_1, type(list_1))
#6
tuple_1 = (1, 2)
print('tuple =', tuple_1, type(tuple_1))
#7
set_1 = {1, 4, 3, 6, 1}
print('set1 =', set_1, type(set_1))
set_2 = {'a', 'b', 'c', 'd'}
print('set2 =', set_2, type(set_2))
#8
frozenset_1 = frozenset(set_1)
print('frozenset =', frozenset_1, type(frozenset_1))
#9
dict_1 = {1: 'nadin', 2: 'protestinginfo'}
print('dict =', dict_1, type(dict_1))

#10 task is performed

#11
'''Создать 2 переменные String, создать переменную
в которой суммируете эти переменные. Вывести в консоль'''
str1 = 'a'
str2 = 'b'
summa_strok = str1 + str2
print('summa_strok =', summa_strok)

#12
'''Создать 2 переменные Integer, создать переменную
в которой суммируете эти переменные. Вывести в консоль'''
x1 = 7
x2 = 8
result_x = x1 + x2
print('result_x =', result_x, type(result_x))

#13
'''Создать переменную в которой 
Разделите эти переменные Int. Вывести в консоль'''
result_div = x1 / x2
print('div_x =', result_div, type(result_div))

#14
'''Создать переменную в которой
Умножите эти переменные Int. Вывести в консоль.'''
result_multiplication = x1 * x2
print('result_multiplication =', result_multiplication, type(result_multiplication))

#15
'''Создать переменную в которой Разделите 
без остатка эти переменные Int. Вывести в консоль.'''
result_div_ostatok = x1 // x2
print('result_div_ostatok =', result_div_ostatok, type(result_div_ostatok))

#16
'''Создать переменную в которой надо 
присвоить остаток от деления этих переменные Int. Вывести в консоль.'''
result_ostatok_ot_div = x1 % x2
print('result_ostatok_ot_div =', result_ostatok_ot_div, type(result_ostatok_ot_div))

#17
'''(7 + 12)  3 + 7 * 4 - 44 / 2  4 
расставить точки так чтобы получилось 6884.25. Вывести в консоль.'''
equation = (7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4
print('equation', equation, type(equation))