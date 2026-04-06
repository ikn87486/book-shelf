    # from flask import Flask
import sqlite3
DB_NAME = 'bookshelf.db'

def create_table():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    #make table name of content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    connect.commit()
    connect.close()


def add_book(name):
    #connect to database and table
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute('INSERT INTO Book (name) VALUES (?)', (name,))
    connect.commit()
    connect.close()

def delete_book(book_id):
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute('DELETE FROM Book  WHERE id = ?',(book_id,))
    connect.commit()
    connect.close()

def get_book():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Book')
    rows = cursor.fetchall()
    connect.close()
    return rows
