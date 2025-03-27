import requests
import sqlite3
import csv
from pathlib import Path
from bs4 import BeautifulSoup





current_dir = Path(__file__).resolve().parent

csv_name=current_dir / 'jobs.csv'
db_name=current_dir / 'jobs.db'

url = 'https://realpython.github.io/fake-jobs'
data_header=['JobTitle','CompanyName','Location','JobDescription','ApplicationLink']
def write_to_db(cards_list):
    """
    Write the data to the database
    """
    global db_name
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Jobs (
            JobTitle TEXT,
            CompanyName TEXT,
            Location TEXT,
            JobDescription TEXT,
            ApplicationLink TEXT
        )
    """) 

    for card in cards_list:
        cursor.execute("INSERT INTO Jobs (JobTitle, CompanyName, Location, JobDescription, ApplicationLink) VALUES (?, ?, ?, ?, ?)", (card['title'], card['company'], card['location'], card['description'], card['link']))
    conn.commit()
    conn.close()

def export_db_to_csv(db_name, csv_name):
    """
    Export the database to csv
    """
    global data_header
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Jobs")
    data = cursor.fetchall()
    conn.close()
    
    # with open(csv_name, 'w') as file:
    #     for row in data:
    #         file.write(','.join(map(str, row)) + '\n')
    with open(csv_name, mode='w',newline='') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(data_header)
        writer.writerows(data)

def filtering(by="Location"):
    """
    Filter the data by location or company name
    """


    global db_name
    if(by[:2]=='com'):
        by="CompanyName"
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Jobs")
    data=cursor.fetchall()
    conn.close()
    # print(data)
    return data

def print_data(data):
    """
    Print the data
    """
    for row in data:
        if(type(row)==list):
            for i in row:
                print(i,end="\t")
            print()
        elif(type(row)==tuple):
            for i in row:
                print(i,end="\t")
            print()
        elif(type(row)==dict):
            for key in row:
                print(key,":",row[key],end="\t")
            print()
        else:
            print(row)


def scrape_job_list():
    """
    Scrape job list from the website
    """
    global url
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    cards=soup.find_all('div',class_='card-content')
    cards_list=list()
    for card in cards:
        title=card.find(class_='title').text.strip()
        company=card.find(class_='company').text.strip()
        location=card.find(class_='location').text.strip()
        description=card.find(class_='content').text.strip()
        a=card.find_all('a')
        if(len(a)>1):
            link=a[1]['href']
        else:
            link=a[0]['href']
        card_dict={
            'title':title,
            'company':company,
            'location':location,
            'description':description,
            'link':link
        }
        cards_list.append(card_dict)

    return cards_list
def get_data():
    """
    Get all data from SQLite
    """
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Jobs")
    data = cursor.fetchall()
    conn.close()
    return data
def incremental_loading():
    """
    Incremental loading of the job list
    """
    global db_name
    global url
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Jobs")
    data = cursor.fetchall()
    conn.close()
    job_list=scrape_job_list()
    new_jobs=list()
    for job in job_list:
        if (job['title'] not in [row[0] for row in data] and job['company'] not in [row[1] for row in data] and job['location'] not in [row[2] for row in data]):
            new_jobs.append(job)
    write_to_db(new_jobs)

def update_tracking():
    """
    Update the tracking of the job list
    """
    global db_name
    data2=scrape_job_list()
    # print(data2)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for data in data2:
        cursor.execute("SELECT * FROM Jobs WHERE JobTitle = '"+data["title"]+"' AND CompanyName = '"+data['company']+"' AND Location = '"+data['location']+"'")
        if(cursor.fetchone() is None):
            cursor.execute("INSERT INTO Jobs (JobTitle, CompanyName, Location, JobDescription, ApplicationLink) VALUES (?, ?, ?, ?, ?)", (data['title'], data['company'], data['location'], data['description'], data['link']))
        else:
            cursor.execute("UPDATE Jobs SET JobDescription = '"+data['description']+"', ApplicationLink = '"+data['link']+"' WHERE JobTitle = '"+data['title']+"' AND CompanyName = '"+data['company']+"' AND Location = '"+data['location']+"'")
    conn.commit()

    print('Updated successfully')

def main():
    global db_name
    global url
    cards_list=scrape_job_list()
    write_to_db(cards_list)
    export_db_to_csv(db_name, 'jobs.csv')
    print_data(filtering())
    # update_tracking()
    incremental_loading()
    print_data(get_data())

main_text="""
1. Scrape job list
2. Write to database
3. Export database to csv
4. Filter by location
5. Update tracking
6. Incremental loading
7. Get All data from SQLite
8. Exit
"""

def repeat_able_main():
    global db_name
    global csv_name
    global url
    while(True):
        print(main_text)
        choice=input("Enter your choice: ")
        if(choice=="1"):
            cards_list=scrape_job_list()
            print_data(cards_list)
        elif(choice=="2"):
            cards_list=scrape_job_list()
            write_to_db(cards_list)
        elif(choice=="3"):
            print('Exporting database to csv')
            csv_name_user=input("Enter the csv name only: ")
            if(len(csv_name_user)>0):
                csv_name=csv_name_user+'.csv'
            export_db_to_csv(db_name, csv_name)
        elif(choice=="4"):
            by=input("Enter the filter by: ")
            # value=input("Enter the value: ")
            if(len(by)>0):
                
                print_data(filtering(by))
            else:
                print_data(filtering())
            
        elif(choice=="5"):
            update_tracking()
            # pass
        elif(choice=="6"):
            incremental_loading()
        elif(choice=="7"):
            print_data(get_data())
        elif(choice=="8"):  
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    # main()
    repeat_able_main()



