


class Task:



    def __init__(self,task_id: int,title,description,due_date,status):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status
        
    def update(self,task_id, int,title,description,due_date,status):
        """
        Update a task record
        """
        self.task_id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def __str__(self):
        return f"{self.task_id},{self.title},{self.description},{self.due_date},{self.status}"


class TaskManager:

    def __init__(self, filename="tasklist.txt"):
        self.task_list=list()
        self.filename=filename
        self.checkFile()
        self.load()
        
    def checkFile(self):
        """
        Check if file exists, if not create it
        """
        try:
            file=open(self.filename,mode="r")
            file.close()
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
    def viewTasks(self):
        """
        View all tasks
        """
        try:
            print("Tasks:\n")
            if(len(self.task_list)>0):
                for task in self.task_list:
                    print(task)
                return True
            return False
        except Exception:
            print("Error happend")
            return False
        
    def addNewTask(self, task: Task):
        """
        Add a new task to the task list
        
        """
        try:
            (self.task_list).append(task)
            return True
        except Exception:
            print('Error happend')
            return False
    def update(self,task_id: int,title,description,due_date,status):
        """
        Update a task by task_id
        
        """
        try:
            records=list()
            if(len(self.task_list)==0):
                print("No tasks to update")
                return 
            for task in self.task_list:
                if(task.task_id==task_id):
                    records.append(Task(task_id,title,description,due_date,status))
                else:
                    records.append(task)
            self.task_list.clear()
            self.task_list=records
            # self.save()
            return True
        except Exception:
            print("Error happend with update")
            return False
    def delete(self,task_id: int):   
        """
        Delete a task by task_id
        
        """ 
        try:
            records=list()
            if(len(self.task_list)==0):
                print("No tasks to delete")
                return 
            for task in self.task_list:
                if(task.task_id!=task_id):
                    records.append(task)
            self.task_list.clear()
            self.task_list=records
            # self.save()
            return True
        except Exception:
            print("Error happend with update")
            return False
    def save(self):
        """
        Save tasks to file
        It is much more easier to save tasks to file than loading tasks from file
        File name can be passed as an argument to the constructor
        """
        try:
            
            with open(self.filename,mode="w") as file_handler:
                
                c=0
                for task in self.task_list:
                    
                    if(c!=0):
                        file_handler.write("\n")

                    file_handler.write(str(task))
                    c+=1
            self.task_list.clear()
            self.load()
            return True
        except Exception:
            print("Error happend")
            return False
    def load(self):
        """
        Load tasks from file
        It is much more easier to load tasks from file than saving tasks to file
        File name can be passed as an argument to the constructor
        Easier to make this code compatible with other file formats like CSV, JSON, etc.
        """
        try:
            
            flag=self.checkFile()
            if(len(self.task_list)>0):
                self.save()
            self.task_list.clear()
            with open(self.filename) as file_handler:
                for line in file_handler:
                    line1=(line.split('\n'))[0].split(",")
                    self.task_list.append(Task(int(line1[0]),line1[1],line1[2],line1[3],line1[4]))
            return flag
        except Exception:
            print("Error happend")
            return False

    def filterByStatus(self,status):
        """
        Filter tasks by status
        """
        print(status,"Tasks")
        for task in self.task_list:
            if(task.status==status):
                print(task)
        
    def main(self):
        """
        Main function to run the application
        """
        print(
    """
    Welcome to the To-Do Application!
    1. Add a new task
    2. View all tasks
    3. Update a task
    4. Delete a task
    5. Filter tasks by status
    6. Save tasks
    7. Load tasks
    8. Exit

    """
            )
        while(True):
            
            try:
                option=int(input("Enter  your choice: "))
                match option:
                    case 1:
                        try:
                            task_id=int(input("Enter Task ID: "))
                            title=input("Enter Title: ")
                            description=input("Enter Description: ")
                            due_date=input("Enter Due Date (YYYY-MM-DD): ")
                            status=input("Enter Status (Pending/In Progress/Completed): ")
                            flag=self.addNewTask(Task(task_id=task_id,title=title,description=description,due_date=due_date,status=status))
                            if(flag):
                                print("Task added successfully!")
                            else:
                                print("There was an error")
                        except Exception:
                            print("Enter everything as required!")
                    case 2:
                        self.viewTasks()
                    case 3:
                        try:
                            task_id=int(input("Enter Task ID: "))
                            title=input("Enter Title: ")
                            description=input("Enter Description: ")
                            due_date=input("Enter Due Date (YYYY-MM-DD): ")
                            status=input("Enter Status (Pending/In Progress/Completed): ")
                            flag=self.update(task_id=task_id,title=title,description=description,due_date=due_date,status=status)
                            if(flag):
                                print("Task updated successfully!")
                            else:
                                print("There was an error")
                        except Exception:
                            print("Enter everything as required!")
                    case 4:
                        try:
                            task_id=int(input("Enter Task ID: "))
                            flag=self.delete(task_id=task_id)
                            if(flag):
                                print("Task deleted successfully!")
                            else:
                                print("There was an error")
                        except Exception:
                            print("Enter everything as required!")
                    case 5:
                        # stat_list=list("Pending","In Progress","Completed")
                        print("Filter tasks by status")
                        # while(True):
                        status=input("Enter Status (Pending/In Progress/Completed): ")
                            # if(status in stat_list):
                            #     break
                        # print("You can only use ",end="")
                        # print(stat_list)
                        self.filterByStatus(status)
                    case 6:
                        flag=self.save()
                        if(flag):
                            print("Tasks are saved successfully!")
                        else:
                            print("There was an error")
                    case 7:
                        flag=self.load()
                        if(flag):
                            print("Tasks are loaded successfully!")
                        else:
                            print("There was an error")
                    case 8:
                        self.save()
                        return            
                    case _:
                        print("You can only enter those choices above!")

            except Exception:
                print("You should enter integer value")
            
taskmanager=TaskManager("tasklist.txt")
taskmanager.main()