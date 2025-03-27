from pathlib import Path
from bs4 import BeautifulSoup

current_dir = Path(__file__).resolve().parent

with open(current_dir / 'weather.html') as file:
    html_doc = file.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
table=soup.table
# print(table)
tr=table.find_all('tr')
information=list()
def getTemperature(row):
    return int(row[1][:-3])
for row in tr:
    td=row.find_all('td')
    row=[i.text for i in td]
    if(len(row)>2):
        row[1]=getTemperature(row)
        information.append(row)
    # print(row)



print("day \t","temperture \t","description")
for i in information:
    if(len(i)>2):
        print(i[0][:3],"\t",i[1],"\t\t",i[2],end="\n")

temp=[i[1] for i in information]
max=max(temp)
indexmax=temp.index(max)
print("The highest temperature is",max,"on",information[indexmax][0])

sunnyDaysIndex=[i for i in range(len(information)) if information[i][2]=="Sunny"]
for i in sunnyDaysIndex:
    print("The sunny day is on",information[i][0])
