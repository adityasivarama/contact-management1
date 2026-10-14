cbook = {}

while True:
    print("\nWelcome to Contact Manager")
    print("Choose from the following options:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        cbook[name] = phone
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter the name to search: ")
        if name in cbook:
            print("Name:", name)
            print("Phone:", cbook[name])
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter the name to update: ")
        if name in cbook:
            phone = input("Enter the new phone number: ")
            cbook[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter the name to delete: ")
        if name in cbook:
            del cbook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == 5:
        if cbook:
            print("\nContact List:")
            for name, phone in cbook.items():
                print("Name:", name, "| Phone:", phone)
        else:
            print("No contacts available!")

    elif choice == 6:
        print("Thank you for using Contact Manager!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 6.")
