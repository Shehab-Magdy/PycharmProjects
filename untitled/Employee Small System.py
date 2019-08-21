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
EmpList = {}
usage = 1
while True:
    choice = input('Welcome to Our system....'
                   '\nDo you want to see a list of the Employees? Please type "List"'
                   '\nDo you want to Add a new employees? Please type "Add"'
                   '\nDo you want to Delelet current employees? Please type "Del"'
                   '\nWhat is your choice?')
    usage += 1
    if usage == 1:
        pass
    else:
        choice = input('Choose a new operation or Exit the system....'
                       '\nDo you want to see a list of the Employees? Please type "List"'
                       '\nDo you want to Add a new employees? Please type "Add"'
                       '\nDo you want to Delelet current employees? Please type "Del"'
                       '\nDo you want to exit? Please type "Exit"'
                       '\nWhat is your choice?')

    x = list(EmpList.keys())
    l = len(EmpList)
    if choice == 'List' or choice == 'list':
        if l <1:
            print('There are no items to show.')
        else:
            for i in x:
                print('Id :',i)
                for k, v in EmpList[i].items():
                    print(k, ':', v)
                print('---------------------')
    elif choice == 'Add' or choice == 'add':
        N = input('Please enter the name : ')
        A = input('Please enter the age : ')
        S = input('Please enter the salary : ')
        l+=1
        if l == 1:
            EmpList[1] = {'Name': N, 'Age': A, 'Salary': S}
        else:
            EmpList[l] = {'Name': N, 'Age': A, 'Salary': S}
        print('Employee Added with code :',l)
    elif choice == 'Del' or choice == 'del':
        d = int(input('Please enter the code you want to delete from the database : '))
        del EmpList[d]
        print('Employee with code',d,'was deleted.')
    elif choice == 'Exit' or choice == 'exit':
        break
    else:
        print('Invalid input, Please try again..')
