''' Task: given an integer n
if n is odd print Weird,
if n is even and in the range of 2-5 print not Weird,
if n is even and in the range of 6-20 print Weird,
if n is even and > 20 print not Weird
make sure that n in range 1-100
'''
''' 
# 1st solution
print('If you want to exit type "exit"')
while True:
    n = input('Please enter a number between 1 and 100 : ')
    if n == 'exit' or n == 'Exit':
        break
    if n.isdigit():
        n = eval(n)
        if 100 > n > 1:
            if n % 2 != 0:
                print('Weird')
            else:
                if 5 >= n >= 2:
                    print('Not Weird')
                elif 20 >= n >= 6:
                    print('Weird')
                elif n > 20:
                    print('Not Weird')
        else:
            print('You did not input a valid number, Please try again.')
    else:
        print('You did not type a number, string is not allowed.')
'''
'''
# 2nd solution
print('If you want to exit type "exit"')
while True:
    n = input('Please enter a number between 1 and 100 : ')
    if n == 'exit' or n == 'Exit':
        break
    if n.isdigit():
        n = eval(n)
        if 100 > n > 1:
            if n % 2 == 0 and 20 >= n >= 6 or n % 2 != 0:
                print('Weird')
            else:
                print('Not Weird')
        else:
            print('You did not input a valid number, Please try again.')
    else:
        print('You did not type a number, string is not allowed.')
'''
'''
# 3rd solution
print('If you want to exit type "exit"')
while True:
    n = input('Please enter a number between 1 and 100 : ')
    if n == 'exit' or n == 'Exit':
        break
    if n.isdigit():
        n = eval(n)
        if n > 100 or n < 1:
            print('You did not input a valid number, Please try again.')
        elif n % 2 == 0 and 20 >= n >= 6 or n % 2 != 0:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('You did not type a number, string is not allowed.')
'''