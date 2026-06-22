tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if len(tasks) > 0:
            try:
                task_num = int(input("Enter task number to update: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter updated task: ")
                    tasks[task_num - 1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        show_tasks()

        if len(tasks) > 0:
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please select between 1 and 5.")