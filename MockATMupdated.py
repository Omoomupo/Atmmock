
#### ****** REGISTER ******
# To register for an account this are the details required: 
    # - First name, Last name, password and email
# - During registration we generate account account number for the account holder which you will use to log in to your account

#### ******  LOG IN  ******
# To Log in to your account you will need this details:
    # - Account number generated and the password you used while registering so keep both safe



#initializing the system


import random

database = {}

def init():

    valid = False
    print("**********Welcome to Omoomupo Bank**********")
    print("The bank for the future")

    while valid == False:
        
        customer = int(input("Do you have account with us \n 1(yes) 2(no) \n"))

        if(customer == 1):
            valid = True
            login()
        elif(customer == 2):
            valid = True
            print(register())
        else:
            print("You have entered an invalid option")
            init()
        
def login():
    
    print("*****Login to your account*****")
#copy the account number generated, and input it when asked to input your account number for login
    customerAccountNumber = int(input("Please input your account number. \n"))
#Make sure the account number you input here is the same as the one you registered with
    password = input("input your password/pin \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == customerAccountNumber):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    
    
    
    #login()
    
def register():
    print("******Register for an account with us.*******")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name,last_name,email,password]

    print("Your account has been created.")
    print("You are now a customer of BankPHB")
    print("This is your account number: %d \n Jot it down in your diary" % accountNumber)
    
    login()

def bankOperation(user):

    print("Welcome %s %s" % (user[0], user[1] ))
    operation = int(input("What operation would you like to perform? \n 1 (Deposit) \n 2 (Withdraw) \n 3 (Check balance) \n 4 (complaint) \n 5 (Account information \n 6 (Logout) \n"  ))

    if(operation == 1):
        deposit()

    elif(operation == 2):
        withdraw()
        
    elif(operation == 3):
        balance()

    elif(operation == 4):
        complaint()

    elif(operation == 5):
        print("""This are your account details
            %s %s %s
    """ % (user[0],user[1],user[2] ) )
        
    elif(operation == 6):
        logout()
        
    pass
    
def deposit():
    input("How much do you want to deposit \n ")
    print("*****Thanks for banking with us.*****")

def withdraw():
    input("How much do you want to withdraw \n ")
    print("*****Thanks for banking with us.*****")

def balance():
    print("Your account balance is \n ")
    print("*****Thanks for banking with us.*****")
    
def complaint():
    input("What is your complaint \n  ")
    print("*****Thanks for banking with us.*****")
    
    
def logout():
    login()
    
def generateAccountNumber():
    
    return random.randrange(1111111111,9999999999)

def money():
    return random.randrange(111111,999999)

##### ACTUAL BANKING SYSTEM ####
#print(generateAccountNumber())
#print(money())
init()












