list = []
list_id = 1

def show_tasks():
    """Display all tasks"""
    if not list:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for t in list:
            print(f"  {t['id']}. {t['title']}")

def add_task(title):
    """Add a new task"""
    global list_id
    new_task = {"id": list_id, "title": title.strip().capitalize()}
    list.append(new_task)
    list_id += 1
    print(f"Task added: {new_task['title']}")

def delete_task(tid):
    """Delete a task by ID"""
    for t in list:
        if t["id"] == tid:
            list.remove(t)
            print(f"Deleted: {t['title']}")
            return
    print("Task not found!")

# Main menu loop
while True:
    print("\n===== Task Manager =====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        title = input("Enter task title: ")
        if title.strip():
            add_task(title)
        else:
            print("Task title cannot be empty!")
    elif choice == "3":
        if not list:
            print("No tasks to delete. Please add some first!")
        else:
            tid_input = input("Enter task ID to delete: ")
            try:
                tid = int(tid_input)
                delete_task(tid)
            except ValueError:
                print("Invalid input! Please enter a number.")
    elif choice == "4":
        print("Thanks for using Task Manager!")
        break
    else:
        print("Invalid choice. Please select from 1–4.")
