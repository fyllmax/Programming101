import requests
import sqlite3
from Client import Client
import hashlib
from time import time
import os
# from random import randint

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def hash_password(password):
    hash_password = hashlib.sha1()
    hash_password.update(password.encode("utf-8"))
    return hash_password.hexdigest()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                hash_password TEXT,
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                login_time INT DEFAULT 1,
                new_pass_code TEXT)'''

    cursor.execute(create_query)


def check_user_exist(username):
    check_for_user_sql = 'SELECT username FROM clients WHERE username = ?'
    is_there_user = cursor.execute(check_for_user_sql, (username, )).fetchone()[0]
    return is_there_user


def check_user_email(username):
    check_user_email_sql = 'SELECT email FROM clients WHERE username = ?'
    is_there_email = cursor.execute(check_user_email_sql, (username, )).fetchone()[0]
    return is_there_email


def create_random_hash(username):
    random_hash = os.urandom(16)
    insert_random_hash = "UPDATE clients SET new_pass_code = ? WHERE username = ?"
    cursor.execute(insert_random_hash, (random_hash))
    conn.commit()


def get_pass_code_hash(username):
    get_hash = cursor.execute('SELECT new_pass_code FROM clients WHERE username = ?', (username, )).fetchone()[0]
    return get_hash


def insert_login_time(username):
    login_time = int(time())
    login_time_sql = "UPDATE clients SET login_time = ? WHERE username = ?"
    cursor.execute(login_time_sql, (login_time, username))
    conn.commit()


def insert_login_time_of_register(username):
    login_time = int(time()) - 300
    login_time_sql = "UPDATE clients SET login_time = ? WHERE username = ?"
    cursor.execute(login_time_sql, (login_time, username))
    conn.commit()


def get_login_time(username):
    get_login_time = cursor.execute('SELECT login_time FROM clients WHERE username = ?', (username, )).fetchone()[0]
    return get_login_time


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET hash_password = ? WHERE id = ?"
    cursor.execute(update_sql, (hash_password(new_pass), logged_user.get_id()))
    conn.commit()


def change_password(new_pass, username):
    update_sql = "UPDATE clients SET hash_password = ? WHERE username = ?"
    cursor.execute(update_sql, (hash_password(new_pass), username))
    conn.commit()


def register(username, password, email):
    insert_sql = "insert into clients (username, hash_password, email) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, hash_password(password), email))
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND hash_password = ? LIMIT 1"

    cursor.execute(select_query, (username, hash_password(password)))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
