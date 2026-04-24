     #  Вложенный цикл

# for i in range( 2 , 11  ) :
#     for j in range( 2, 6) :
#         print( f"{j} x {i} = {i*j}" , end= "\t\t")
#     print()
# print()
# for i in range( 2 , 11  ) :
#     for j in range( 6 , 10) :
#         print( f"{j} x {i} = {i*j}" , end= "\t\t")
#     print()









n = int(input( ' Введите число : '))

if 0 < n < 16 :
    for i in range(1):
        for j in range(1, 11):
            print( f"{n}  *  {j} = { n * j }" )
else:
   print ( ' Введите число от 1 до 15 ' )






# n = int(input( ' Введите число : ' ))
# if n%2 == 0:
#     print('Четное число : ' , f'{n} / 2 = {n//2}')
#
# else:
#     print( ' Нечетное число ')


# n = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
# for i in range (0, 5):
#     if i <=3:
#         print( i , end = "\t" )









