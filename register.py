import re

#Register/Login

usr_response = str(input("Welcome!, if you already have an account press L to login, else you can register with R key: "))

#Register
if usr_response == "R" or usr_response == "r":

    #Form register

    reg_usr = str(input("Username: "))

    #No repetir usernames

    usr_database_r = open("usr_database.txt", "r")
    read_usr_database = usr_database_r.read()
    usr_database_r.close()
    repeated_usr = re.findall("{}".format(reg_usr), read_usr_database)

    #print(repeated_usr)
    if len(repeated_usr) > 0:
        print("\nEl nombre de usuario ya está en uso.")
        exit()

    elif len(repeated_usr) == 0:
        print("\nNombre de usuario válido.\n")
        reg_pwd = str(input("\nPassword: "))
        reg_pwd_confirm = str(input("\nConfirm Password: "))

    #Agregar o anexar datos a la base en caso de que las contrasenas coincidan

    usr_database_w = open("usr_database.txt", "a")

    if reg_pwd == reg_pwd_confirm:
        usr_database_w.write("{} | {}\n".format(reg_usr, reg_pwd))
        usr_database_w.write("")
        usr_database_w.close()

    elif reg_pwd != reg_pwd_confirm:
        print("Password doesn't match")

#Login

elif usr_response == "L" or usr_response == "l":

    log_usr = str(input("Username: "))
    #No repetir usernames

    usr_database_r = open("usr_database.txt", "r")
    read_usr_database = usr_database_r.read()
    usr_database_r.close()
    repeated_usr = re.findall("{}".format(log_usr), read_usr_database)

    #print(repeated_usr)
    if repeated_usr == log_usr:
        log_pwd = str(input("\nPassword: "))
