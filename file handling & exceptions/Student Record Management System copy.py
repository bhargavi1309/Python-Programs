while True:

    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")

        with open("students.txt", "a") as file:
            file.write(name + "\n")

    elif choice == "2":

        try:
            with open("students.txt", "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No records found")

    elif choice == "3":
        break