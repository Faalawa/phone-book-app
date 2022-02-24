selected_option = input("what do you want to do(1-5)?")
if selected_option == "2":
    name =input("what is the contact's name?")
    phone_number = input("what is their phone number?")
    phonebook[name] = phone_number
    print("contact added successfully!")
    print(menu)
    
