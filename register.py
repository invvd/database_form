#Título

print("Registro")

#Database (la "w" es para sobreescribir y la "a" para anexar)

usr_database = open("usr_database.txt", "a")

#Form

reg_usr = str(input("Username: "))
reg_pwd = str(input("Password: "))
reg_pwd_confirm = str(input("Confirm Password: "))

if reg_pwd == reg_pwd_confirm:
    usr_database.write("{} | {} \n".format(reg_usr, reg_pwd))
    usr_database.write("")
    usr_database.close()

elif reg_pwd != reg_pwd_confirm:
    print("Las contrasenas no coinciden")

