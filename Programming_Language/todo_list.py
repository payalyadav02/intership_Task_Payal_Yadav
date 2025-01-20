task = []
def menu():
    while True:
        print("\n--- To Do List ----")
        print("1. Add Your New Task")
        print("2. Edit Your Existing Task")
        print("3. List of All Tasks")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            list_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Choice. Please Try Again!")

def add_task():
    title = input("Enter Your Task: ")
    status = "New"  
    task.append({"task": title, "status": status})
    print(f"Task '{title}' added successfully with status '{status}'.")

def edit_task():
    if not task:
        print("No tasks to edit.")
        return

    list_task()  
    try:
        task_id = int(input("Enter the task number to edit: "))
        if 1 <= task_id <= len(task):
            new_title = input("Enter New Title (leave blank to keep current title): ")
            new_status = input("Enter New Status (New/In Progress/Completed/Cancelled): ")

            if new_title:
                task[task_id - 1]["task"] = new_title
            if new_status in ["New", "In Progress", "Completed", "Cancelled"]:
                task[task_id - 1]["status"] = new_status
            else:
                print("Invalid status. Keeping the current status.")

            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def list_task():
    if not task:
        print("No tasks found.")
        return

    print("\n--- List of Tasks ---")
    for i, t in enumerate(task, start=1):
        print(f"{i}. Title: {t['task']}, Status: {t['status']}")

def remove_task():
    if not task:
        print("No tasks to remove.")
        return

    list_task() 
    try:
        task_id = int(input("Enter the task number to remove: "))
        if 1 <= task_id <= len(task):
            removed_task = task.pop(task_id - 1)
            print(f"Task '{removed_task['task']}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

menu()
