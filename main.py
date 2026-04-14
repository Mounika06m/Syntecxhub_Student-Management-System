from manager import StudentManager

def main():
    mgr = StudentManager()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")   
        print("3. Delete Student")
        print("4. List All Students")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("Enter ID: ").strip()
            name = input("Enter Name: ").strip()
            grade = input("Enter Grade: ").strip()
            mgr.add(sid, name, grade)
        elif choice == "2":
            sid = input("Enter ID to update: ").strip()
            name = input("New Name: ").strip()
            grade = input("New Grade: ").strip()
            mgr.update(sid, name, grade)
        elif choice == "3":
            sid = input("Enter ID to delete: ").strip()
            mgr.delete(sid)
        elif choice == "4":
            mgr.list_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()