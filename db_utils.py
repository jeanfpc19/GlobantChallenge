# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:04:44 2023

@author: jeanfran.pinerua
"""
import sqlite3

def create_table(table_name):
    conn = sqlite3.connect('GlobantHR.db')
    c = conn.cursor()
    
    if table_name == 'departments':
        c.execute('''
            CREATE TABLE IF NOT EXISTS departments
            (id INTEGER,
            department TEXT)
        ''')
    elif table_name == 'jobs':
        c.execute('''
            CREATE TABLE IF NOT EXISTS jobs
            (id INTEGER,
            job TEXT)
        ''')
    elif table_name == 'hired_employees':
        c.execute('''
            CREATE TABLE IF NOT EXISTS hired_employees
            (id INTEGER,
            name TEXT,
            datetime TEXT,
            department_id INTEGER,
            job_id INTEGER)
        ''')
    else:
        print(f'Invalid table name: {table_name}')
    
    conn.commit()
    conn.close()
