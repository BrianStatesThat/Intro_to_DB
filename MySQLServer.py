#!/usr/bin/env python3
"""
MySQLServer.py - Script to create the alx_book_store database
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username if different
            password=''   # Replace with your MySQL password if needed
        )
        
        # Create database if it doesn't exist
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        # Close the cursor if it exists
        if cursor is not None:
            cursor.close()
        
        # Close the connection if it exists and is connected
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()