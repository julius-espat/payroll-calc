from database import *
from ui import *
import os
import json
global DB_PATH

def config_check():
    if os.path.exists('config.json'):
        with open("config.json", "r") as config:
            path = json.load(config)
            return path["db_path"]
    else:
        with open("config.json", "w") as config:
            path = database_select()
            data_path = {"db_path":path}
            config.write(json.dumps(data_path))
            return path
        

        

    
    


if __name__ == "__main__":
    DB_PATH = config_check()
    connected = False
    while connected == False:
        try:
            sql_connection(DB_PATH)
            connected = True
        except:
            simple_error("Database not found, select or create database")
            os.remove("config.json")
            DB_PATH = config_check()
            continue
    main()
        
