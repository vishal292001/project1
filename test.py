from pymongo import MongoClient
client = MongoClient("mongodb://database:27017")
print("Connection Successful")

mylist= [
   { "_id":1, 'Title':'Employee Skills Dashboard' , 'Likes':1},
   { "_id":2, 'Title':'Dockerizing a simple data pipeline' , 'Likes':1},
   { "_id":3, 'Title':'Introduction to Great Expectations' , 'Likes':1},
   { "_id":4, 'Title':'Dashboards using Python Plotly - Part 2' , 'Likes':0},
   { "_id":5, 'Title':'Informatica Repository Objects Migration' , 'Likes':0},
   { "_id":6, 'Title':'Connect_PowerBI_with_MongoDB' , 'Likes':0},
   { "_id":7, 'Title':'Query Federation using Presto' , 'Likes':1},
   { "_id":8, 'Title':'Streaming databases' , 'Likes':1},
   { "_id":9, 'Title':'Snowflake Data Cloud' , 'Likes':0},
   { "_id":10, 'Title':'Data Engineering Using DBT' , 'Likes':0},
   { "_id":11, 'Title':'MongoDB' , 'Likes':2},
   { "_id":12, 'Title':'Job Scheduling using Airflow' , 'Likes':1},
   { "_id":13, 'Title':'Introduction to Pandas Profiling' , 'Likes':1},
   { "_id":14, 'Title':'Automate with PyTest' , 'Likes':1},
   { "_id":15, 'Title':'Star Schema Demo Pipeline informatica' , 'Likes':1},
   { "_id":16, 'Title':'Data Modelling in Power BI' , 'Likes':2},
   { "_id":17, 'Title':'How to run DBT tests' , 'Likes':1},
   { "_id":18, 'Title':'customized Job Scheduling in Airflow' , 'Likes':0},
   { "_id":19, 'Title':'Pipelines using Ploomber' , 'Likes':0},
   { "_id":20, 'Title':'StreamSets' , 'Likes':0},
   { "_id":21, 'Title':'Apache Kafka' , 'Likes':0},
   { "_id":22, 'Title':'Dashboards using Python Plotly' , 'Likes':0},
   
]


db = client["example"]
col = db["Videos"]

x = col.insert_many(mylist)
print(x.inserted_ids)


