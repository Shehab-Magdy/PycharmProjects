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

tries = 1
numbers = []
x = randint(1, 99)
noOfPlays =1
print(x)
while tries <= 10:
    userInput = int(input('Please guess a number : '))
    if userInput not in range(100):
        print('The number is not allowed, Please try again')
    elif userInput == x:
        b = input('Congratulations! \nYou made it. \nDo you want to continue paling? yes / no : ')
        tries += 1
        numbers.append(userInput)
        if b == 'yes':
            while x in numbers:
                x = randint(1, 99)
            print(x)
            noOfPlays +=1
        elif b == 'no':
            break
    else:
        if userInput not in numbers:
            tries += 1
            numbers.append(userInput)
            print('Try again')
        else:
            print('You have entered this number before')
print('______________', '\nThe last guessed number is :', x, '\n You have played :', noOfPlays,'times','\nYour totsl numbers enterd are :', numbers,
      '\nYour number of tries is :',
      tries - 1, '\n--------------')
