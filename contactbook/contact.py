contactNames = []
phoneNumbers = []
numOfContacts = 2

for i in range(numOfContacts) :
    contactName = input("Name: ")
    phoneNumber = input("Phone Number: ")
    contactNames.append(contactName)
    phoneNumbers.append(phoneNumber)

print("\nName\t\t\tPhone Number\n")

for i in range(numOfContacts) :
    print("{}\t\t\t{}".format(contactNames[i], phoneNumbers[i]))

searchContact = input("\nEnter Search Term: ")
print("search Result")
if searchContact in contactNames :
    index = contactNames.index(searchContact)
    phoneNumber = phoneNumbers[index]
    print("Name {}, Phone Number: {}".format(searchContact, phoneNumber))
else:
    print("Name not found")