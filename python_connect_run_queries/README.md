README.txt

The files contained in this model are:
- _config.json_, which contains the login credentials for Snowflake connection as well as the location of the sql statements "sql_queries".
- _sql_queries_, which holds the queries to be ran in Snowflake
- _run_queries.py_, which is the main python script that calls to the other files to connect to Snowflake and run the queries. 

In order to use these files, don't forget to:
- Fill your credentials and the location of the file in the _config.json_ file.
- Modify the location of _config.json_ in _run_queries.py