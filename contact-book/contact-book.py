import json

FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save contacts to the file
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    # Add Contact
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name and phone:
            contacts.append({"name": name, "phone": phone})
            save_contacts(contacts)
            print("Contact saved!")
        else:
            print("Name and phone cannot be empty.")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            print("\nYour Contacts:")
            for i, contact in enumerate(contacts, 1):
                name = contact.get("name", "Unknown")
                phone = contact.get("phone", "No number")
                print(f"{i}. {name} - {phone}")

    # Search Contact
    elif choice == "3":
        search = input("Enter name to search: ").strip().lower()

        found = False

        for i, contact in enumerate(contacts, 1):
            name = contact.get("name", "").lower()

            if search in name:
                phone = contact.get("phone", "No number")
                print(f"{i}. {contact.get('name','Unknown')} - {phone}")
                found = True

        if not found:
            print("Contact not found")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")