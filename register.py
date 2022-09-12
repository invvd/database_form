import re

#Título

print("Registro\n")

#Form

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

#Database (la "w" es para sobreescribir y la "a" para anexar)

usr_database_w = open("usr_database.txt", "a")

#Verificar que las contraseñas estén correctas

if reg_pwd == reg_pwd_confirm:
    usr_database_w.write("{} | {}\n".format(reg_usr, reg_pwd, end=""))
    usr_database_w.write("")
    usr_database_w.close()

elif reg_pwd != reg_pwd_confirm:
    print("\nLas contraseñas no coinciden")
    exit()

#Login exitoso
print("Registro completado.")

