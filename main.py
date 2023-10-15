import os
from tkinter import Tk
import operations

class internal_database:
    Services = []
    DatabasePath = ""
    Encode = ""
    RequireLogin = ""

class init_application:
    import configparser
    default_directory = ["lib/appconfig.ini"]
    def init_configuration():
        try:
            f = open("lib/appconfig.ini", 'r')
            config = init_application.configparser.ConfigParser()
            config.read('lib/appconfig.ini')
            internal_database.DatabasePath = config['DEFAULT']['DatabasePath']
            internal_database.Encode = config['DEFAULT']['Encode']
            internal_database.RequireLogin = config['DEFAULT']['RequireLogin']
            f.close()
        except: 
            operations.create_new_configuration()
            print("В корневой директории отсутствовал файл с конфигурацией, был создан новый файл.")
            init_application.init_configuration()
            
    def init_database(databasepath):
        try:
            f = open(databasepath, 'r')
            database = init_application.configparser.ConfigParser()
            database.read(databasepath)
            if len(database.sections()) > 0:
                for row in database.sections():
                    internal_database.Services.append([database[row]['id'],database[row]['service_name'],database[row]['password']])
            else:
                print ("база данных пустая")
            f.close()
        except: 
            operations.create_new_database(databasepath)
            print("В корневой директории отсутствовал файл с базой паролей, был создан новый файл.")



def main():
    print("\n\n\n\n\n\n---started---\n")
    init_application.init_configuration()
    init_application.init_database(internal_database.DatabasePath)
    print ("password database:")
    print (internal_database.Services)
    operations.main_menu(internal_database.Services)

if __name__ == "__main__":
	main()