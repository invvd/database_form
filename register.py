from loginuser import loginUsr
from registeruser import registerUsr
#Register/Login

usr_response = str(input("Welcome!, if you already have an account press L to login, else you can register with R key: "))

#Register
if usr_response == "R" or usr_response == "r":
    registerUsr()
#Login

elif usr_response == "L" or usr_response == "l":
    loginUsr()
