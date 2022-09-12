from loginuser import loginusr
from registeruser import registerusr
#Register/Login

usr_response = str(input("Welcome!, if you already have an account press L to login, else you can register with R key: "))
def main():
    #Register
    if usr_response == "R" or usr_response == "r":
        registerusr()

    #Login
    elif usr_response == "L" or usr_response == "l":
        loginusr()
    
    else:
        print("Invalid key.")
        exit()
main()