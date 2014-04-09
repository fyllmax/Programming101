# Import
import sql_manager
import getpass
from time import time
import smtp


def check_pass(password):

    has_upper = False
    has_digit = False
    has_special = False

    for i, c in enumerate(password):
        if c.isupper():
            has_upper = True

    for i, c in enumerate(password):
        if c.isdigit():
            has_digit = True

    chars = set("!@#$%^&*()_+}{:?><~`,./;[]-=")

    if any((c in chars) for c in password):
        has_special = True

    if has_upper and has_digit and has_special:
        return True
    else:
        return False


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register, login or reset_pass")

    tries = 6

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password_pass = False
            while not password_pass:
                password = getpass.getpass()
                if len(password) >= 8 and check_pass(password):
                    password_pass = True
                    email = input('Enter your email: ')
                    sql_manager.register(username, password, email)
                    sql_manager.insert_login_time_of_register(username)
                    break

                print("Password shoud be at least 8 characters, and shound contain a capital letter, a number and a special charachter")

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")

            if username == sql_manager.check_user_exist(username):
                print('there is such user')

                time_now = int(time())
                time_between_logins = time_now - sql_manager.get_login_time(username)

                if time_between_logins > 300:
                    tries = 1

                while tries < 6:
                    password = getpass.getpass()
                    logged_user = sql_manager.login(username, password)

                    if logged_user:
                        sql_manager.insert_login_timloe_of_register(username)
                        logged_menu(logged_user)
                        break

                    else:
                        print('You have typed wrong password. Remaining tries {}'.format(5 - tries))
                        tries += 1
                        sql_manager.insert_login_time(username)

                if tries > 5:
                    print("You have reached your limit of guessing the passwordfor now, try again in few minutes.")

            else:
                print("User with such name does not exists!")

        elif command == 'reset_pass':

            username = input('Enter username: ')

            if username == sql_manager.check_user_exist(username):
                email = input('Enter email: ')

                if email == sql_manager.check_user_email(email):

                    random_hash = sql_manager.create_random_hash(username)

                    smtp.send_email(email, random_hash)

                    print('Check your email for the secret code')

                    enter_hash = input('Enter the secret code: ')

                    if enter_hash == sql_manager.get_pass_code_hash(username):
                        new_password = input('Enter new password: ')
                        sql_manager.change_password(new_password, username)
                        print('You Successfullu changed your password')
                        break

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")

        elif command == 'exit':
            break

        else:
            print('Not a valid command, try again!')


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
