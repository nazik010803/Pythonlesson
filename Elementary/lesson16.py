# student = {
#     'last_name': ' Bakytbek kyzy ',
#     'first_name': 'Nazik'
# }






#        Задача 1
#
# teachers = {
#     "Преподаватель 1": 20,
#     "Преподаватель 2": 15,
#     "Преподаватель 3": 25,
#     "Преподаватель 4": 10,
#     "Преподаватель 5": 18
# }
#
# for teacher, students in teachers.items():
#     if students > 18:
#         n = students - 18
#         print(teacher, f' исключили : {n}')
#     elif students < 18:
#         print(teacher, f'набор : { 18 - students}')
#     else:
#         print(teacher, "класс полный")






#           Задача 2

# for bull in range(10):
#     for cow in range(20):
#         n = 100 - bull - cow
#         money = cow * 5000 + bull * 10000 + n * 1000
#         if money == 100000 and  n >= 0:
#             print(f'bull : {bull}, cow : {cow}, calv : {n}' )






#       Задача 3

# x = float(input(" X :  "))
# y = float(input(" Y :  "))
# day = 1
# while x < y :
#     x = x * 1.1
#     day += 1
#
# print(day)




#        Задача 4
#
# passwords = []
# while True:
#     n = input( ' Введите пароль : ')
#     if len(n)  < 8 :
#         print( ' Короткий ! ' )
#         continue
#     if 'abs'  in n or '123' in n :
#         print( ' Нельзя повторять ')
#         continue
#     if n.isdigit() :
#         print( ' Ошибка нет букв и символов')
#         continue
#     if n.isalpha() :
#         print(  ' Ошибка нет цифр  и символов ' )
#         continue
#     if  n.isalnum():
#         print( ' нет символов')
#         continue
#     if n.upper() == n.lower():
#         print( ' Нет букв ')
#         continue
#     if '0' not in n and '1' not in n and '2' not in n and '3' not in n and '4' not in n and '5' not in n and '6' not in n and '7' not in n and '8' not in n and '9' not in n :
#         print( ' Нет цифр  ')
#         continue
#     print( '  Надежный пароль ')
#     passwords.append(n)
#     print( '  Ваш пароль сохранен в списке Passwords list . '  )
#     print ( )
#     print( f'  Passwords list : {passwords} ')
#     break



#      Задача 5

# a = int(input( 'Введите цифру : '))
# b = int(input( 'Введите цифру : '))
# c = input ( 'Выберите  символ * , + , - , // : ')
#
# if c == '*':
#     print (f'{a} * {b} = { a * b} ')
# if c == '+':
#     print (f'{a} + {b} = { a + b} ')
# if c == '-':
#     print (f'{a} - {b} = { a - b} ')
# if c == '//':
#     print (f'{a} // {b} = { a // b} ')
# elif c != '*' and c != '+' and c != '-' and c != '//':
#     print ( 'Error ')




#       Задача 6

# 1 . Integer - int
# 2 . Floating point number - float
# 3 . String - str
# 4 . Boolean - bool
# 5 . List - list
# 6 . Tuple - tuple
# 7 . Dictionary - dict
# 8 . Set - set





#          Задача 7
#
# list = []
# while True :
#     n = int(input(" number: "))
#     list.append(n)
#     if n == 8 :
#         break
#
# print(f' Попытки : {list}')
# print(f' Количество : { len(list)}')
#




#         Задача 8

# set = { 1 , 2 , 3 , 'Nazik '}
# dict = {
#     'Name' : 'Nazik' ,
#     'Age' : 23
# }
# tuple = ( 1,2,3 )
# list = [ 1 , 2 , 3 ]
# int = 1
# float = 1.2
# str = 'Nazik'
# bool = True or False



#          Задача 9

# cd - открывает рабочий стол
# ls - показывает  что на рабочем столе
# mkdir - создает  папку
# touch - создает файл
# rm - удаляет без возврата
# clear - очищает терминал
# cd_ - выход
# ls_a - показывает скрытые файлы




#          Задача 10

# while True :
#     print("Hello World")

# for i in range(5):
#     print(i)




#           Задача 11

# def start ( ):
#     a = input( 'Введите команду : ')
#     if a == 'start':
#         b = input ( 'Ваше имя : ')
#         print( f' Привет { b } !' )
# start()




#           Задача 12
# def m():
#     a = input( ' Name : ')
#     def n():
#         for i in range(5):
#             print( f' Hello {a} !' )
#     n()
# m()