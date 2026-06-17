try:
    num = int(input("Enter Number: "))
    result = 100 / num

    print(result)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")