#Operations with database:

def create_new_configuration():
    f = open("lib/appconfig.ini", 'w')
    f.writelines('#This is your password database file, dont share this file to anyone for you security\n')
    f.writelines("[DEFAULT]\n")
    f.writelines("DatabasePath = lib/passdatabase.db\n")
    f.writelines("Encode = full\n")
    f.writelines("RequireLogin = yes")
    f.close()

def create_new_database(databasepath):
    f = open(databasepath, 'w')
    f.writelines('#This is your password database file, dont share this file to anyone for you security\n')
    f.close()

