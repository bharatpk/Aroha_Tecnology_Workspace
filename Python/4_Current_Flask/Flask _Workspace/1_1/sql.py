import sqlite3
with sqlite3.connect("sample_example.db") as connection:
	c = connection.cursor()
	c.execute("DROP TABLE mytable1")
	c.execute('CREATE TABLE mytable1(title TEXT, description TEXT)')
	c.execute('INSERT INTO mytable1 VALUES("1","Bharat")')
	c.execute('INSERT INTO mytable1 VALUES("2","xyz")')

	#c.commit()
