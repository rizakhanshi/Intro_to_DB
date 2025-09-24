#!/usr/bin/python3
"""
Script to create a MySQL database 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (adjust user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            # connection was never created
            pass

if __name__ == "__main__":
    create_database()
