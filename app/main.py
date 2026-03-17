import re
import db

def true_id(id):
    return id.isdigit()

def validate_name(name):
    name = name.strip()
    return len(name) <= 20

def validate_phone(phone):
    phone = phone.strip()
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None


def menu():
    print("\nPHONEBOOK MENU")
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Find by id")
    print("6. Exit")
    return input("Choose an action: ").strip()


def main():
    while True:
        choice = menu()

        if choice == '1':
            contacts = db.get_all_contacts()
            if not contacts:
                print("\nThe contact list is empty.")
            else:
                print("\nID | First Name | Last Name | Phone | Note")
                print("-" * 60)
                for i in contacts:
                    print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")

        elif choice == '2':
            f_n = input("First name: ").strip()
            l_n = input("Last name: ").strip()
            ph = input("Phone: ").strip()
            nt = input("Note: ").strip()

            if not validate_name(f_n):
                print("Eroor: first name must contain less than 20 characters")
                continue

            if not validate_name(l_n):
                print("Eroor: last name must contain less than 20 characters")
                continue

            if not validate_phone(ph):
                print("Error! phone must contain 10-20 digits and can start with +")
                continue

            db.add_contact(f_n, l_n, ph, nt)
            print("Done")

        elif choice == '3':
            id = input("Enter ID to update: ")
            if not true_id(id):
                print("Print norm id")
                continue
            c = db.get_contact_by_id(id)
            if c:
                f_n = input("New first name: ").strip()
                l_n = input("New last name: ").strip()
                ph = input("New phone: ").strip()
                nt = input("New note: ").strip()

                if not validate_name(f_n):
                    print("Eroor: first name must containl ess than 20 characters")
                    continue

                if not validate_name(l_n):
                    print("Error! last name must contain less than 20 characters")
                    continue

                if not validate_phone(ph):
                    print("Error! phone must contain 10-20 digits and can start with +")
                    continue
                db.update_contact(id, f_n, l_n, ph, nt)
                print("Updated")
            else:
                print("The id was not found")


        elif choice == '4':
            id = input("Enter ID to delete: ")
            if not true_id(id):
                print("Print norm id")
                continue
            c = db.get_contact_by_id(id)
            if c:

                db.delete_contact(id)
       
                print("Deleted")
            else:
                print("The id was not found")
         

        elif choice == '5':
            id = input("Enter ID: ")
            if not true_id(id):
                print("Print norm id")
                continue
            c = db.get_contact_by_id(id)
            if c:
                print(f"Found: {c[1]} | {c[2]} | {c[3]} | {c[4]}")
            else:
                print("The contact not found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Error! choose a number from 1 to 6.")


if __name__ == "__main__":
    main()