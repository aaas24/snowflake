import snowflake.connector
import json
import os


def run_sql_script(connection, script):
  """
  this function takes a snowflake connection and executes a series of SQL commands 
  in a script (also provided).

  :param connection: an instance of a snowflake connection.
  :param script: a path to a SQL script to execute.
  :returns: message from database
  :rtype: string
  """
  with open(script, "r") as file:
    for cur in connection.execute_stream(file):
      for ret in cur:
        print(ret)


# 
# main procedure
# 

def main():

  #defined variables (change based on environment). Ex: /Users/aalvarez/Desktop/Analytics/
  CONFIG_LOCATION='<complete me>'

  # load config
  CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())

  # extract snowhouse secrets from config
  SF_ACCOUNT    = CONFIG['secrets']['account']
  SF_USER       = CONFIG['secrets']['user']
  SF_WAREHOUSE  = CONFIG['secrets']['warehouse']
  SF_ROLE       = CONFIG['secrets']['role']
  SF_DATABASE   = CONFIG['secrets']['database']
  SF_SCHEMA     = CONFIG['secrets']['schema']
  SF_PASSWORD   = CONFIG['secrets']['password']

  # extract SQL script from config
  SCRIPT  = CONFIG['load_script']

  # fire up an instance of a snowflake connection
  connection = snowflake.connector.connect (
      account  = SF_ACCOUNT,
      role     = SF_ROLE,
      user     = SF_USER,
      password = SF_PASSWORD,
      database = SF_DATABASE,
      schema   = SF_SCHEMA
  )

  try:

    # run SQL script
    run_sql_script(connection, SCRIPT)

  except Exception as e:

    raise e





# 
# run it!
# 

if __name__ == '__main__':
  main()