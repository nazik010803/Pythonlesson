# n = [ 1 , 2 , 3 , 4 , 5 ]
# if 1 in n :
#     print(' 1 ')
#     if 2 in n :
#         print(' 2 ')
#         if 3 in n :
#             print(' 3 ')
#             if 4 in n :
#                 print(' 4 ')
#                 if 5 in n :
#                     print(' 5 ')
#

# names = [ 'Akulya' , 'Aigerim' , 'Erbol' , 'Aliya' ]
# if len(names [0])>5:
#     print(names [0])
# if len(names [1])>5:
#     print(names [1])
# if len(names [2])>5:
#     print(names [2])
# if len(names [3])>5:
#     print(names [3])
#
#
# numbers = [1, -3, 5, -7, 9, -2]
#
# print("Положительные:")
# if numbers[0] > 0:
#     print(numbers[0])
# if numbers[1] > 0:
#     print(numbers[1])
# if numbers[2] > 0:
#     print(numbers[2])
# if numbers[3] > 0:
#     print(numbers[3])
# if numbers[4] > 0:
#     print(numbers[4])
# if numbers[5] > 0:
#     print(numbers[5])
#
# print("Отрицательные:")
# if numbers[0] < 0:
#     print(numbers[0])
# if numbers[1] < 0:
#     print(numbers[1])
# if numbers[2] < 0:
#     print(numbers[2])
# if numbers[3] < 0:
#     print(numbers[3])
# if numbers[4] < 0:
#     print(numbers[4])
# if numbers[5] < 0:
#     print(numbers[5])



#
# numbers = [1, -3, 5, -7, 9, -2]
#
# positive = []
# negative = []
#
# if numbers[0] > 0:
#     positive.append(numbers[0])
# else:
#     negative.append(numbers[0])
#
# if numbers[1] > 0:
#     positive.append(numbers[1])
# else:
#     negative.append(numbers[1])
#
# if numbers[2] > 0:
#     positive.append(numbers[2])
# else:
#     negative.append(numbers[2])
#
# if numbers[3] > 0:
#     positive.append(numbers[3])
# else:
#     negative.append(numbers[3])
#
# if numbers[4] > 0:
#     positive.append(numbers[4])
# else:
#     negative.append(numbers[4])
#
# if numbers[5] > 0:
#     positive.append(numbers[5])
# else:
#     negative.append(numbers[5])
#
# print("Положительные:", positive)
# print("Отрицательные:", negative)



numbers = [1, -3, 5, -7, 9, -2]

positive = []
negative = []

for n in numbers:
    if n > 0:
        positive.append(n)
    if n < 0:
        negative.append(n)
print(positive)
print(negative)


# w = [ 100 , 200 , 300 , 400 , 500 , 600 ]
# w.reverse()
# print(w)

# q = [ 1 , 2 , 3 , 4 , 5  ]
# z = [ 6 , 7 , 8 , 9 , 10 , 11 ]
# q.extend(z)
# print(q)

# menu = [ ' lagman - 150som ',' plov - 300som ',' borsh - 105som ',' manty - 400som']
# menu.append( 'besh - 280som')
# menu[3] = ' manty - 410som'
# menu.pop(2)
# print(menu)


