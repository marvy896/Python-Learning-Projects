import os
print("Welcome to Marv's Contact Book \n")
contactNames = []


options = input('Add (a) Search (s) Quit (q) Print (p) Delete (d): ')
if options == 'a':
    if os.path.exists("contactlist"):
        with open("contactlist", "r") as f:
            for i in f:
                contactNames.append(i)
    contactName = input("Name: ")
    phoneNumber = input("Phone Number: ")
    contactNames.append(contactName + " : " + phoneNumber + "\n")
    contactNames.sort(key= str.lower)
    with open("contactlist", "w") as f:
        f.writelines(contactNames)
elif options == 's':
    with open("contactlist", "r") as f:
        searchContact = input("\nEnter Search Term: ")
        for i in f:
            if searchContact in i:
                print(i)
elif options == 'p':
    with open("contactlist", "r") as f:
        for i in f:
            print(i)
elif options == 'd':
    with open("contactlist", "r") as f:
        deleteOption = input("Enter delete term: ")
        for i in f:
            if deleteOption.lower() not in i.lower():
                contactNames.append(i)
    with open("contactlist", "w") as f:
        f.writelines(contactNames)
else:
    print("Goodbye")
