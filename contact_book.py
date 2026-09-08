dict={}
while True:
    while True:
        try:
            choice=int(input("Enter your choice\n1.Add contact\n2.View contact list\n3.Search contact\n4.Update contact\n5.Delete contact\n6.Exit\nYour choice is "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice==1:
        while True:
            try:
                dict["Name"]=str(input("Enter name of the contact: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid name.")
        while True:
            try:
                dict["Phone"]=int(input("Enter phone number of the contact: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid phone number.")
        while True:
            try:
                dict["Email"]=str(input("Enter email of the contact: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid email.")
        while True:
            try:
                dict["Address"]=str(input("Enter address of the contact: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid address.")
        print("Contact added successfully!")

    elif choice==2:
        if dict:
            for i in dict:
                print("Contact List:")
                print(f"Name: {dict['Name']}\nPhone: {dict['Phone']}\nEmail: {dict['Email']}\nAddress: {dict['Address']}")
        else:
            print("List is Empty...")


    elif choice==3:
        cont=int(input("Enter the phone number of the contact you want to search: "))
        if dict["Phone"]==cont:
            print(f"Name: {dict['Name']}\nPhone: {dict['Phone']}\nEmail: {dict['Email']}\nAddress: {dict['Address']}")
        else:
            print("Contact not found.")

    elif choice==4:
        cont=int(input("Enter the phone number of the contact you want to update: "))
        if dict["Phone"]==cont:
            while True:
                try:
                    dict["Name"]=str(input("Enter name of the contact: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid name.")
            while True:
                try:
                    dict["Phone"]=int(input("Enter phone number of the contact: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid phone number.")
            while True:
                try:
                    dict["Email"]=str(input("Enter email of the contact: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid email.")
            while True:
                try:
                    dict["Address"]=str(input("Enter address of the contact: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid address.")
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice==5:
        cont=int(input("Enter the phone number of the contact you want to delete: "))
        if dict["Phone"]==cont:
            dict.clear()
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice==6:
        print("Exiting the program...")
        break

    deci=input("Do you want to continue (y/n): ")
    deci=deci.lower()
    if deci=="n":
        break
