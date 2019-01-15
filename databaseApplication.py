
import sqlite3
import time
class Database:
    #Constructor would create database using object that has established connection between program and db
    def __init__(self, columnName1, columnName2, db):
        self.name = columnName1
        self.id = columnName2
        db.execute('drop table if exists employee')
        db.execute('create table employee({col1} varchar(5), {col2} int not null)'.format(col1 = self.name, col2 = self.id))
        db.commit()

    #Inserting into table once it's been created
    def insertion(self, db, row):
       db.execute('insert into employee ({col1}, {col2}) values(?, ?)'.format(col1 = self.name, col2 = self.id), (row['ename'], row['eid']))
       db.commit()
       print('Inserted Successfully.')

    #Retrieving any row using primary key
    def retrive(self, pkey, db):
        cursor = db.execute('select * from employee where {primary} = {val}'.format(primary = self.id, val = pkey))
        for row in cursor:
            if ( row.keys()): 
                print(row['ename'])
            else:
                print("Nothing's is available to print.")
                break
    
    #Updating table using primary key
    def updation(self, pkey, db): 
        db.execute("update employee SET  ename = ? where eid = ?", ('Aditya Tiwari', pkey))
        db.commit()
    
    #Deleting any row using primary key
    def deletion(self, pkey, db):
        db.execute('delete from  employee where eid = ?',(pkey,))
        db.commit()
        print('Deleted Succesfully.')



def main():
    
    db = sqlite3.connect('employee.db')
    dbclass = Database('ename', 'eid', db)
    db.row_factory = sqlite3.Row
    dbclass.insertion(db, dict(ename = 'aditya', eid = int(45)))
    time.sleep(2)
    dbclass.updation(45, db)
    time.sleep(2)
    dbclass.retrive(45, db)
    dbclass.deletion(45, db)
    time.sleep(2)
    dbclass.retrive(45, db)
    time.sleep(2)

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