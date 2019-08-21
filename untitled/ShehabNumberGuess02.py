'''
Your game generates a random number
and give only 10 tries for the user to guess that number.
Get the user input and compare it with the random number.
Display a hint message to the user in case the user number is smaller or bigger than the random number.
If the user typed a number out of range(100), display a message that is not allowed and don’t count this as a try.
if the user typed a number that has been entered before, display a hint message and don’t count this as a try also.
In case the user entered a correct number within the 10 tries, display a congratulations message
and let your application guess another random number with the remain number of tries.
If the user finished his all tries, display a message to ask him if he want to play a gain or not.
'''
from random import randint


def testNoinRange(a):
    # Function accepts the max number of range.
    userInput = a + 1
    while userInput not in range(a):
        userInput = int(input('Please guess a number : '))
        if userInput in range(a):
            return userInput
        else:
            print('The number is not allowed, Please try again')


def Nonot_Equals(a, b, c):
    # Accepts a: user input, b: list of prev inputs, c: No of tries.
    if a not in b:
        c += 1
        b.append(a)
        print('Try again')
    else:
        print('You have entered this number before')
    return b, c


def lets_play_with_number_guessing(a, b, c):
    # Accepts a: the max range for random to guess, b: max number of tries, c: the max number of user to enter
    tries = 1
    numbers = []
    x = randint(1, a)
    print(x)
    while tries <= b:
        user_input = testNoinRange(c)
        if user_input == x:
            YN = input('Congratulations! \nYou made it. \nDo you want to continue paling? yes / no : ')
            tries += 1
            numbers.append(user_input)
            if YN == 'yes':
                x = randint(1, a)
                print(x)
            elif YN == 'no':
                break
        else:
            numbers, tries = Nonot_Equals(user_input, numbers, tries)
    print('______________', '\nThe guessed number is :', x, '\nYour entered numbers are :', numbers,
          '\nYour number of tries is :',
          tries - 1, '\n--------------')


lets_play_with_number_guessing(99, 10, 100)
