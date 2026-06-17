while True:

    print("\n1.Write Note")
    print("2.Read Notes")
    print("3.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        note = input("Enter Note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

    elif choice == "2":

        try:
            with open("notes.txt", "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No notes available")

    elif choice == "3":
        break