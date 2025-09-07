tasks = []   # List containing all the tasks    
print("--- Welcome to Task Manager App ---")
total_task=int(input("How many tasks you want to add? "))
for i in range(1,total_task+1):       # For adding all the tasks
    task_name = input(f"Enter task {i} : ")
    tasks.append(task_name)
print(f"Today's tasks are : {tasks}")    

while True:
    operation=int(input("Enter 1- Add\n2- Update\n3- Delete\n4- View\n5- Exit/Stop\n"))
    # For Adding a new Task
    if operation==1:
        add = input("Add a task: ")
        tasks.append(add)
        print(f"Task {add} has been added.")
    # For Updating an existing Task
    elif operation==2:
        updated_val = input("Which task name you want to update? ") 
        if updated_val in tasks:
            up = input("Enter new task : ")   
            ind = tasks.index(updated_val)
            tasks[ind]=up
            print(f"Updated Task {up}")
    # For Deleting a task
    elif operation==3:
        deleted_task =input("Enter task you want to delete : ") 
        if deleted_task in tasks:
            ind = tasks.index(deleted_task)   
            del tasks[ind]    
            print(f"Task {deleted_task} has been deleted.")
    # For showing all the tasks        
    elif operation==4:
        print(f"Total tasks are : {tasks}")
    # To exit the program    
    elif operation==5:
        print("Closing the program...")
        break    
    else:
        print("Invalid Input.Please Enter (1 or 2 or 3 or 4 or 5)")
