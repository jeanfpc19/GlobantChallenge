# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:04:44 2023

@author: jeanfran.pinerua
"""
import sqlite3
dbName = 'GlobantHR.db'

def create_table(table_name):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    
    if table_name == 'departments':
        c.execute('''
            CREATE TABLE IF NOT EXISTS departments
            (id INTEGER,
            department TEXT,
            upload_timestamp DATETIME)
        ''')
    elif table_name == 'jobs':
        c.execute('''
            CREATE TABLE IF NOT EXISTS jobs
            (id INTEGER,
            job TEXT, 
            upload_timestamp DATETIME)
        ''')
    elif table_name == 'hired_employees':
        c.execute('''
            CREATE TABLE IF NOT EXISTS hired_employees
            (id INTEGER,
            name TEXT,
            datetime TEXT,
            department_id INTEGER,
            job_id INTEGER,
            upload_timestamp DATETIME)
        ''')
    
    conn.commit()
    conn.close()
    
def insert_df_into_table(table_name,df):
        conn = sqlite3.connect(dbName)
        
        df.to_sql(table_name, conn, if_exists='append', index=False)
        
        conn.commit()
        conn.close()
