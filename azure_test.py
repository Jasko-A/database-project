import pyodbc

server = 'ecs171jokedb.database.windows.net'
database = 'jokedb'
username = 'test'
password = 'Password3'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute('select joke_rater_id, rating from JokeRating where joke_id=506')
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()