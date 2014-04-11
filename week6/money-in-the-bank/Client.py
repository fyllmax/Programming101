import os
import binascii
import hashlib
import smtp
import sql_manager


class Client():
    def __init__(self, id, username, email, balance, message, tan):
        self.__username = username
        self.__email = email
        self.__balance = balance
        self.__id = id
        self.__message = message
        self.__tan10 = tan.split(" ")

    def random_tan(self):
        random_tan = str(binascii.b2a_hex(os.urandom(32)))
        hash_tan = hashlib.sha224()
        hash_tan.update(random_tan.encode("utf-8"))
        return hash_tan.hexdigest()

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_message(self):
        return self.__message

    def tan_left(self):
        return len(self.__tan10)

    def set_message(self, new_message):
        self.__message = new_message

    def get_email(self):
        return self.__email

    def create_10_tans(self):
        for i in range(11):
            self.__tan10.append(self.random_tan())

    def get_left_tans(self):
        return self.__tan10

    def check_tanlist_empty(self):

        if len(self.__tan10) == 0 or self.__tan10[0] == '':
            return True
        return False

    def get_tan(self):

        if self.__tan10[0] == '0' or self.__tan10[0] == '':
            self.__tan10.pop(0)
            self.create_10_tans()
            sql_manager.update_tan(self.__username, self.__tan10)
            smtp.send_tan(self.__email, self.__tan10)

            return "Check your email for your tan codes."

        return "You still have tans to use"

    def get_new_tan(self):

        if len(self.__tan10) == 0:
            self.create_10_tans()
            sql_manager.update_tan(self.__username, self.__tan10)
            smtp.send_tan(self.__email, self.__tan10)

        return "Check your email for your tan codes."

    def deposit(self):

        print("Enter tan code to continue")
        tan_code = input("Code: ")

        if tan_code in self.__tan10 and tan_code != '':
            self.__tan10.remove(tan_code)
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.__balance += int(amount)
                return "You have deposited {}$".format(amount)
            return "Deposit can be negative or 0 $"

        return "Tan code does not exist"

    def withdraw(self):

        if self.__balance == 0:
            return "You are out of money. Bump!"

        elif self.__balance > 0:

            print("Enter tan code to continue")
            tan_code = input("Code: ")

            if tan_code in self.__tan10 and tan_code != '':
                self.__tan10.remove(tan_code)
                amount = int(input("Enter amount to withdraw: "))

                if 0 < amount <= self.__balance:
                    self.__balance -= amount
                    return "You have withdrawt {}$".format(amount)

                return "You enter either higher or negative amount, try again!"

            return "Tan code does not exist"
