# Exam Seat Allocation System

students = []
rooms = {}


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    subject = input("Enter Subject: ")

    student = {
        "roll": roll,
        "name": name,
        "subject": subject,
        "room": None,
        "seat": None
    }

    students.append(student)
    print("Student added successfully!\n")


# Add Room
def add_room():
    room_no = input("Enter Room Number: ")
    capacity = int(input("Enter Room Capacity: "))

    rooms[room_no] = capacity

    print("Room added successfully!\n")


# Allocate Seats
def allocate_seats():
    if len(students) == 0:
        print("No students available.\n")
        return

    if len(rooms) == 0:
        print("No rooms available.\n")
        return

    student_index = 0

    for room_no, capacity in rooms.items():

        for seat in range(1, capacity + 1):

            if student_index >= len(students):
                break

            students[student_index]["room"] = room_no
            students[student_index]["seat"] = seat

            student_index += 1

        if student_index >= len(students):
            break

    if student_index < len(students):
        print("Not enough seats for all students.")
    else:
        print("Seats allocated successfully.")

    print()


# Search Student
def search_student():
    roll = input("Enter Roll Number: ")

    found = False

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Details")
            print("----------------------")
            print("Name   :", student["name"])
            print("Roll   :", student["roll"])
            print("Subject:", student["subject"])
            print("Room   :", student["room"])
            print("Seat   :", student["seat"])

            found = True
            break

    if not found:
        print("Student not found.")

    print()


# Display Seating Arrangement
def display_seating():
    print("\n===== SEATING ARRANGEMENT =====")

    for room_no in rooms:

        print("\nRoom:", room_no)

        found = False

        for student in students:

            if student["room"] == room_no:

                print(
                    "Seat:", student["seat"],
                    "| Roll:", student["roll"],
                    "| Name:", student["name"],
                    "| Subject:", student["subject"]
                )

                found = True

        if not found:
            print("No students allocated.")

    print()


# Save Data to File
def save_to_file():

    file = open("exam_seat_allocation.txt", "w")

    file.write("===== EXAM SEAT ALLOCATION =====\n\n")

    for student in students:

        file.write(
            "Roll: " + student["roll"] +
            " | Name: " + student["name"] +
            " | Subject: " + student["subject"] +
            " | Room: " + str(student["room"]) +
            " | Seat: " + str(student["seat"]) +
            "\n"
        )

    file.close()

    print("Allocation saved to exam_seat_allocation.txt\n")


# Main Menu
while True:

    print("================================")
    print("   EXAM SEAT ALLOCATION SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. Add Exam Room")
    print("3. Allocate Seats")
    print("4. Search Student")
    print("5. Display Seating Arrangement")
    print("6. Save Allocation")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_room()

    elif choice == "3":
        allocate_seats()

    elif choice == "4":
        search_student()

    elif choice == "5":
        display_seating()

    elif choice == "6":
        save_to_file()

    elif choice == "7":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.\n")