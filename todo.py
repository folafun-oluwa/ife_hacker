def menu():

    print("TO-DO LIST MENU")
    print("Add task")
    print("View task")
    print("Delete task")
    print("Exit") 

def Add_task(task):
    userInput = input("Enter task to add: ")
    print("The task added is", {"task"})

def View_task(task):
    userInput = input("Pick the task to view: ")
    print("The task viewed is", {"task"})

def Delete_task(task):
    userInput = input("Pick the task to delete: ")
    print("This task has been deleted")
   
task = ["Add_task", "View_task", "Delete_task", "Exit"]



def main():
    tasks = []
    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            Add_task(task)
        elif choice == '2':
            View_task(task)
        elif choice == '3':
            Delete_task(task)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()