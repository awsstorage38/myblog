import sqlite3

connection = sqlite3.connect('C:\\Users\\Akshith\\Desktop\\myblog\\Database\\myblog.db')
cursor = connection.cursor()

# Test query
#cursor.execute('SELECT * FROM login WHERE username=? AND password=?", (ganesh, password123)')
cursor.execute("SELECT * FROM login WHERE username=? AND password=?", ('ganesh', 'password123'))
user = cursor.fetchone()
#rows = cursor.fetchone()
print(user)

connection.close()
