import sqlite3

def insertInto():
    db = sqlite3.connect('employee.db')
    db.execute('create table employee (name varchar(5), id int not null)')
    db.execute('insert into employee (name, id) values("Aditya", 45)')
    db.commit()


def showDatabase():
    db = sqlite3.connect("employee.db")
    db.row_factory = sqlite3.Row
    cursor = db.execute('select * from employee')
    for row in cursor:
        fileContainer = open('employee.txt', 'w')
        dictRow = dict(row)
        fileContainer.write(str(dictRow))
        print(dictRow)
        

showDatabase()