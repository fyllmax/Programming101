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
    print("Welcome to our bank service. You are not logged in. \nPlease register, login or forgotten_pass")

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
                print('Hello {}. Welcome again! Please enter your password to proceed '.format(username))

                time_now = int(time())
                time_between_logins = time_now - sql_manager.get_login_time(username)

                if time_between_logins > 300:
                    tries = 1

                while tries < 6:
                    password = getpass.getpass()
                    logged_user = sql_manager.login(username, password)

                    if logged_user:
                        sql_manager.insert_login_time_of_register(username)
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

        elif command == 'forgotten_pass':

            username = input('Enter username: ')

            if username == sql_manager.check_user_exist(username):

                email = input('Enter email: ')

                if email == sql_manager.check_user_email(username):

                    sql_manager.create_random_hash(username)

                    get_random_hash = sql_manager.get_pass_code_hash(username)

                    smtp.send_email(email, get_random_hash)

                    print('Check your email for the secret code')

                    enter_hash = input('Enter the secret code: ')

                    if enter_hash == sql_manager.get_pass_code_hash(username):

                        new_password_pass = False

                        while not new_password_pass:

                            new_password = getpass.getpass('Enter new passowrd: ')

                            if len(new_password) >= 8 and check_pass(new_password):
                                new_password_pass = True
                                sql_manager.change_password(new_password, username)
                                print('You Successfully changed your password')
                                break

                            print("Password shoud be at least 8 characters, and shound contain a capital letter, a number and a special charachter")

                else:
                    print("There is no such email in our database")

            else:
                print('There is no such user in our database')

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
        print("")
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')
            print("You have left with {} tan codes".format(logged_user.tan_left()))
            # print("Your email is:" + logged_user.get_email())

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            help_command = [
                "List of commands:",
                "",
                "*info - for showing account info",
                "*changepass - for changing passowrd",
                "*change-message - for changing users message",
                "*show-message - for showing users message",
                "*deposit - putting funds in your bank acc",
                "*withdraw - getting funds out of your bank acc",
                "*balance - showing current available funds",
                "*get_tan - sends email with 10 tan codes needed for transaction"]

            print('\n'.join(help_command))

        elif command == 'get_tan':
            print(logged_user.get_tan())

        elif command == 'deposit':
            print(logged_user.deposit())

        elif command == 'withdraw':
            print(logged_user.withdraw())

        elif command == 'balance':
            print(logged_user.get_balance())

        elif command == 'exit':

            sql_manager.update_balance(logged_user.get_username(), logged_user.get_balance())

            if logged_user.check_tanlist_empty():
                print("You had 0 tan codes, so we send you new ones.")
                print(logged_user.get_new_tan())

            sql_manager.update_tan(logged_user.get_username(), logged_user.get_left_tans())

            break

        else:
            print('Not a valid command, try again!')


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
