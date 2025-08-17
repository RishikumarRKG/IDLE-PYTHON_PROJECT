tasks = []  

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("✅ Task added!")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_num - 1] = new_task
                print("Task updated!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nGoodbye! 👋")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
