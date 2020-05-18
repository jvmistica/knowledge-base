# Knowledge Base
A knowledge base web application created using Flask.

## Getting Started

Install the required modules:
```
pip install -r requirements.txt
```  

Setup the database:
1. Create an SQL instance by logging into Google Cloud Platform and navigating to Storage > SQL.
2. Click "Create Instance" > "Choose MySQL" and fill up the details for the instance.
3. Create a database by clicking "Databases" > "Create database" under your SQL instance.
4. Fill up the details and click "Create"
5. Change the details in the modules/config.py file:
```
DB_USER="db_user"
DB_PASS="db_pass"
DB_NAME="db_name"
CLOUD_SQL_CONNECTION_NAME="sql_conn_name"
```  

Deploy to Google App Engine:
```
gcloud app deploy
```
