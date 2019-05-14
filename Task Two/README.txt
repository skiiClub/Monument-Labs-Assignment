Out of the two tasks this one was more straight forward. However, to run the code the mysql driver must be installed. 

To begin the task I connected to the hypothetical mysql database. For this code to actually work, the correct credidentials must be entered on lines 11-14.
After I connect to the database, I run the query "select * from users" to gather all the data from the table. Once that is done, I loop through
each row of the data base and create a json object to be sent to the Intercom API. I place the newly created json object into a list and close the 
connection. 

After gathering the data I needed from the mysql database, I loop through my list of JSON objects and send each one to the API. Note that for this code 
to work the correct API key must be entered on line 40.
