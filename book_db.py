    # from flask import Flask
import sqlite3
from datetime import datetime
DB_NAME = 'bookshelf.db'

def create_table():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    #make table name of content
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT
        )
    ''')
    connect.commit()
    connect.close()


def add_book(name):
    #connect to database and table
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    now_time = datetime.now().strftime("%Y/%m/%d %H:%M")
    cursor.execute('INSERT INTO Book (name, date) VALUES (?, ?)', (name, now_time))
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
