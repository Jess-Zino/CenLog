import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["CENLog"]
mytab = mydb["Student details"]

def find_student():
    print("Find a Student\n")
    check = input("How do you want to find this student:\n1. First Name\n2. Last Name\n3. Matriculation Number\n4. Room Number\n5. Hall\n6. Cancel Search\n")
    if check == '1':
        chck = input("First Name:")
        cursor = mytab.find({"firstname": chck.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found.")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
    elif check == '2':
        chck = input("Last Name:")
        cursor = mytab.find({"lastname": chck.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found.")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
    elif check == '3':
        chck = input("Matriculation Number:")
        cursor = mytab.find({"matnum": chck.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found.")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
    elif check == '4':
        chck = input("Room Number:")
        cursor = mytab.find({"room": chck.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found.")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
    elif check == '5':
        chck = input("Hall:")
        cursor = mytab.find({"hall": chck.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found.")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
    elif check == '6':
        print("Cancel Search")
        sys.exit()
    else:
        print("Invalid Option")

def update_document(matric_number, field_to_update, new_value):
    try:
        filter_criteria = {"matnum": matric_number}
        update_data = {"$set": {field_to_update: new_value}}
        result = mytab.update_one(filter_criteria, update_data)

        if result.modified_count > 0:
            print(f"Document with Matric Number {matric_number} updated successfully.")
        else:
            print(f"Document with Matric Number {matric_number} not found or no changes made.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    activity = input("Welcome to CEN434 Student Log\nHow may I help you today:\n1. List of All Students\n2. Add New Student\n3. Find a Student\n4. Update Student Details\n5. Delete Student from Log\n6. End Program\n")

    if activity == '1':
        if mytab.count_documents({}) == 0:
            print("No Records found\n")
        else:
            for x in mytab.find():
                print(x["lastname"] + " " + x["firstname"] + "\t " + x["matnum"])
    elif activity == '2':
        newfnam = input("First Name: ")
        newlnam = input("Last Name: ")
        newmat = input("Matriculation Number: ")
        newroom = input("Room Number: ")
        newhall = input("Hall:")
        query = {"firstname": newfnam.capitalize(), "lastname": newlnam.capitalize(), "matnum": newmat.upper(), "room": newroom.capitalize(), "hall": newhall.capitalize()}
        mytab.insert_one(query)
        print("Student Successfully Added")
    elif activity == '3':
        find_student()
    elif activity == '4':
        matric_number = input("Enter Matriculation Number: ")
        field_to_update = input("Enter the field to update (room or hall): ").lower()
        new_value = input(f"Enter the new {field_to_update.capitalize()} value: ").capitalize()

        if field_to_update not in ["room", "hall"]:
            print("Invalid field name. Please specify 'room' or 'hall'.")
        else:
            update_document(matric_number, field_to_update, new_value)
    elif activity == '5':
        print("Delete Student from Log")
        check = input("Delete Student with Matriculation Number: ")
        cursor = mytab.find({"matnum": check.capitalize()})
        result_list = list(cursor)
        if len(result_list) == 0:
            print("Student not found. Delete Failed\n\n")
        else:
            for x in result_list:
                print("\nFirst Name:" + x["firstname"] + "\nLast Name:" + x["lastname"] + "\nMatriculation Number:" + x["matnum"] + "\nRoom:" + x["room"] + "\nHall:" + x["hall"])
                confirm = input("Do you want to delete " + x["lastname"] + " " + x["firstname"] + " from the Log? y/n")
                if confirm == 'y':
                    mytab.delete_one({"matnum": check})
                else:
                    print("Delete failed")
    elif activity == '6':
        print("Ending Program Now")
        sys.exit()
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main()
