__author__ = "Gio Cadiz"

# Import the modules
import sqlite3


conn = sqlite3.connect('sales_db.sqlite')
c = conn.cursor()

#Crear tabla
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS empleado (sale_id INTEGER, customerName TEXT, SaleValue INTEGER,saleDate TEXT)')

#Insertar data
def insert_data():	
	c.execute("INSERT INTO empleado VALUES (1,'Smith', 1200,'2008-07-14')")
	c.execute("INSERT INTO empleado VALUES (2,'Johnson', 1400,'2008-08-17')")
	c.execute("INSERT INTO empleado VALUES (3,'Williams', 600,'2008-08-26')")
	c.execute("INSERT INTO empleado VALUES (4,'Jones', 950,'2008-09-10')")
	c.execute("INSERT INTO empleado VALUES (5,'Brown', 350,'2008-10-15')")
	c.execute("INSERT INTO empleado VALUES (6,'David', 1550,'2008-10-27')")
	c.execute("INSERT INTO empleado VALUES (7,'Miller', 1200,'2008-11-07')")
	c.execute("INSERT INTO empleado VALUES (8,'Wilson', 750,'2008-11-29')")
	c.execute("INSERT INTO empleado VALUES (9,'Moore', 450,'2008-12-15')")
	c.execute("INSERT INTO empleado VALUES (10,'Taylor', 700,'2009-01-05')")

	conn.commit()
	c.close()
	conn.close()

# Seleccionar datos	
def selectAllTable(): 	
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()]

# Selecionar por monto salario	
def selectSaleValue():
	c.execute('SELECT * FROM empleado WHERE SaleValue < 600 ORDER BY SaleValue')
	[print(row) for row in c.fetchall()]

# Actualiza data
def updateData():
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()] #show data
	
	print('='*40)
	
	c.execute('UPDATE empleado SET SaleValue=2000 WHERE sale_id = 1 ')
	conn.commit()
	c.close()
	conn.close()
	
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()]
	
# Elimina fila
def deleteData():
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()] #show data
	
	print('='*40)
	
	c.execute('DELETE FROM empleado WHERE sale_id = 10 ')
	conn.commit()
	c.close()
	conn.close()
	
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()]	
	
# Menu
def menu():
	while True:
		print("""
			[1]-create_table
			[2]-insert_data
			[3]-selectAllTable
			[4]-selectSaleValue
			[5]-updateData
			[6]-deleteData
			[7]-exit
			""")
		op = int(input(' Enter Option - '))
		if op == 1:
			create_table()
		elif op == 2:
			insert_data()
		elif op == 3:
			selectAllTable()
		elif op == 4:
			selectSaleValue()
		elif op == 5:
			updateData()
		elif op == 6:
			deleteData()
		elif op == 7:
			break
		else:
			print("error option")

# Main			
if __name__ == '__main__':			
	menu()	
	
