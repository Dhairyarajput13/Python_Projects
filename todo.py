def task():
    tasks = []
    print("--------Welcome to task management app---------")
    task = int(input("Enter the number of tasks:"))
    for i in range(1,task+1):
        task_name = input("Enter the task name=")
        tasks.append(task_name)
    print(f"The tasks are = {tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/end"))
        if operation == 1:
            add = input("Enter the task you want to add=")
            tasks.append(add)
            print(f"Your task has been successfully added = {add}")

        elif operation == 2:
            update_val = input("Enter the task you want to update=")
            if update_val in tasks:
                new = input("Enter the new task=")
                ind = tasks.index(update_val)
                tasks[ind] = new
                print(f"updated task {new}")

        elif operation == 3:
            del_val = input("Which task you want to delete=")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]     
                print(f"Task {del_val} has been deleted")

        elif operation == 4:
            print (f" Total tasks {tasks}")

        elif operation == 5:
            print("closing of program....")  
            break

        else:
            print("invalid Input....")

task()            


           
