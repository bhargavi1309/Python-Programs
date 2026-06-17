try:
    num = int(input("Enter Number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)