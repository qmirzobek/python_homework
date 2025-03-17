

class Employee:

    
    def __init__(self,employee_id: int, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def update(self,employee_id: int, name,position, salary):
        """
        Update an employee record
        """
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary=salary

    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"

class EmployeeManager:


    def __init__(self):
        self.filename="employees.txt"
        self.employees = []
        self.createFile()
        self.main()

    def add_employee(self, employee: Employee):
        """
        Add employee to the list
        """
        try:
            self.employees.append(employee)
            return True
        except Exception:
            return False

    def readContent(self):
        """
        Read content of the file
        """
        try:
            with open(self.filename) as file_handler:
                    for line in file_handler:
                        if(line!="\n"):
                            # print(line)
                            record=line.split(',')
                            # print(record)
                            record[-1]=(record[-1].split("\n"))[0]

                            emp=Employee(int(record[0]),record[1],record[2],record[3])
                            # emp=Employee(tuple(record))
                            self.employees.append(emp)
        except:
            print("Error occured")
    def createFile(self):
        """
        Create file if it does not exist
        """
        try:
            
            self.readContent()
            return True
        except FileNotFoundError:
            try:
                file = open(self.filename, mode='w')
                # file.write('banana')
                file.close()
                return True
            except OSError:
                print('Error occured with creating file')
                return False
        
    def searchFor(self, employeeID=-1):
        """
        Search for an employee by employee ID
        """
        try:
        
            if(employeeID==-1):
                print("You haven't entered anything")
                return False
            
            # with open(self.filename) as file_handler:
            for record in self.employees:
                # print((self.employees[i])[0])
                if(int(employeeID)==int(record.employee_id)):
                        return record
            
                    
            else:
                return False
        except Exception:
            print("Error arose with working on the file")
            return False
    def writeToFile(self):
        """
        Write to file
        """
        try:
            with open(self.filename, 'w') as file_handler:
                for record in self.employees:
                    file_handler.write('\n')
                    file_handler.write(str(record))
            # print("Employee record is updated successfully!")
            return True
            # file.close()
            # file_handler.close()
        except Exception:
            print("Error arose with working on the file")
            return False
    def appendNewEmployee(self,employeeID,name,position,salary):
        # global filename
        """
        Add new employee record
        """
        try:
            
            employeeRecord=Employee(employeeID,name,position,salary)
            added=self.add_employee(employeeRecord)
            self.writeToFile()
            return added
        except Exception:
            print("There was an error with working on file!")
            return False

    def updateEmployee(self,employeeID: int,name="",position="",salary=""):
        """
        Update an employee record
        """
        try:
            for record in self.employees:
                if int(record.employee_id)==int(employeeID):
                    record.update(employeeID,name,position,salary)
                
            
            write=self.writeToFile()
            self.readContent()
            return write
        except Exception:
            print("Error arose with working on the file")
            return False
        
    def viewAll(self):
        """
        View all employee records
        """
        # global filename
        try:
            self.readContent()
            # file=open(filename,mode="r")
            # all=file.read()
            print("Employee ID, Name, Position, Salary")
            with open(self.filename) as file_handler:
                for line in file_handler:
                    if(line!="\n"):
                        print(line,end="")
            # file.close()
        except Exception:
            print("Error arose with working on the file")
    def deleteEmployeeRecord(self,employeeID: int):
        """
        Delete an employee record by employee ID
        """
        try:
            records=list()
            for line in self.employees:
                if(int(line.employee_id)!=int(employeeID)):
                    # print(record)
                    records.append(line)
            self.employees.clear()
            self.employees=records
            
            self.writeToFile()
            print("Employee record is deleted successfully!")
            return True
        except Exception:
            print("Error arose with working on the file")
            return False

    def main(self):
        """
        Main function to run the program
        """
        while(True):
            print("""  
        1. Add new employee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee's information
        5. Delete an employee record
        6. Exit""")
            try:
                option=int(input("Enter your option: "))
            except TypeError:
                print("There is an error with your input")
            if(option==1):
                while(True):
                    try:
                        employeeID=int(input("Enter employee ID: "))
                        name=input("Enter employee name: ")
                        position=input("Enter employee position: ")
                        salary=input("Enter employee salary: ")
                        if(employeeID>0 and name!="" and position!="" and salary!=""):
                            break
                        print('You should fill all the fields')
                    except Exception:
                        print("Please pay attention to requirements of fields")
                
                # name
                self.appendNewEmployee(employeeID,name,position,salary)
            elif(option==2):
                self.viewAll()
            elif(option==3):
                try:
                    employeeID=int(input("Search employee record by ID: "))
                    flag=self.searchFor(employeeID)
                    if(flag==False):
                        print("Employee is not found")
                    else:
                        print(flag)
                except:
                    print("Employee id should be integer")
                
            elif(option==4):
                while(True):
                    try:
                        employeeID=int(input("Enter employee ID: "))
                        name=input("Enter employee name: ")
                        position=input("Enter employee position: ")
                        salary=input("Enter employee salary: ")
                        if(employeeID>0 and name!="" and position!="" and salary!=""):
                            break
                        print('You should fill all the fields')
                    except Exception:
                        print("There was an error with your inputs")
                
                # name
                self.updateEmployee(employeeID,name,position,salary)
            elif(option==5):
                accept=["yes",'y']
                while(True):
                    try:
                        employeeID=int(input("Enter employee ID: "))
                    except:
                        print("Employee id should be integera")
                    acceptOption=input("Are you sure you want to delete this employee? Yes,yes,y/No,no,n")
                    if(employeeID!=""):
                        if(acceptOption.lower() in accept):
                            self.deleteEmployeeRecord(employeeID)
                            # print("Employee is deleted successfully!")
                        break
                    if(acceptOption.lower() not in accept):
                        break
            elif(option==6):
                # quit()
                break
            else:
                print("Option you entered is not in the list!")        


EmployeeManager()




