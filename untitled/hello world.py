"""
x = input('Type your name')
y = input('What is you programing languag?')
print('hello ', x, 'welcome in ', y, 'language')
age = input('Enter your age:')


z = input('how are you? (fine - not OK)')
if z== 'fine':
    zx = 'Great'
elif z == 'not OK':
    zx = 'Why'
else:
    input('please type a valid answer (fine - not OK')
print (zx)
print ()
"""
# 60 + 20 = 80 using +

"""
first_number=eval(input('Please enter your first number: '))
secund_number = eval(input('Please enter your first number: '))
print(str(first_number) +' + ' + str(secund_number) + ' = ' + str(first_number+secund_number))
"""

# num1=eval(input('Please enter your first number: '))
# num2 = eval(input('Please enter your first number: '))
# print('Division output = ', num1 / num2, "\nDivision output as integer = ", num1 // num2, "\nReminder output = ", num1 % num2)
#
# import math
# ax = eval(input('Enter x for 1st point : '))
# ay = eval(input('Enter y for 1st point : '))
# bx = eval(input('Enter x for 2nd point : '))
# by = eval(input('Enter y for 2nd point : '))
#
# xx = eval(input('How many numbers you want after decimal point : '))
# res = math.sqrt((int(ax)-int(bx))**2 + (int(ay)-int(by))**2 )
# #res = round(math.sqrt(math.pow(bx-ax,2)+math.pow(by-ay,2)),xx)
#
# print (res)
#
# op = input('Chose a process \n1 for Add \n2 for Sub \n3 for Mul \n4 for Div \nType your choice ')
# if op in ['1','2','3','4']:
#     ax = eval(input('Enter 1st number : '))
#     ay = eval(input('Enter 2nd number : '))
#
#     if (op == '1'):
#         print(ax, '+', ay , '=', ax+ay)
#     elif (op == '2'):
#         print(ax, '-', ay, '=', ax - ay)
#     elif (op == '3'):
#         print(ax, '*', ay, '=', ax * ay)
#     else:
#         if ay != 0:
#             print(ax, '/', ay, '=', ax / ay)
#         else:
#             print('You can not divid by 0')
# else:
#     print( 'You did not pick a right operation')
#
# x= [[1,'Hello',3],'Python',[1,0,'to'],[1,[100,'all']]]
# print (x[0][1],x[1],x[2][2],x[3][1][1])
# print (x[0][1][0],x[0][1][1],x[0][1][2],x[1][0])
# print ('Help')

# x1 = 'Hello All!'; x2 = 'Python'
# if len(x1) % 2 == 0 and len(x2) % 2 == 0:
#     print(x1[:int(len(x1) / 2)] + x2[:int(len(x2) / 2)] + '\n' + x1[int(len(x1) / 2):] + x2[int(len(x2) / 2):])
# else:
#     print('The length of the strings is not even')

# x_str = 'Mari'
# alpha = ['a', 'e', 'i', 'o', 'u']
# if x_str[0] in alpha:
#     print('index ' + '0' + ' is in the list')
# elif x_str[1] in alpha:
#     print('index ' + '1' + ' is in the list')
# elif x_str[2] in alpha:
#     print('index ' + '2' + ' is in the list')
# elif x_str[3] in alpha:
#     print('index ' + '3' + ' is in the list')
# else:
#     print('is not')
#
#
# x_str = 'Mari'
# alpha = ['a', 'e', 'i', 'o', 'u']
# index = 0
# for g in x_str:
#     if g in alpha:
#         print('Index ' + str(index) + ' is ' + g + ' it is a vowel')
#     index +=1

# salaries=[3000,4000,7000,20000,600]
# sum=0
# for i in salaries:
#     sum +=i
# print(sum)

# x=eval(input('Type the number you want to print : '))
# for i in range(1,13):
#     print(x,'x',i,'=',x*i)

# x=[]
# numberOfValues= eval(input('Please enter number of inputs '))
# sum=0
# for i in range(numberOfValues):
#     y=eval(input('Enter your number '))
#     x.append(y)
#     sum += y
# print(sum)

# x = int(input('Enter a number : '))
# for i in range(1, x + 1):
#     print(i, end='')

