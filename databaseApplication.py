
import sqlite3

class Database:
    def __init__(self, columnName1, columnName2, db):
        self.name = columnName1
        self.id = columnName2
        db.execute('drop table if exists employee')
        db.execute('create table employee({col1} varchar(5), {col2} int not null)'.format(col1 = self.name, col2 = self.id))
        db.commit()

    def insertion(self, db, row):
       db.execute('insert into employee ({col1}, {col2}) values(?, ?)'.format(col1 = self.name, col2 = self.id), (row['ename'], row['eid']))
       db.commit()
       print('Inserted Successfully.')

    def retrive(self, pkey, db):
        cursor = db.execute('select * from employee where {primary} = {val}'.format(primary = self.id, val = pkey))
        for row in cursor:
            print(row['ename'])
    def updation(self): 
        pass
    def deletion(self):
        pass



def main():
    
    db = sqlite3.connect('employee.db')
    dbclass = Database('ename', 'eid', db)
    db.row_factory = sqlite3.Row
    dbclass.insertion(db, dict(ename = 'aditya', eid = int(45)))
    dbclass.retrive(45, db)

main()


'''
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
        

insertInto()
'''