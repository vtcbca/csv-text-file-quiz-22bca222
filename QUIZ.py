

### 8.  Create Contact.csv file which contain name,contact. Use "|" as Delimiter.
###  Search perticular contact by entering person name . 

#### creating contact.csv and take records.
import csv
f=open('c:\\22bca222\\python\\SQLITE3\\contact.csv', 'w',newline='')
csv_w=csv.writer(f)
column=['NAME','CONTACT']
rec=[['om',9876576475],['sai',4534723545],['ram',7597863756],['yug',5465326556]]
v_w.writerow(column)
csv_w.writerows(rec)
f.close()

#### print records

with open('c:\\22bca222\\python\\SQLITE3\\contact.csv', 'r') as file:
    csv_r=csv.reader(file)
    for rec in csv_r:
        print(rec)

#### Search perticular contact by entering person name .

f=open('c:\\22bca222\\python\\SQLITE3\\contact.csv', 'r',newline='')
c_reader=csv.reader(f)
name=input("enter name that you want to search:")
for row in c_reader:
    if row[0]==name:
        print(row)
f.close()

#### output in dictionary form

with open('c:\\22bca222\\python\\SQLITE3\\contact.csv', 'r',newline='') as f:
    c_reader=csv.DictReader(f)
    for row in c_reader:
        print(row)
    







