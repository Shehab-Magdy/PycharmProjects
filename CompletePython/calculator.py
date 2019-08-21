import re


def perform_math():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input('Enter Equation : ')
    else:
        equation = input(str(previous))
    if equation.lower() == 'exit':
        print('Good Bye...')
        run = False
    else:
        equation = re.sub('[a-zA-Z,:;\'" "()]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


print('Our Calculator \nType "Exit" to quiet\n')
previous = 0
run = True

while run:
    perform_math()
