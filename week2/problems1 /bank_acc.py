# Imports


# Globals

initial_balance = raw_input("Please enter the amount for your first deposit:")
total_funds = initial_balance

# Function
def get_balance():
    global total_funds
    return total_funds


def deposit_money(amount):
    global total_funds
    if amount <= 0:
      return "Show me the money"
    else:
        total_funds = total_funds + amount
        return total_funds
        


def withdraw_money(amount):
    global total_funds
    if total_funds >= amount:
        total_funds -= amount
        return "You just witdraw " + str(amount) + " and you have left " + str(total_funds) + " in your account"
    else:
        return "Not sufficient funds in your acc"

# Main
def main():


# Program run
if __name__ == '__main__':
    main()
