# Sqlalchemy-Challenge
### Jupyter Notebook Database, Data Analysis, API SQLite in SQLAlchemy 

# Jupyter Notebook Database
First of all I use SQLAlchemy's functions to connect to Sqlite database and reflects into classes. 
After i used Link Python to the database by creating a SQLAlchemy session.
# Data Analysis
I use SQLAlchemy ORM queries, Pandas, and Matplotlib for data analysis. First i analyze Precipitation. 
I analyze the recent data, create a query from last year of data and create dataframe to show on plot.

![image](https://github.com/gulcan7414/sqlalchemy-challenge/assets/123443605/0cbb423c-d30d-4664-ae8b-23f40cf925b4)

Secondly I analyze Stations.I analyze the recent data, create a query from last year of data and create dataframe to show on histogram.

![image](https://github.com/gulcan7414/sqlalchemy-challenge/assets/123443605/7f6b38bd-5dba-40b4-8ffc-3fdc38079676)

# API SQLite
I design a Flask API based on the queries that I just developed. 

I list all available routes ,specifically list of precipitation, stations, temperature and the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

<img width="296" alt="Screen Shot 2023-05-25 at 1 02 53 pm" src="https://github.com/gulcan7414/sqlalchemy-challenge/assets/123443605/a7fc895f-4137-4859-bd2c-9269cbf21af6">

