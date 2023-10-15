#Main functional:

class switch(object):
     def __init__(self, value):
         self.value = value  # значение, которое будем искать
         self.fall = False   # для пустых case блоков

     def __iter__(self):     # для использования в цикле for
         """ Возвращает один раз метод match и завершается """
         yield self.match
         raise StopIteration

     def match(self, *args):
         """ Указывает, нужно ли заходить в тестовый вариант """
         if self.fall or not args:
             # пустой список аргументов означает последний блок case
             # fall означает, что ранее сработало условие и нужно заходить 
             #   в каждый case до первого break
             return True
         elif self.value in args:
             self.fall = True
             return True
         return False

#Init operations:

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

#CLI Menus:
def clear():
    for i in range(10):
        print("")
def main_menu(Services):
    print ("\n---select option---")
    print ("1 - Create service")
    print ("2 - Manage service")
    print ("3 - Reveal password")
    option = int(input("\nChoosen option is: "))
    for case in switch(option):
        clear()
        if case(1): print("create"); break
        if case(2): services.show_services(Services); break
        if case(3): print("reveal"); break
        if case(): main_menu(Services)
    
#Operations with database:
class services():
    def reveal_service(Services):
        option = int(input("Выберите id сервиса, пароль которого хотите посмотреть: "))
        try:
            if option >= 0:
                for row in Services:
                    if int(option) == int(row[0]):
                        print (f"id - {row[0]}, service - {row[1]}, password - {row[2]}")
        except:
            main_menu()
    def show_services(Services):
        for row in Services:
            print (f"id - {row[0]}, service - {row[1]}")
        services.reveal_service(Services)
    def show_service(Services, id):
        for row in Services:
            if id == row[0]:
                print (f"id - {row[0]}, service - {row[1]}")