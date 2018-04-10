README.txt

The files contained in this model are:
- config.json, which contains the login credentials for Snowflake connection as well as the location of the sql statements "sql_queries".
- sql_queries, which holds the queries to be ran in Snowflake
- run_queries.py, which is the main python script that calls to the other files to connect to Snowflake and run the queries. 

In order to us this files you must:
- Fill your credentials and the location of the file in the config.json file.
- Modify location of config.json in run_queries.py