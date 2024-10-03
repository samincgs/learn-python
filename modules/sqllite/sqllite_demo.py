import sqlite3
from employee import Employee

# Sqlite is used for database functionality 
# use to spin up a database but dont want a full on mySQL or PostgresSQL database
# it is lightweight and medium sized and database lives on a disk
# use for testing and prototyping before porting it to a bigger database if needed

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp.first, 'last': emp.last, 'pay': emp.pay})
        
def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()
conn = sqlite3.connect('employee.db')
# conn = sqlite3.connect(':memory:') runs in memory and starts completely fresh each time
c = conn.cursor()
emp_1 = Employee('John', 'Doe', '50000')
emp_2 = Employee('Jane', 'Mills', '35000')
emp_3 = Employee('Josh', 'Cane', '75000')
# c.execute('''
#           CREATE TABLE employees (
#               first text,
#               last text,
#               pay integer
#           )
#           ''')
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# insert_emp(emp_3)
print(get_emp_by_name('Cane'))
# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Smith'})
# print(c.fetchall())
# conn.commit()
conn.close()