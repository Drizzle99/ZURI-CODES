import random

database = {}


def init():
    print('Welcome to My banking ATM')

    haveAccount = int(input('Do you have account with us:\n 1 (Yes) 2(No): '))

    if haveAccount == 1:

        login()
    elif haveAccount == 2:

        register()

    else:
        print('You have selected invalid option')
        init()


def login():
    print('Kindly login below')

    accountNumberFromUser = int(input('Input your account number below \n'))
    password = input('What is your password? \n')

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)

    print('Invalid account or password')
    login()


def register():
    print('Kindly Register below\n')

    email = input('what is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Input a password you will like to use \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, 0]

    print('Your Account has successfully been created')
    print(f'Your account Number is  {accountNumber}')

    login()

def bankOperation(user):
    print(f'Welcome {(user[0], user[1])}')

    selectedOption = int(input('Kindly select your transaction Option below\n (1) deposit (2) withdrawal (3) logout (4) Quit)'))

    if selectedOption == 1:
        depositOperation()

    elif selectedOption == 2:
        withdrawalOperation()

    elif selectedOption == 3:
        logout()

    elif selectedOption == 4:
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    print('Withdraw')


def depositOperation():
    print('Deposit')


def generateAccountNumber():
    return random.randrange(111111, 999999)


def logout():
    login()


init()
