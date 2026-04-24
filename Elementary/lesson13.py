# n = {
#     'Zarina' : 100 ,
#     'Muslim' : 60 ,
#     'Bayaman' : 50 ,
#     'Nuriza' : 105 ,
#     'Umar' : 110 ,
#     'Chyngyz' : 70 ,
#     'Askat' : 40
#
# }
#
# b = [ ]
# a = [ ]
# for k , v  in n.items():
#     if v < 90:
#         b.append(v)
#     if v > 90 :
#         a.append(v)
# print(a)
# print(b)












# a = {
#     'apple' : 3 ,
#     'banana' : 4 ,
#     'bread' : 5 ,
#     'egg' : 6 ,
#     'grape' : 7 ,
#     'water' : 8
# }
# k = {}
# b = input(' Введите товар :')
# n = int(input( 'Количество : '))
# while True :
#     if b in k :










# s = input( 'Введите слово : ' )
# v = {
#     'monday':'понедельник ',
#     'tuesday':'вторник',
#     'wednesday':'среда ',
#     'thursday':'четверг ',
#     'friday':'пятница ',
#     'saturday':'суббота ',
#     'sunday':'воскресенье',}
#
# if s in v :
#     print ( 'Перевод : ' , v[s])
# else:
#     print( 'Слова нет в словаре ')





# film = {
#     'name ': 'Boyforrent',
#     'year' : 2026 ,
#     'actress':'kim jisu' }
# print(film)




# n = {
#     'название':'Сеул',
#     'страна':'Корея',
#     'население':100000000,
#     'достопримечательность ' : 'Башня Намсан'
# }
# print( n )



# m = {
#     'France' : 'Paris',
#     'Germany' : 'Berlin',
#     'Kazakstan': 'AStana',
#     'Italy' : 'Rome',
# }
#
# country = input( 'Введите страну : ')
# print( m [ country ] )



#
# weather = {
#     "понедельник": 20,
#     "вторник": 22,
#     "среда": 18,
#     "четверг": 19,
#     "пятница": 23,
#     "суббота": 25,
#     "воскресенье": 21
# }
#
# print(weather)
#
#


#
#
#
# weather = {
#     "понедельник": 20,
#     "вторник": 22,
#     "среда": 18,
#     "четверг": 19,
#     "пятница": 23,
#     "суббота": 25,
#     "воскресенье": 21
# }
#
# day = input("Введите день недели: ")
#
# print(weather[day])


#
#
#
#
#
#
# words = {
#     "кот": 3,
#     "собака": 6,
#     "дом": 3,
#     "машина": 6
# }
#
# print(words)
#
#
#
#
#
#
#
# words = {
#     "кот": 3,
#     "собака": 6,
#     "дом": 3,
#     "машина": 6
# }
#
# word = input("Введите слово: ")
#
# print(words[word])


#
#
# letters = {
#     "кот": {"гласные": 1, "согласные": 2},
#     "дом": {"гласные": 1, "согласные": 2}
# }
#
# print(letters)
#
#
#
#
# #
#
# l = {
#     "кот": {"гласные": 1, "согласные": 2},
#     "дом": {"гласные": 1, "согласные": 2}
# }
#
# word = input("Введите слово: ")
#
# print("Гласные:", l[word]["гласные"])
# print("Согласные:", l[word]["согласные"])








# g = {
#     "математика": 5,
#     "русский": 4,
#     "английский": 5,
#     "история": 3
# }
#
# for s , k in g.items():
#     if k > 4:
#         print(s)





# prices = {
#     "a": 50,
#     "b": 30,
#     "s": 40
# }
# while True:
#     p = input("Введите товар: ")
#     c = int(input("Введите количество: "))
#     n = int(input( 'Хотите завершить покупку ? '))
#     for k , v in prices.items():
#         if k == p :
#             t = v * c
#             continue
#     print("Сумма:", t )
#     if n == 1:
#         break

