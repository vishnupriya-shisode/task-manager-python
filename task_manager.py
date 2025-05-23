print("Welcome to Task Manager!")
print("Type 'help' to see available commands.")
tasks = []  # this is an empty list to store all your tasks

def show_help():
    print("Available commands: add, view, help, quit")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

while True:
    command = input(">> What would you like to do? ")

    if command == "help":
        print("Available commands: add, view, quit")
    elif command == "add":
        task = input("Enter your task: ")
        tasks.append(task)  # we add the task to the list
        print(f"Task '{task}' added!")
    elif command == "view":
        if not tasks:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i, t in enumerate(tasks, 1):  # print all tasks with numbers
                print(f"{i}. {t}")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Sorry, I didn't understand that.")
