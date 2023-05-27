print("Welcome to Marv's Contact Book")
contactNames = []
phoneNumbers = []
numOfContacts = 2
options = input('Add (a) Search (s) Quit (q)')
if options == 'a':
    for i in range(numOfContacts):
        with open("contactlist", "a") as f:
            contactName = input("Name: ")
            phoneNumber = input("Phone Number: ")
            f.writelines((contactName, " : ", phoneNumber, "\n"))
            contactNames.append(contactName)
            phoneNumbers.append(phoneNumber)
            print("\nName\t\t\tPhone Number\n")
            print("{}\t\t\t{}".format(contactNames, phoneNumbers))
elif options == 's':
    with open("contactlist", "r") as f:
        searchContact = input("\nEnter Search Term: ")
        for i in f:
            if searchContact in i:
                print(i)
else:
    print("Goodbye")
