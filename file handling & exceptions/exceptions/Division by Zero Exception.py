try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")