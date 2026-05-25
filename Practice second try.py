import json
import os


class GIM:
    def __init__(self, name="", father_name="", Number="", fees="Unpaid", student_id=None):
        self.name = name
        self.father_name = father_name
        self.Number = Number
        self.fees = fees
        self.student_id = student_id

    def New_Students(self, student_id):
        self.name = input("Enter user name ===> ")
        self.father_name = input("Enter father name ===> ")
        self.Number = input("Enter user number ===> ")
        self.student_id = student_id
        return self

    def Save(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "father_name": self.father_name,
            "number": self.Number,
            "fees": self.fees
        }

    def Load(self):
        if os.path.exists("Save.json"):
            with open("Save.json", "r") as file:
                try:
                    data = json.load(file)
                    if isinstance(data, dict):
                        return [data]
                    return data
                except json.JSONDecodeError:
                    return []
        return []


def save_to_file(data):
    with open("Save.json", "w") as file:
        json.dump(data, file, indent=4)


def get_next_id(data):
    if not data:
        return 1
    return max(student["id"] for student in data) + 1


def is_id_exist(data, new_id):
    return any(student["id"] == new_id for student in data)


student = GIM()

while True:
    print("\n===== MENU =====")
    print("1. Add new student")
    print("2. Show student list")
    print("3. Edit student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ---------- ADD ----------
    if choice == "1":
        data = student.Load()

        new_id = get_next_id(data)

        student.New_Students(new_id)

        data.append(student.Save())

        save_to_file(data)

        print(f"✅ Student added successfully! ID = {new_id}")

    # ---------- SHOW ----------
    elif choice == "2":
        data = student.Load()

        if not data:
            print("⚠ No data found!")
        else:
            print("\n📋 Student List:")
            for s in data:
                print(f"ID: {s['id']} | Name: {s['name']} | Father: {s['father_name']} | Number: {s['number']}")

    # ---------- EDIT ----------
    elif choice == "3":
        data = student.Load()

        if not data:
            print("⚠ No data found!")
            continue

        edit_id = input("Enter student ID to edit ===> ")

        found = False

        for s in data:
            if str(s["id"]) == edit_id:
                found = True

                print("\nWhat do you want to edit?")
                print("1. Name")
                print("2. Father name")
                print("3. Number")
                print("4. ID")

                option = input("Choose option: ")

                if option == "1":
                    s["name"] = input("Enter new name ===> ")

                elif option == "2":
                    s["father_name"] = input("Enter new father name ===> ")

                elif option == "3":
                    s["number"] = input("Enter new number ===> ")

                elif option == "4":
                    while True:
                        new_id = int(input("Enter new ID ===> "))
                        if is_id_exist(data, new_id):
                            print("❌ This ID already exists! Enter another one.")
                        else:
                            s["id"] = new_id
                            break

                else:
                    print("❌ Invalid option!")

                save_to_file(data)
                print("✏️ Updated successfully!")
                break

        if not found:
            print("❌ Student not found!")

    # ---------- EXIT ----------
    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")