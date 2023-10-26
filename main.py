# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:23:28 2023

@author: jeanfran.pinerua
"""

from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/upload/<table_name>', methods=['POST'])
def upload_file(table_name):
    uploaded_file = request.files['file']
    
    if uploaded_file:
        return jsonify({'message': f'Data uploaded to {table_name} successfully'})
    else:
        return jsonify({'error': 'No file provided in the request'}), 400 
        

if __name__ == '__main__':
    app.run()