# n = ( 1 , 2 , 3)
# print ( n[0:4:2] )
#


# v = ( 1 , 3 , 4 )
# b = ( 'abs ', 'sdfdg' , 'nbv')
# c = list (v + b )
# print ( c )


# a = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 )
# print( a[1:11:2])
#
# nums = ( 1 , 2 , 3 , 4 , 5 )
# x = list( nums )
# x.insert(2 , 99 )
# print(x)












# words = ["apple", "banana", "cat"]
# for i in words:
#     print( len(i) , end =' ' )






# nums = [ 2 , 3 , 6, 8, 9 , 12]
# for s in nums:
#     if s % 2 == 0 and s % 3 == 0:
#         print( s )
#
#
#
#
# words = ["apple", "banana", "cat"]
# a = [len (n) for n in words ]
# print (a)
#
#
#
#
# numbers = [ 2 ,3 ,5 ,7 ,9,10,12 ]
# s = []
# for m in numbers:
#     if m % 3 == 0 or m % 5 == 0:
#         s.append(m)
# print( s )


# slova = ["apple", "banana", "bat", "cat", "ball"]
# new = []
# for i in slova:
#     if 'b' in i:
#         new.append(i)
# print( new )


# words = ["apple", "banana", "cat"]
# a = []
# for i in words:
#     a.append(len(i))
# print(a)

a = [12, 2, 3, 4, 5, ['frog', 2, 56, 565, [], 43, ['hice', 2, 4, 6, [[[['leto', 'home']], 2, 3, 4, 5, [], ['Asan', [2 ,3, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']]]]]]]
s = str ( a [5][6][4][0][6][1][2])
a = s.count('b')
print(  f' "b" in a : {a}' )