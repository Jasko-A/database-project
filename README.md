# data

## How to access our database through Azure:

1. Install the drivers for SQL Server and Azure.  ([Windows](https://sqlchoice.azurewebsites.net/en-us/sql-server/developer-get-started/python/windows/)/[Linux](https://www.microsoft.com/en-us/sql-server/developer-get-started/python/ubuntu/)/[Mac](https://sqlchoice.azurewebsites.net/en-us/sql-server/developer-get-started/python/mac/))

2. Get a username, password, and server address from db team.

3. Run a sample program. [(Linux)](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python)

```python
import pyodbc

server = 'ecs171jokedb.database.windows.net'
database = 'jokedb'
username = 'fake_account23'
password = 'fake_password23'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute('select joke_rater_id, rating from JokeRating where joke_id=506')
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()
```

## How to run the website locally

Requirements (pip2.7): django1.8.7, django-countries, netifaces, iso3166
Other requirements: sqlite3, copy of the db

1. Clone the repo to your local machine.

2. Get a .sql dump of the database from the db team, put it into the same repo.

3. Create a database using the sql dump.

```
sqlite3 db.sqlite3
> .read dump.sql
```

4. Run the django development server (python manage.py runserver)

5. Navigate to http://127.0.0.1:8000.
