# main.py

from manager import StudentManager

def main():
    manager = StudentManager()

    menu = """
╔══════════════════════════════╗
║   Student Management System  ║
╠══════════════════════════════╣
║  1. Add Student              ║
║  2. Update Student           ║
║  3. Delete Student           ║
║  4. List All Students        ║
║  5. Exit                     ║
╚══════════════════════════════╝
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            sid   = input("Enter Student ID   : ").strip()
            name  = input("Enter Name         : ").strip()
            grade = input("Enter Grade (A-F)  : ").strip().upper()
            manager.add_student(sid, name, grade)

        elif choice == "2":
            sid   = input("Enter Student ID to update : ").strip()
            name  = input("New Name  (press Enter to skip): ").strip()
            grade = input("New Grade (press Enter to skip): ").strip().upper()
            manager.update_student(sid, name or None, grade or None)

        elif choice == "3":
            sid = input("Enter Student ID to delete: ").strip()
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("\n👋 Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()