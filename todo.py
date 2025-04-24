def menu():
    print("\nTO-DO LIST MENU")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def Add_task(tasks):
    userInput = input("Enter task to add: ")
    tasks.append(userInput)
    print(f"The task '{userInput}' has been added.")

def View_task(tasks):
    if not tasks:
        print("No tasks available to view.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def Delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    View_task(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"The task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            Add_task(tasks)
        elif choice == '2':
            View_task(tasks)
        elif choice == '3':
            Delete_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()