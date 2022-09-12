import re

def loginUsr():
    
    log_usr = str(input("\nUsername: "))

    #No repetir usernames

    usr_database_r = open("usr_database.txt", "r")
    read_usr_database = usr_database_r.read()
    usr_database_r.close()
    repeated_usr = re.findall("{}".format(log_usr), read_usr_database)

    #print(repeated_usr)
    #print(log_usr)
    #print("['{}']".format(log_usr))

    #Log Auth

    if str(repeated_usr) == str("['{}']".format(log_usr)):
        log_pwd = str(input("\nPassword: "))

        usr_database_r = open("usr_database.txt", "r")
        read_usr_database = usr_database_r.read()
        usr_database_r.close()
        log_auth = re.findall(str(log_usr) + "|" + str(log_pwd), read_usr_database)

    elif str(repeated_usr) != str("['{}']".format(log_usr)):
        print("\nEl nombre de usuario no existe, registrate primero.")
        exit()

    if str(log_auth) == "['{}' | '{}']".format(log_usr, log_pwd):
        print("\nAcceso concedido, estamos más cerca.")
    
    elif str(log_auth) != "['{}' | '{}']".format(log_usr, log_pwd):
        print("\nAcceso denegado.")
        exit()