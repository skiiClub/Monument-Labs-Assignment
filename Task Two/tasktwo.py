#To run this code the mySQL driver must be installed 

import mysql
import json
import requests

#user_data holds all the json data to send as a POST request to API
user_data = []

#replace this with the information for actual sql database 
conn = mysql.connector.connect(host='localhost',
                             database='Monument_db',
                             user='username',
                             password='password')


sql_select_Query = "select * from users"
cursor = mySQLconnection .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

#The actual user object takes much more inputs
#Full list can be found on https://developers.intercom.com/intercom-api-reference/v0/reference#users

    for row in records:
        data = {
                "type": "user",
                'id':row[0],
                'name':row[1],
                'email':row[2]
                }

        user_data.append(data)

    cursor.close()

#Looping through json data objects and sending them to the api 
for data in user_data:
    data_json = json.dumps(data)
    payload = {'json_payload': data_json, 'apikey': 'INSERT_API_KEY_HERE'}
    r = requests.get('https://api.intercom.io/users', data=payload)
