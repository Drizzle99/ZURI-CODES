from datetime import datetime 
import random

db = { }
acc_num = random.int(0,9)
name = input('What is your name? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

def create(account_num, email, password):
	 user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
if name in allowedUsers:
    password = input('Your password? \n')
    userId = allowedUsers.index(name)
    dateTime = datetime.now()

    if password == allowedPassword[userId]:
    	
        print(dateTime)
        print('Welcome %s' % name)
        print('these are the available options:')
        print('1. Withdrawal')
        print('2. cash deposit')
        print('3. complaint')

        selectedOption = int(input('Please select an option:  '))
    

        if selectedOption == 1:
            print('you selected %s' % selectedOption)
            int(input('How much would you like to withdraw \n'))
            print('Take your cash ')
            
        
        elif selectedOption == 2:
            print('you selected %s' % selectedOption)
            depo=  int(input('How much would you like to deposit \n'))
            print('Your current balance is  %s' % depo)
             

        elif selectedOption == 3:
            print('you selected %s' % selectedOption)
            input('What issue would you like to report \n ')
            print('Thank You for contacting us. ')
            
        else:
            print('invalid option selected, try again')


    else:
        print('Password incorrect, please try again')
else:
    print('Name not found, please try again')