
# global filename
filename="employees.txt"
def createFile(filename="employees.txt"):
    # try:
    #     file=open(filename,mode='w')
    # except IOError:
    #     print('There was an error with file creation.')
    try:
        file = open(filename, mode='w')
        # file.write('banana')
        file.close()
    except IOError:
        print('Error')
# createFile()

def appendNewEmployee(employeeID,name,position,salary):
    global filename
    try:

        file=open(filename,mode='a')
        employeeRecord="\n"
        employeeRecord=employeeID+", "+name+", "+position+", "+ salary
        # employeeRecord+=name+
        file.write(employeeRecord)
        file.close()
    except IOError:
        print("There was an error with working on file!")
def viewAll():
    global filename
    try:
        # file=open(filename,mode="r")
        # all=file.read()
        print("Employee ID, Name, Position, Salary")
        with open('employees.txt') as file_handler:
            for line in file_handler:
                if(line!="\n"):
                    print(line)
        # file.close()
    except IOError:
        print("Error arose with working on the file")

def updateEmployee(employeeID,name="",position="",salary=""):
    global filename
    try:
        # file=open(filename,mode="r")
        # all=file.read()
        # print("Employee ID, Name, Position, Salary")
        records=list()
        with open(filename) as file_handler:
            for line in file_handler:
                record=line.split(',')
                line1=line
                if(record[0]==str(employeeID)):
                    # print(record)
                    if(name==""):
                        name=record[1]
                    if(position==""):
                        position=record[2]
                    if(salary==""):
                        salary=record[3]
                    newRecord=employeeID+","+name+","+position+","+salary
                    line1=newRecord
                # print(record)
                records.append(line1)
        
        with open(filename, 'w') as file_handler:
            for record in records:
                # record=record.join()
                file_handler.write((record))
        print("Employee record is updated successfully!")
        # file.close()
        # file_handler.close()
    except OSError:
        print("Error arose with working on the file")


def searchFor(employeeID=""):
    global filename
    try:
        # file=open(filename,mode="r")
        # all=file.read()
        # print("Employee ID, Name, Position, Salary")
        # for line in all:
        
        if(employeeID==""):
            print("You haven't entered anything")
            return
        
        with open(filename) as file_handler:
            for line in file_handler:
                # print(line)
                # if(line[0,3]==employeeID):
                #     print(line)
                record=line.split(",")
                if(str(employeeID)==record[0]):
                    print("Employee ID, Name, Position, Salary")
                    print(line)
        # file.close()
    except OSError:
        print("Error arose with working on the file")

def deleteEmployeeRecord(employeeID=""):
    global filename
    try:
        # file=open(filename,mode="r")
        # all=file.read()
        # print("Employee ID, Name, Position, Salary")
        records=list()
        with open(filename) as file_handler:
            for line in file_handler:
                record=line.split(',')
                line1=line
                if(record[0]!=str(employeeID)):
                    print(record)
                    records.append(line1)
                
        
        with open(filename, 'w') as file_handler:
            for record in records:
                # record=record.join()
                file_handler.write((record))
        print("Employee record is deleted successfully!")
        # file.close()
        # file_handler.close()
    except OSError:
        print("Error arose with working on the file")


# createFile()
# viewAll()
# # updateEmployee("1003")
# # viewAll()
# # deleteEmployeeRecord('1003')
# viewAll()
while(True):
    print("""  
   1. Add new employee record
   2. View all employee records
   3. Search for an employee by Employee ID
   4. Update an employee's information
   5. Delete an employee record
   6. Exit""")
    option=int(input("Enter your option: "))
    if(option==1):
        while(True):
            employeeID=input("Enter employee ID: ")
            name=input("Enter employee name: ")
            position=input("Enter employee position: ")
            salary=input("Enter employee salary: ")
            if(employeeID!="" and name!="" and position!="" and salary!=""):
                break
            print('You should fill all the fields')
        # name
        appendNewEmployee(employeeID,name,position,salary)
    elif(option==2):
        viewAll()
    elif(option==3):
        employeeID=input("Search employee record by ID: ")
        searchFor(employeeID)
    elif(option==4):
        while(True):
            employeeID=input("Enter employee ID: ")
            name=input("Enter employee name: ")
            position=input("Enter employee position: ")
            salary=input("Enter employee salary: ")
            if(employeeID!="" and name!="" and position!="" and salary!=""):
                break
            print('You should fill all the fields')
        # name
        updateEmployee(employeeID,name,position,salary)
    elif(option==5):
        accept=["yes",'y']
        while(True):
            employeeID=input("Enter employee ID: ")
            acceptOption=input("Are you sure you want to delete this employee? Yes,yes,y/No,no,n")
            if(employeeID!=""):
                if(acceptOption.lower() in accept):
                    deleteEmployeeRecord(employeeID)
                    # print("Employee is deleted successfully!")
                break
            if(acceptOption.lower() not in accept):
                break
    elif(option==6):
        # quit()
        break
    else:
        print("Option you entered is not in the list!")        

quit()

