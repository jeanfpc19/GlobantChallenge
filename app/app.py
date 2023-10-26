# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:23:28 2023

@author: jeanfran.pinerua
"""

from flask import Flask, jsonify, request
import pandas as pd
from datetime import datetime
from db_utils import create_table, insert_df_into_table, get_metric


app = Flask(__name__)

@app.route('/upload/<table_name>', methods=['POST'])
def upload_file(table_name):
    uploaded_file = request.files['file']
    
    if uploaded_file:
        column_names = {
            'departments': ['id', 'department'],
            'jobs': ['id', 'job'],
            'hired_employees': ['id', 'name', 'datetime', 'department_id', 'job_id']
        }
        
        if table_name not in column_names:
            return jsonify({'error': 'Invalid table name provided'}), 400
        
        df = pd.read_csv(uploaded_file, header=None, names=column_names[table_name])
        df.dropna(inplace=True)
        df['upload_timestamp'] = datetime.now()
        
        create_table(table_name)
        insert_df_into_table(table_name, df)
        
        return jsonify({'message': f'Data uploaded to {table_name} successfully'})
    else:
        return jsonify({'error': 'No file provided in the request'}), 400 
        
@app.route('/metrics/<metric_name>', methods=['GET'])
def get_sql_metric(metric_name):
    
    result = get_metric(metric_name)
    if result == 400:
        return jsonify({'error': 'Invalid metric name'}), result
    else: 
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)