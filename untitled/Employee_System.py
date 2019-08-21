dict_emp = {}
choice = 0
key=0
ans="yes"
check = False
print("Hello to the employee system ,Please :\n", "press 1 for see all employees in the system\n", "press 2 for add new employee in the system\n", "press 3 for see delete employee in the system")
while(True):
    if ans == "yes" or ans == "Yes":
        choice = int(input("Enter your choice :___"))
        if choice == 1:
            if len(dict_emp) == 0:
                print("NO Employees are found ")
            else:
                print("ID", "  ", "Eployee's Name ", "  ", "Age", "  ", "Salary")
                for key, value in dict_emp.items():
                    print(key, "   ", value['name'], "    ", value['age'], "    ", value['salary'])
                choice = 0
                print("Do you want another operation ? yes/No")
                ans = input("write yes/No :")
        elif choice == 2:
            emp_name = input("Enter the employee's name : ")
            emp_age = int(input("Enter the employee's age :"))
            emp_salary = int(input("Enter the employee's salary :"))
            key=len(dict_emp)+1
            dict_emp.update({key:{"name" : emp_name,"age" : emp_age,"salary" : emp_salary}})
            print("The Employee is added.")
            emp_salary = 0
            emp_name = ""
            emp_age = 0
            choice = 0
            print("Do you want another operation ?")
            ans = input("Write yes/No : ")
        elif choice == 3:
            emp_id = int(input("Enter the employee's ID who wanted to delete him:"))
            for emp in list(dict_emp.keys()):
                if emp == emp_id:
                    del dict_emp[emp]
                    print("Employee is deleted..")
                    check = True
            if check == False:
                print("This is employee isn't found..")
            emp_salary = 0
            emp_name = ""
            emp_age = 0
            choice = 0
            check = False
            print("Do you want another operation ?")
            ans = input("Write yes/No : ")
        else:
            print("Invalid choice, please press 1,2 or 3")
    elif ans == "No" or ans == "no":
        print("See you soon, GOOBDYE...")
        break
    else:
        print("Please, write yes or No")
        ans = input("Write yes/No : ")
