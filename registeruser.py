import re

def registerusr():
        #Form register

        reg_usr = str(input("\nUsername: "))

        #No repetir usernames

        usr_database_r = open("usr_database.txt", "r")
        read_usr_database = usr_database_r.read()
        usr_database_r.close()
        repeated_usr = re.findall("{}".format(reg_usr), read_usr_database)

        #print(repeated_usr)
        if len(repeated_usr) > 0:
            print("\nUsername already used, please try another.")
            return registerusr()

        elif len(repeated_usr) == 0:
            print("\nUsername valid.")
            reg_pwd = str(input("\nPassword (whithout spaces): "))
            reg_pwd_confirm = str(input("\nConfirm Password: "))

        #Agregar o anexar datos a la base en caso de que las contrasenas coincidan

        usr_database_w = open("usr_database.txt", "a")

        if reg_pwd != reg_pwd_confirm:
            print("\nPassword doesn't match")

        elif reg_pwd == reg_pwd_confirm:
            usr_database_w.write("{} | {}\n".format(reg_usr, reg_pwd))
            usr_database_w.write("")
            usr_database_w.close()
            print("\nSuccessful registration!")