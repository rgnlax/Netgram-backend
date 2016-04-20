import MySQLdb

db = MySQLdb.connect(host="db",user="root",passwd="admin",port=3306)
cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS djangodb')
cursor.execute("GRANT ALL PRIVILEGES ON djangodb.* TO 'djangouser'@'%' IDENTIFIED BY 'secret';")