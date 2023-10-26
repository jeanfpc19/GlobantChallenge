# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:04:44 2023

@author: jeanfran.pinerua
"""
import sqlite3
import numpy as np
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

        for chunk in np.array_split(df, len(df) // 1000 + 1):
            chunk.to_sql(table_name, conn, if_exists='append', index=False)
        
        conn.commit()
        conn.close()

def get_metric(metric_name):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()

    if metric_name == 'quarterly_hired_employees':
        c.execute('''
            SELECT  departments.department, 
                    jobs.job,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) as Q1,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) as Q2,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) as Q3,
                    SUM(CASE WHEN strftime('%m', datetime) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) as Q4
            FROM hired_employees
            LEFT JOIN departments ON hired_employees.department_id = departments.id
            LEFT JOIN jobs ON hired_employees.job_id = jobs.id
            WHERE strftime('%Y', datetime) = '2021'
            GROUP BY departments.department, jobs.job
            ORDER BY departments.department, jobs.job
        ''')
        
    elif metric_name == 'high_hires_departments':
        c.execute('''
            SELECT  departments.id as department_id, 
                    departments.department as department_name, 
                    COUNT(he.id) as hired
            FROM departments
            JOIN hired_employees he 
            ON (departments.id = he.department_id)
            WHERE strftime('%Y', he.datetime) = '2021'
            GROUP BY departments.id, departments.department
            HAVING COUNT(he.id) > (SELECT AVG(department_hired)
                                    FROM (
                                        SELECT COUNT(he2.id) as department_hired
                                        FROM hired_employees he2
                                        WHERE strftime('%Y', he2.datetime) = '2021'
                                        GROUP BY he2.department_id)
                                    )
            ORDER BY hired DESC;


        ''')
    else:
        return 400

    result = c.fetchall()

    conn.close()
    return result