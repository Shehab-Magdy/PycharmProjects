"""
*.We have an employee small system , we offer for the client that a three options:
    1: see all the employees in his system.
    2: add a new employee.
    3: delete a specific employee.
    4: Read data about specific emp.
    5: Update data for a specific emp. view old data and allow to update each one
    6: soft delete instead of delete.
    7: roles of access
*.The system welcome message should contain the three options for the user.
*.The employee data that will be listed or created are : id , name , age , salary.
*.Note : the employee id MUST be unique in the system.
*.When the user asks to add a new employee, the system will automatically generate the id,
  so the user will only add name, age and salary.
*.After any operation, the system will ask the user to choose a new operation or exit from the system.
"""

def num_Only():
    while True:
        x = input()
        if x.isnumeric():
            return eval(x)
        else:
            print('You did not input a number. Please try again')


def login(x):
    uname = input('Please enter your User Name : ')
    if uname in x.keys():
        upassword = input('Please enter your Password : ')
        if upassword == x[uname]:
            return True, uname
        else:
            print('Sorry Password is incorrect, Please try again.')
            return False
    else:
        print('Sorry User name is not exist, Please try again.')
        return False

def listTheEmp(x):
    print(x)
    for k, v in x.items():
        if v['isdeleted'] == 0:
            print('Emp Id is :', k)
            print('emp name is :', v['name'])
            print('emp age is :', v['age'])
            print('emp salary is :', v['salary'])
            print('**************************')


def addNewEmp(x):
    listofkeys = list(x.keys())
    if len(x) == 0:
        id = 1
    else:
        id = max(listofkeys) + 1
    n = input('Enter the name of the new emplyee : ')
    print('Enter the age of the new emplyee : ',end='')
    a=num_Only()
    print('Enter the salary of the new emplyee : ',end='')
    s=num_Only()
    x[id] = {'name': n, 'age': a, 'salary': s, 'isdeleted': 0}
    print('Emp added with ID : ', id)
    return x


def delEmp(x):
    if len(x) == 0:
        print('No Items to delete')
        return x
    else:
        delno = int(input('enter the ID to delete : '))
        listofkeys = list(x.keys())
        if delno in listofkeys:
            x.pop(delno)
            return x
        else:
            print('Emp not exist')
            return x


def soft_delete(x):
    if len(x):
        delid = int(input('enter the ID to delete : '))
        listofkeys = list(x.keys())
        if delid in listofkeys:
            x[delid]['isdeleted'] = 1
            print('Employee is deleted')
            return x
        else:
            print('Emp not exist')
            return x
    else:
        print('No Items to delete')
        return x


def empread(x):
    if len(x) == 0:
        print('List is empty')
    else:
        idToRead = int(input('Please input the id of the employee to view : '))
        listofkeys = list(x.keys())
        if idToRead in listofkeys and x[idToRead]['isdeleted'] == 0:
            print('Emp Id is :', idToRead)
            print('emp name is :', x[idToRead]['name'])
            print('emp age is :', x[idToRead]['age'])
            print('emp salary is :', x[idToRead]['salary'])
            print('**************************')
        else:
            print('Id is not exist')


def update_Emp(x):
    if len(x) == 0:
        print('List is empty')
    else:
        idToupdate = int(input('Please input the id of the employee to update : '))
        listofkeys = list(x.keys())
        if idToupdate in listofkeys and x[idToupdate]['isdeleted'] == 0:
            print('Emp Id is :', idToupdate)
            print('emp name is :', x[idToupdate]['name'])
            n = input('Type the new name : ')
            print('emp age is :', x[idToupdate]['age'])
            a = int(input('Type the new age : '))
            print('emp salary is :', x[idToupdate]['salary'])
            s = int(input('Type the new salary : '))
            x[idToupdate] = {'name': n, 'age': a, 'salary': s, 'isdeleted': 0}
            print('Emp with ID : ', idToupdate, 'is updated.')
            return x
        else:
            print('Id is not exist')


welcomemessage = 'Welcome to Our system....' \
                 '\nDo you want to see a list of the Employees? Please type "List"' \
                 '\nDo you want to Add a new employees? Please type "Add"' \
                 '\nDo you want to Delelet current employees? Please type "Del"' \
                 '\nDo you want to Read data for a specefic employees? Please type "Read"' \
                 '\nDo you want to Update data for a specefic employees? Please type "Update"' \
                 '\nWhat is your choice? '

repetedmessage = 'Choose a new operation or Exit the system....' \
                 '\nDo you want to see a list of the Employees? Please type "List"' \
                 '\nDo you want to Add a new employees? Please type "Add"' \
                 '\nDo you want to Delelet current employees? Please type "Del"' \
                 '\nDo you want to Read data for a specefic employees? Please type "Read"' \
                 '\nDo you want to Update data for a specefic employees? Please type "Update"' \
                 '\nDo you want to exit? Please type "Exit"' \
                 '\nWhat is your choice? '
usage = 1
empList = {}
usersList={'admin':'123','user':'123456'}
passvalied, user = login(usersList)
if passvalied:
    while True:
        if usage == 1:
            operation = input(welcomemessage)
            usage += 1
        else:
            operation = input(repetedmessage)
        if operation.lower() == 'list':
            if len(empList) == 0:
                print('List is empty')
            else:
                listTheEmp(empList)
        elif operation.lower() == 'add':
            empList = addNewEmp(empList)
        elif operation.lower() == 'del':
            if user=='admin':
                empList = soft_delete(empList)
            else:
                print('You are not authorized to delete.')
        elif operation.lower() == 'read':
            empread(empList)
        elif operation.lower() == 'update':
            if user=='admin':
                empList = update_Emp(empList)
            else:
                print('You are not authorized to update.')
        elif operation.lower() == 'exit':
            break
        else:
            print('Invalid input')
