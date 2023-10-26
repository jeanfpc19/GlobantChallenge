# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:00:52 2023

@author: jeanfran.pinerua
"""

import requests
import pandas as pd

url = 'http://127.0.0.1:5000'

def test_upload():
    table_names = ['jobs', 'departments', 'hired_employees']
    for table_name in table_names:
        file_path = f'files/{table_name}.csv'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(f'{url}/upload/{table_name}', files=files)
        assert response.status_code == 200

def test_metrics():
    metrics = ['quarterly_hired_employees', 'high_hires_departments']
    for metric in metrics:
        response = requests.get(f'{url}/metrics/{metric}')
        assert response.status_code == 200

        data = response.json()
        df = pd.DataFrame(data)
        assert not df.empty