# x = []
# numberOfValues = eval(input('Please enter number of inputs '))
# sumOfElements = 0
# i = 0
# while i < numberOfValues:
#     y = eval(input('Enter your number '))
#     x.append(y)
#     sumOfElements += y
#     i += 1
# print(sumOfElements)

# input < 50 divided by 3 print the number *10 then take a nother nnumber otherwise break
# while True:
#     a=eval(input('Please input a number : '))
#     if a <50 and a%3 ==0:
#         print(a*10)
#     else:
#         print('Invaled input...')
#
#         break

# x={1:'this is one',2:'this is 2'}
# print(x[1])
# print(x.keys())
# print(x.items())
# print(len(x))
# for i in x:
#     print(x[i])

# d={111:{'name':'Ahmed','age':25},222:{'name':'Hossam','age':30},333:{'name':'Hassan','age':35}}
# for i in list(d.keys()):
#     print('ID of emp is :', i)
#     print('Name of emp is :', d[i]['name'])
#     print('Age of emp is :', d[i]['age'])
#
# for k, v in d.items():
#     print('ID of emp is :', k)
#     print('Name of emp is :', v['name'])
#     print('Age of emp is :', v['age'])

# print = 3
# a= print+2
# print(a)

'''1-Take three numbers, 
2-check if number is even or odd, 
3-if even: 
    a-get the factorial of the number, 
    b-get 70% of the number, 
    c-add step a+ step b; 
4-if odd: 
    a-get the factorial of the number 
    b-get 30% of the number, 
    c-add a+b;
5- add the result of process in a list & print it'''


# import math
#
# a = eval(input('Enter your 1st number : '))
# b = eval(input('Enter your 2nd number : '))
# c = eval(input('Enter your 3rd number : '))
# res = []
# for i in (a, b, c):
#     if i % 2 == 0:
#         perc = i * 0.7
#     else:
#         perc = i * 0.3
#     res.append(math.factorial(i) + perc)
# print(res)

# import Helloworldmethods as hm
#
# opp = input('input your choise : + , - , * , /')
# num1 = eval(input('Enter your 1st number'))
# num2 = eval(input('Enter your 2nd number'))
# if opp == '+':
#     print(hm.addnum(num1, num2))
# elif opp == '-':
#     print(hm.subnum(num1, num2))
# elif opp == '*':
#     hm.subnum(num1, num2)
# elif opp == '/':
#     hm.subnum(num1, num2)

# def func(par=[]):
#     par.append('a')
#     return par
#
#
# print(func()+func()+func())


# def dev_str(str):
#     if len(str) % 2 == 0:
#         re1 = str[:int(len(str) / 2)]
#         rez = str[int(len(str) / 2):]
#     else:
#         re1 = str[:int(len(str) / 2 + 1)]
#         rez = str[int(len(str) / 2 + 1):]
#     return re1, rez
#
#
# def cut_to_2(st1, st2):
#     re1, rez = dev_str(st1)
#     re2, rey = dev_str(st2)
#     # if len(st1) % 2 == 0:
#     #     re1 = st1[:int(len(st1) / 2 )]
#     #     rez = st1[int(len(st1) / 2 ):]
#     # else:
#     #     re1 = st1[:int(len(st1) / 2 + 1)]
#     #     rez = st1[int(len(st1) / 2 + 1):]
#     # if len(st2) % 2 == 0:
#     #     re2 = st2[:int(len(st2) / 2)]
#     #     rey = st2[int(len(st2) / 2):]
#     # else:
#     #     re2 = st2[:int(len(st2) / 2 + 1)]
#     #     rey = st2[int(len(st2) / 2 + 1):]
#
#     return str(re1 + rey), str(rez + re2)
#
#
# str1 = 'abcd'
# str2 = 'wxyz'
# # res1, res2 = cut_to_2(str1, str2)
# print(cut_to_2(str1, str2))


# def x(x1):
#     x2 = x1 * 3
#     print(x2)
#     return x2
#
#
# # print(x2)
# x2 = x(5)
# print(x2)


# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(120))

# def sum_list(L):
#     if len(L) == 0:
#         return 0
#     return L.pop() + sum_list(L)
#
# n_list = [5, 6, 9]
# print(sum_list(n_list))


# algorithms , data structures, soled patterns, design patterns
