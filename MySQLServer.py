import mysql.connector
from sys import argv

try:
    db = mysql.connector.connect(
        host="localhost",
        user=argv[1],
        password=argv[2]
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if 'db' in locals() and db.is_connected():
        db.close()