import re
from registeruser import registerusr

def loginusr():
    
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
        print("\nUsername doesn't exists, please sign in")
        return registerusr()

    if str(log_auth) == "['{}' | '{}']".format(log_usr, log_pwd):
        print("\nWelcome back, " + log_usr + "!")
    
    elif str(log_auth) != "['{}' | '{}']".format(log_usr, log_pwd):
        print("\nAccess denied.")
        exit()