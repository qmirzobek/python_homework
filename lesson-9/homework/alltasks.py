import csv
import json

# Task 1: Library Management System

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.borrow_limit = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise BookNotFoundException("This book was not borrowed by the member.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException("Book not found in library.")

    def borrow_book(self, member, title):
        book = self.find_book(title)
        member.borrow_book(book)
        print(f"{member.name} borrowed {title}.")

    def return_book(self, member, title):
        book = self.find_book(title)
        try:
            member.return_book(book)
            print(f"{member.name} returned {title}.")
        except BookNotFoundException as e:
            print(e)

    def display_available_books(self):
        available_books = [book.title for book in self.books if not book.is_borrowed]
        if available_books:
            print("Available books:", ", ".join(available_books))
        else:
            print("No books are currently available.")

# Task 2: Student Grades Management

def read_grades(filename):
    grades = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grades.append({"Name": row["Name"], "Subject": row["Subject"], "Grade": int(row["Grade"])} )
    return grades

def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}
    
    for record in grades:
        subject = record["Subject"]
        grade = record["Grade"]
        subject_totals[subject] = subject_totals.get(subject, 0) + grade
        subject_counts[subject] = subject_counts.get(subject, 0) + 1
    
    averages = {subject: total / subject_counts[subject] for subject, total in subject_totals.items()}
    return averages

def write_average_grades(averages, output_file):
    with open(output_file, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

# Task 3: JSON Handling

def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks
    print(f"Total tasks: {total_tasks}\nCompleted tasks: {completed_tasks}\nPending tasks: {pending_tasks}\nAverage priority: {average_priority:.2f}")

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Example Usage
if __name__ == "__main__":
    # Task 1 Test
    library = Library()
    book1 = Book("Python Basics", "John Doe")
    book2 = Book("Advanced Python", "Jane Smith")
    member1 = Member("Alice")
    library.add_book(book1)
    library.add_book(book2)
    library.add_member(member1)
    try:
        library.borrow_book(member1, "Python Basics")
        library.borrow_book(member1, "Advanced Python")
        library.return_book(member1, "Python Basics")
    except Exception as e:
        print(e)
    
    library.display_available_books()
    
    # Task 2 Test
    grades = read_grades("grades.csv")
    averages = calculate_average_grades(grades)
    write_average_grades(averages, "average_grades.csv")
    
    # Task 3 Test
    tasks = load_tasks("tasks.json")
    display_tasks(tasks)
    calculate_task_stats(tasks)
    convert_json_to_csv("tasks.json", "tasks.csv")
