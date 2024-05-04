import sqlite3

# Database connection
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Create employee table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS employee
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name TEXT,
             last_name TEXT,
             age INTEGER,
             department TEXT,
             salary REAL)''')

# Employee class
class Employee:
    #Emplyee List as a Class Variable
    employee_list = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        #Methods
        Employee.employee_list.append(self)
        c.execute('''INSERT INTO employee (first_name, last_name, age, department, salary) 
                     VALUES (?, ?, ?, ?, ?)''', (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()
        #Transfer Method
    def transfer(self, new_department):
        self.department = new_department
        # Update database record
        c.execute('''UPDATE employee SET department = ? WHERE first_name = ? AND last_name = ?''',
                  (self.department, self.first_name, self.last_name))
        conn.commit()
        #Fire Method
    def fire(self):
        Employee.employee_list.remove(self)
        # Delete record from database
        c.execute('''DELETE FROM employee WHERE first_name = ? AND last_name = ?''',
                  (self.first_name, self.last_name))
        conn.commit()
        #Show Method
    def show(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @classmethod
    def list_employees(cls):
        for emp in cls.employee_list:
            emp.show()
#CLASSES
# Manager class
class Manager(Employee): #Inheriting from Employee
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        #Calling Parent Class Constructor using super() and passing the required parameters
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department
    #Methods
    def show(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("Salary: [Confidential]")
        print(f"Managed Department: {self.managed_department}")

# Command-line interface
def main():
    #Printing Main Menu
    while True:
        print("\nMenu:")
        print("1. Add new employee (e)")
        print("2. Add new manager (m)")
        print("3. Transfer employee to another department")
        print("4. Fire employee")
        print("5. Show all employees")
        print("6. Exit (q)")
        #Asking for user input
        choice = input("Enter your choice: ")
        #Validating user input
        #If user input is 'e' then ask for employee details
        if choice == 'e':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            Employee(first_name, last_name, age, department, salary)
        #If user input is 'm' then ask for manager details
        elif choice == 'm':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            managed_department = input("Enter managed department: ")
            Manager(first_name, last_name, age, department, salary, managed_department)
        #If user input is '3' then ask for employee details and new department
        elif choice == '3':
            print("Transfer employee to another department:")
            first_name = input("Enter first name of employee: ")
            last_name = input("Enter last name of employee: ")
            new_department = input("Enter new department: ")
            for emp in Employee.employee_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.transfer(new_department)
                    print("Employee transferred successfully.")
                    break
            #If employee not found
            else:
                print("Employee not found.")
        #If user input is '4' then ask for employee details to fire
        elif choice == '4':
            print("Fire an employee:")
            first_name = input("Enter first name of employee: ")
            last_name = input("Enter last name of employee: ")
            for emp in Employee.employee_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.fire()
                    print("Employee fired successfully.")
                    break
            else:
                print("Employee not found.")
        #If user input is '5' then list all employees
        elif choice == '5':
            print("List of all employees:")
            Employee.list_employees()
        #If user input is 'q' then exit the program
        elif choice == 'q':
            print("Exiting program...")
            break
        #If user input is invalid then ask for input again
        else:
            print("Invalid choice. Please try again.")
#Main Function
if __name__ == "__main__":
    main()
