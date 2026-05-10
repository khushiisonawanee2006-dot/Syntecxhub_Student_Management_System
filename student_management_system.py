import json
student_grades={}

#load data
def load_data():
    global student_grades
    try:
        with open("students.json","r") as file:
            student_grades = json.load(file)
    except FileNotFoundError:
        student_grades={}

#save data
def save_data():
    with open("student.json","w") as file:
        json.dump(student_grades, file, indent=4)

#add student
def add_student(name, id, grade):
    #check uniqueID
    for student in student_grades.values():
        if student[id]==id:
            print("ID already exists")
            return
    student_grades[name]={
        "id" : id,
        "grade" : grade,
    }
    save_data()
    print(f"{name} added successfully")

#update student
def update_student(name, id, grade):
    if name in student_grades:
        student_grades[name]["id"] = id
        student_grades[name]["grade"] = grade
        save_data
        print(f"{name} updated successfully")
    else:
        print("student not found")

#delete
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        save_data()
        print(f"{name} deleted successfully")
    else:
        print("student not found")

#view
def display_all_students():
    if student_grades:
        print("\n----Student Records----")
        for name, details in student_grades.items():
            print(f"Name : {name}")
            print(f"ID : {details['id']}")
            print(f"Grade : {details['grade']}")
            print("--------------")
    else:
        print("No student records found")

def main():
    load_data()
    while True:
        print("\n----student management system----")
        print("1. Add")
        print("2. Update")
        print("3. Delete")
        print("4. View")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            id = int(input("Enter student ID: "))
            grade = input("Enter student grade: ")
            add_student(name, id, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            id = int(input("Enter new ID: "))
            grade = input("Enter new grade: ")
            update_student(name, id, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing Program....")
            break

        else:
            print("Invalid choice")

if __name__== "__main__":
    main()
    