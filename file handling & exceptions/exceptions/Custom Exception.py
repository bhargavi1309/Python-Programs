age = int(input("Enter Age: "))

try:
    if age < 18:
        raise Exception("Not Eligible")

    print("Eligible")

except Exception as e:
    print(e)