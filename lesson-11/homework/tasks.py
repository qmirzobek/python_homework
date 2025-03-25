import sqlite3

def task_1():
    # Connect to SQLite database
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)
    
    # Insert data
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
    
    # Update Jadzia Dax to Ezri Dax
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    
    # Query and display Bajoran species
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print("Bajoran Characters:", cursor.fetchall())
    
    # Delete characters aged over 100 years
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    
    # Add Rank column
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    
    # Update Rank values
    rank_data = [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ]
    cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", rank_data)
    
    # Retrieve sorted data
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("Characters sorted by Age:", cursor.fetchall())
    
    conn.commit()
    conn.close()

def task_2():
    # Connect to SQLite database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)
    
    # Insert data
    books = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books)
    
    # Update year published for 1984
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    
    # Query and display Dystopian books
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    print("Dystopian Books:", cursor.fetchall())
    
    # Delete books published before 1950
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    
    # Add Rating column
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    
    # Update Rating values
    rating_data = [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ]
    cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", rating_data)
    
    # Retrieve sorted books by year published
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("Books sorted by Year Published:", cursor.fetchall())
    
    conn.commit()
    conn.close()

# Run both tasks
task_1()
task_2()
