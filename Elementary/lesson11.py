# n = 6
# a = 0
# while n > a :
#     print( ' Nazik' )
#     a += 1
from curses.ascii import isalpha

# while True:
#     num = int(input( 'Введите цифру :  '))
#     if num == 6:
#         print ( ' ok ')
#         continue
#     if num == 7:
#         print ( ' break ')
#         break

# while True :
#     n = 'nazik'
#     print(n)
#
#     break






passwords = []
while True:
    n = input( ' Введите пароль : ')
    if len(n)  < 8 :
        print( ' Короткий ! ' )
        continue
    if 'abs'  in n or '123' in n :
        print( ' Нельзя повторять ')
        continue
    if n.isdigit() :
        print( ' Ошибка нет букв и символов')
        continue
    if n.isalpha() :
        print(  ' Ошибка нет цифр  и символов ' )
        continue
    if  n.isalnum():
        print( ' нет символов')
        continue
    if n.upper() == n.lower():
        print( ' Нет букв ')
        continue
    if '0' not in n and '1' not in n and '2' not in n and '3' not in n and '4' not in n and '5' not in n and '6' not in n and '7' not in n and '8' not in n and '9' not in n :
        print( ' Нет цифр  ')
        continue
    print( '  Надежный пароль ')
    passwords.append(n)
    print( '  Ваш пароль сохранен в списке Passwords list . '  )
    print ( )
    print( f'  Passwords list : {passwords} ')
    break













    # v = 0
    # s = 1
    # g = 2

    # for d in n:
    #     if d.isdigit():
    #         v = 4
    #     elif d.isalpha():
    #         s = 5
    #     else:
    #         g = 6
    #
    #
    # if  v == 0:
    #     print( ' error ')
    #     continue
    # if  s == 1:
    #     print( ' error  ')
    #     continue
    # if  g == 2:
    #     print( ' error ')
    #     continue
    #
    # print( 'ok ' )
    # break


















