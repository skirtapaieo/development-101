import json
import re

class Contact:
    def __init__(self, first_name, last_name, mobile=None, home=None, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.home = home
        self.email = email
        self.address = address

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Mobile: {self.mobile}, Home: {self.home}, Email: {self.email}, Address: {self.address}"


class ContactList:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add(self, contact):
        if self.exists(contact):
            print("Contact with same first name and last name already exists.")
            return False
        self.contacts.append(contact.__dict__)
        return True

    def delete(self, first_name, last_name):
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                self.contacts.remove(contact)
                return True
        print("Contact not found.")
        return False

    def list(self):
        return [Contact(**contact) for contact in sorted(self.contacts, key=lambda k: k['first_name'])]

    def search(self, first_name, last_name):
        return [Contact(**contact) for contact in self.contacts if first_name in contact['first_name'] and last_name in contact['last_name']]

    def exists(self, contact):
        return any(c['first_name'] == contact.first_name and c['last_name'] == contact.last_name for c in self.contacts)


def main():
    contact_list = ContactList()
    print("Welcome to your contact list!")
    print('Enter "add" to add a contact.')
    print('Enter "delete" to delete a contact.')
    print('Enter "list" to list all contacts.')
    print('Enter "search" to search for a contact.')
    print('Enter "q" to quit the program.')

    while True:
        command = input("\nEnter command: ")
        if command == "q":
            break
        elif command == "add":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            mobile = input("Mobile Phone Number: ")
            home = input("Home Phone Number: ")
            email = input("Email Address: ")
            address = input("Address: ")
            contact = Contact(first_name, last_name, mobile, home, email, address)
            if contact_list.add(contact):
                print("Contact Added!")
        elif command == "delete":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            if contact_list.delete(first_name, last_name):
                print("Contact Deleted!")
        elif command == "list":
            contacts = contact_list.list()
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")
        elif command == "search":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            contacts = contact_list.search(first_name, last_name)
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact}")
        else:
            print("Unknown command.")

    contact_list.save()
    print("Contacts were saved successfully.")


if __name__ == "__main__":
    main()
