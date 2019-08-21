"""
*.We have an employee small system , we offer for the client that a three options:
    1: see all the employees in his system.
    2: add a new employee.
    3: delete a specific employee.
*.The system welcome message should contain the three options for the user.
*.The employee data that will be listed or created are : id , name , age , salary.
*.Note : the employee id MUST be unique in the system.
*.When the user asks to add a new employee, the system will automatically generate the id,
  so the user will only add name, age and salary.
*.After any operation, the system will ask the user to choose a new operation or exit from the system.
"""


def nnn():
    while True:
        x = input()
        if x.isnumeric():
            return eval(x)
        else:
            print('You did not input a number. Please try again')


def maxid(x):
    if len(x) == 0:
        y = 1
    else:
        y = max(x)+1
    return y


welcomeMessage = 'Welcome to Our system....' \
                 '\nDo you want to see a list of the Employees? Please type "List" ' \
                 '\nDo you want to Add a new employees? Please type "Add" ' \
                 '\nDo you want to Delete current employees? Please type "Del" ' \
                 '\nWhat is your choice? '
repeatedMessage = 'Choose a new operation or Exit the system.... ' \
                  '\nDo you want to see a list of the Employees? Please type "List" ' \
                  '\nDo you want to Add a new employees? Please type "Add" ' \
                  '\nDo you want to Delete current employees? Please type "Del" ' \
                  '\nDo you want to exit? Please type "Exit" ' \
                  '\nWhat is your choice? '
EmpDict = {}
ArchEmpDict = {}
list_of_Keys = []
choice = input(welcomeMessage)
firstTime = True
while True:
    if not firstTime:
        choice = input(repeatedMessage)
    firstTime = False
    if choice.lower() == 'list':
        if len(EmpDict) == 0:
            print('** There are no items to show.')
        else:
            for Keys in list(EmpDict.keys()):
                print('Id :', Keys)
                for key, value in EmpDict[Keys].items():
                    print(key, ':', value)
                print('---------------------')
    elif choice.lower() == 'add':
        name = input('Please enter the name : ')
        print('Please enter the age : ')
        Age = nnn()
        print('Please enter the salary : ')
        Salary = nnn()
        ID = maxid(list_of_Keys)
        EmpDict[ID] = {'Name': name, 'Age': Age, 'Salary': Salary}
        list_of_Keys.append(ID)
        print('** Employee Added with code :', ID)
    elif choice.lower() == 'del':
        if len(EmpDict) == 0:
            print('** List is Empty !')
        else:
            print('Please enter the code you want to delete from the database : ')
            Key2Del = int(nnn())
            if Key2Del in list(EmpDict.keys()):
                ArchEmpDict[Key2Del]=EmpDict[Key2Del]
                del EmpDict[Key2Del]
                print('** Employee with code', Key2Del, 'was deleted.')
            elif Key2Del not in list(EmpDict.keys()) and Key2Del in list_of_Keys:
                print('Employee already deleted.')
            else:
                print('** Invalid input **')
    elif choice.lower() == 'exit':
        break
    else:
        print('Invalid input, Please try again..')
