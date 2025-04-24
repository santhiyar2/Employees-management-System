# Dictionary to store employee details
employees = {}

# Function to add Employee
def add_employee(emp_id, name, age, salary, department):
    employees[emp_id] = {
        "Name": name,
        "Age": age,
        "Salary": salary,
        "Department": department
    }
    print(f"Employee {name} added Successfully")

# Function to view all Employees
def view_employee():
    if employees:
        for emp_id, emp_details in employees.items():
            print(f"ID: {emp_id}, Details: {emp_details}")
    else:
        print("\nNo Employees Added Yet!\n")

# Function to update Employees
def update_employee(emp_id, name=None, age=None, salary=None, department=None):
    try:
        if emp_id in employees:
            if name:
                employees[emp_id]["Name"] = name
            if age:
                employees[emp_id]["Age"] = age
            if salary:
                employees[emp_id]["Salary"] = salary
            if department:
                employees[emp_id]["Department"] = department
            print(f"Employee {emp_id} Updated Successfully")
        else:
            print(f"Employee with ID {emp_id} Not Found")
    except KeyError as e:
        print(f"Error Updating Employee Details: {e}")


# Function to Remove Employees

def remove_employee(emp_id):
    try:
        emp = employees.pop(emp_id)

        print(f"Employee {emp["Name"]} Removed Successfully" )

    except KeyError :

        print(f"Employee With ID {emp_id} not found")

# Function to Save Employees data to a file without JSON

def save_to_file(filename):
    try:

        with open(filename,"w")as file:

            for emp_id,details in employees.items():

                line = f"{emp_id} :-> {details["Name"]},{details["Age"]},{details["Salary"]},{details["Department"]} \n "
                file.write(line)

        print("Employee data Saved Successfully")

    except Exception as e:
        print(f"Error : {e}")

# Function to Load employee data from file without JSON

def load_from_file(filename):

    try:

        with open(filename,"r")as file:

            global employees
            employees = {} # Clear the existing dictionary before loading

            for line in file:
                emp_data = line.strip().split(",")
                emp_id,name,age,salary,department = emp_data

                employees[emp_id]={
                    "Name": name,
                    "Age": age,
                    "Salary": salary,
                    "Department": department
                }
        print("Employee data Loaded Successfully...!")
    except FileNotFoundError:

        print(f"File {filename} not found")

    except Exception as e:

        print(f"Error : {e}")


# Menu Function
def menu():
    while True: 
        print("\nWelcome To The Employee Management System:")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Load From File")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee name: ")
            age = input("Enter Employee age: ")
            salary = input("Enter Employee salary: ")
            department = input("Enter Employee department: ")
            add_employee(emp_id, name, age, salary, department)

        elif choice == "2":
            view_employee()

        elif choice == "3":
            emp_id = input("Enter Employee ID to Update: ")
            name = input("Enter New Name (Leave Blank to Skip): ") or None
            age = input("Enter New Age (Leave Blank to Skip): ") or None
            salary = input("Enter New Salary (Leave Blank to Skip): ") or None
            department = input("Enter New Department (Leave Blank to Skip): ") or None
            update_employee(emp_id, name, age, salary, department)

        elif choice == "4":

            emp_id=input("Enter Employee ID to Remove : ")

            remove_employee(emp_id)

        elif choice == "5":
           
           filename = input("Enter Your FileName To Save :")

           save_to_file(filename)

        elif choice == "6":
           filename = input("Enter FileName to Load : ")
           load_from_file(filename)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()