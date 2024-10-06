import re

# Dictionary to store contact information
contacts = {}

def display_menu():
    print("""
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file 
8. Quit
    """)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    # Validate phone number and email using regex
    if not re.match(r"^\+?[0-9]{7,15}$", phone):
        print("Invalid phone number format. Please try again.")
        return
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        print("Invalid email format. Please try again.")
        return
    
    additional_info = input("Enter any additional info (optional): ")
    
    # Use phone number as the unique identifier
    contacts[phone] = {
        'name': name,
        'email': email,
        'additional_info': additional_info
    }
    print("Contact added successfully.")

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone in contacts:
        print(f"Editing contact: {contacts[phone]['name']}")
        name = input(f"Enter new name ({contacts[phone]['name']}): ") or contacts[phone]['name']
        email = input(f"Enter new email ({contacts[phone]['email']}): ") or contacts[phone]['email']
        additional_info = input(f"Enter new additional info ({contacts[phone]['additional_info']}): ") or contacts[phone]['additional_info']
        
        contacts[phone] = {
            'name': name,
            'email': email,
            'additional_info': additional_info
        }
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    query = input("Enter the name or phone number to search: ")
    for phone, details in contacts.items():
        if query in details['name'] or query in phone:
            print(f"Contact found: {details['name']}, Phone: {phone}, Email: {details['email']}, Info: {details['additional_info']}")
            return
    print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for phone, details in contacts.items():
            print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Info: {details['additional_info']}")

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for phone, details in contacts.items():
                file.write(f"{phone},{details['name']},{details['email']},{details['additional_info']}\n")
        print("Contacts exported successfully.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                phone, name, email, additional_info = line.strip().split(',')
                contacts[phone] = {
                    'name': name,
                    'email': email,
                    'additional_info': additional_info
                }
        print("Contacts imported successfully.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            display_all_contacts()
        elif choice == 6:
            export_contacts()
        elif choice == 7:
            import_contacts()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
