def task():
    tasks=[]
    print("---WELCOME TO THE TASK MANAGER APP---")
    total_task=int(input("Enter how many task you want to add: "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}: ")
        tasks.append(task_name)
    print("Todays tasks are \n",tasks)
    while True:
        operation=int(input("Enter\n1)Add\n2)Update\n3)Delete\n4)view\n5)Exit/Stop "))
        if operation==1:
            add=input("Enter task you want to add")
            tasks.append(add)
            print("Task",add,"has been added")
        elif operation==2:
            updated_val=input("Which task do you want to update?")
            if updated_val in tasks:
                update=input("Enter new task: ")
                ind=tasks.index(updated_val)
                tasks[ind]=update
                print("Task",update,"updated")
        elif operation==3:
            del_val=input("Which task do you want to delete: ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print("Task",del_val,"deleted")
        elif operation==4:
            print("Total tasks",tasks)
        elif operation==5:
            print("Closing the program:)..:)")
            break
        else:
            print("Invalid choice")
task()