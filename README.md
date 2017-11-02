# data

## How to access our database through Azure:

1. Install the drivers for SQL Server and Azure. 

[Windows](https://sqlchoice.azurewebsites.net/en-us/sql-server/developer-get-started/python/windows/)

[Linux](https://www.microsoft.com/en-us/sql-server/developer-get-started/python/ubuntu/)

[Mac](https://sqlchoice.azurewebsites.net/en-us/sql-server/developer-get-started/python/mac/)

2. Get a username, password, and server address from db team.

3. [Sample program (Linux):](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connect-query-python)

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
