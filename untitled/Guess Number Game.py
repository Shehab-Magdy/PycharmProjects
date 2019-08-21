'''Your game generates a random number and give only 10 tries for the user to guess that number.
Get the user input and compare it with the random number.
Display a hint message to the user in case the user number is smaller or bigger than the random number.
If the user typed a number out of range(100), display a message that is not allowed and don’t count this as a try.
if the user typed a number that has been entered before, display a hint message and don’t count this as a try also. In case the user entered a correct number within the 10 tries, display a congratulations message and let your application guess another random number with the remain number of tries.
If the user finished his all tries, display a message to ask him if he want to play a gain or not.
'''
from random import randint
num =randint(0,99)
print(num)
tries = 1
listOfTries=[]
#while True:
while True:
    userInput = int(input('Enter the number : '))
    if 0 < userInput < 100:
        if userInput in listOfTries:
            print('Number has been enterd before')
        else:
            if userInput < num:
                print('The number is smaller than the random number')
                listOfTries.append(userInput)
                tries = tries + 1
            elif userInput > num:
                print('The number is bigger than the random number')
                listOfTries.append(userInput)
                tries = tries + 1
            else: # userinput == num
                print('congratulations.., the number is correct and the number is :', num, '\nnumber of tries is :', tries, '\nYour tries are :', listOfTries,'\nPlay again... guess a number.')
                num = randint(0, 99)
                listOfTries.clear()
                print(num)
    else:
        print('The number is out of range 100')
    if tries > 10:
        ask = input('your tries is over, Do you want to play again? yes/no')
        if ask == 'yes':
            tries = 1
            listOfTries.clear()
            num = randint(0, 99)
            print(num)
        elif ask == 'no':
            break
        else:
            print('invalid input')
# else:
#     print('number of tries is over')
#     ask = input('do you want play again? yes/no')
#     if ask == 'yes':
#         tries =1
#         listOfTries.clear()
#         num = randint(0, 99)
#     elif ask == 'no':
#         break
#     else:
#         print('invalid input')

