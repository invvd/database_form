import re

#Register/Login

usr_response = str(input("Welcome!, if you already have an account press L to login, else you can register with R key: "))

#Register
if usr_response == "R" or usr_response == "r":

    #Form register

    reg_usr = str(input("\nUsername: "))

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
        print("\nNombre de usuario válido.")
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
        print("\nRegistro exitoso")
    
#Login

elif usr_response == "L" or usr_response == "l":

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

    if str(log_auth) == "['{}', '{}']".format(log_usr, log_pwd):
        print("\nAcceso concedido, estamos más cerca.")