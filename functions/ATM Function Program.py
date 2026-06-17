balance = 1000

def withdraw(amount):

    global balance

    if amount <= balance:
        balance -= amount
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")

withdraw(500)

print(balance)