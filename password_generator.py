import string
import random

more_password = 'yes'


def password_generator():
    global more_password
    while True:

        if more_password == 'yes':
            password_len = int(
                input("How many letters would you like in your password?\n"))
            chars = string.ascii_letters + string.digits + '!#$%&*' + '1234567890'
            passSend = ''.join(random.choice(chars)
                               for i in range(password_len))
            print(
                f"Your new, awesome and hard to hack password is: {passSend}")
            more_password = input(
                'Do you want to get another password? Type "yes" or "no."\n')
            continue
        elif more_password == 'no':
            print("Thank you for taking your time and using my password generator!")
            break


print("Welcome to the Little Password Generator!")
password_generator()
