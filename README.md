SQLite-Python-3
===============
Gio Cádiz
* Twitter : [@Gio_Cadiz](https://twitter.com/Gio_Cadiz)
## Description
Script básico en Python 3 para realizar [CRUD](https://es.wikipedia.org/wiki/CRUD) a la [base de datos](https://es.wikipedia.org/wiki/Base_de_datos) SQLite.

## Requirements
Este script requiere lo siguiente:
* Python version 3.6.2 [Download Python](https://www.python.org/downloads/).
* SQLite [official Web](https://www.sqlite.org/index.html).
* Documentation [Python3 - SQLite3](https://docs.python.org/3.6/library/sqlite3.html).

##
Para usar el módulo, primero debe crear un objeto de conexión que representa la base de datos. 
Aquí se almacenan los datos en el archivo sales_db.sqlite:
```python
import sqlite3

conn = sqlite3.connect('sales_db.sqlite')
```
Una vez creada la conexión, puede crear un objeto Cursor (**c** ): 
```python
c = conn.cursor()
```
y llamar a su método **execute()** para ejecutar comandos SQL:
## CRUD

#### CREATE
```python
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS empleado (sale_id INTEGER, customerName TEXT, SaleValue INTEGER,saleDate TEXT)')
```
#### INSERT
```python
def insert_data():	
	c.execute("INSERT INTO empleado VALUES (1,'Smith', 1200,'2008-07-14')")
  
	conn.commit()
```  
#### READ
```python
def selectAllTable(): 	
	c.execute('SELECT * FROM empleado')
	[print(row) for row in c.fetchall()]
```
#### UPDATE
```python
def updateData():
	c.execute('UPDATE empleado SET SaleValue=2000 WHERE sale_id = 1 ')
	conn.commit()
```
#### DELETE
```python
def deleteData():
	c.execute('DELETE FROM empleado WHERE sale_id = 10 ')
	conn.commit()
```

