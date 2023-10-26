# Globant Data Engineering API

This API provides endpoints to migrate historical HR data, including uploading CSV files, querying metrics.

## Features

- **File Upload**: Upload CSV files for 'departments', 'jobs', and 'hired employees' data.

- **Metrics**: Retrieve HR metrics like quarterly hired employees and high hires departments.

## Usage
## Setup Using Docker:

- Navigate to the root directory.

- Build and run the Docker Image:

   docker --build -t flask-app
   
   docker run -p 5000:5000 flask-app
## Manual Setup:
 - Navigate to the root directory
 - Install all the libraries in the requirements.txt
 - Navigate to /app/ directory
 - Run app.py

## Using the API
- **Uploading CSV Files**
- The API is programmed to receive 3 types of files and insert them into a database
        1. jobs.csv -> jobs table
        2. departments.csv -> departments table
        3. hired_employees -> hired_employees table
  *Example*
- Use a tool like Postman to make POST requests to http://127.0.0.1:5000/upload/jobs. Attaching the jobs.csv file with the request.
- Or using the python request library you could upload files like this:
  
        file_path = 'files/jobs.csv'
        files = {'file': open(file_path, 'rb')}
        response = requests.post('[{url}](http://127.0.0.1:5000)/upload/jobs', files=files)
        print(response)

**Querying Metrics**
 The API is programmed to provide 2 types of metrics
        1. quarterly_hired_employees
        2. high_hires_departments
        
 *Example*
- Use a tool like Postman to make GET requests to http://127.0.0.1:5000/metrics/high_hires_departments
- Or using the python request and pandas library you could get the metrics like this:
  
      url = 'http://127.0.0.1:5000/metrics/high_hires_departments'
      response = requests.get(url)
      df = pd.DataFrame(response.json())
      print(df)
