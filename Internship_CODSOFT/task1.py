  # TASK 1
# One helpful project that aids users in effectively managing and organizing their chores is a To-Do List application. 
# The goal of this project is to utilize Python to develop a command-line or graphical user interface (GUI) 
# that will enable users to make, modify, and monitor to-do lists.

tasks= []

def add_task():
    enter_task = input("Kindly Enter Task: ")
    tasks.append(enter_task)
    print("Task added succesfully")

def view_tasks():
    if tasks:
        print("Tasks: ")
        for task in tasks:
            print(task)
    else:
        print("No tasks found. ")

def view_task():    
    if tasks:
        print("Tasks: ")
        for task in tasks:
            print(task)
    else:
        print("No Task Found. ")

def update_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter Task Number To Update: ")) -1
        if 0 <= task_index < len(tasks):
            new_task_name = input("Kindly Enter The New Task: ")
            tasks[task_index] = new_task_name
            print("Task Updated Successfully.")
        else:
            print("Invalid Task Number.")
    else:
        print("No Tasks To Update.")

def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter Task Number To Delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks [task_index]
            print("Task Deleted Successfully. ")
        else:
            print("Invalid Task Number. ")
    else:
        print("No Tasks To Delete. ")

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Kindly Enter Your Choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
