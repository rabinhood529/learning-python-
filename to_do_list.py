# to do list
print("to do list")
Task = []



# menu
print("option")
print("1.ADD task \n"
"2.Show task \n"
"3.Search task \n"
"4.Remove task \n")
option = int(input("select option:"))
match option:
    case 1:
        task_name = input("enter a task name:" )
        task_deadline = input("enter the deadline date (YYY-MM-DD):")
        task_last_date = input("enter the deadline date (HH:MM):")
        new_task = {"task_name" : task_name,
                "task_deadline": task_deadline,
                "task_last_date": task_last_date}
                # Task.append(new_task)

    case 2:
        for Task in Task:
            print(Task)
    case 3:
        Search =input("enter task to serch:")
        for Tasks in Task:
            if Search in Tasks["task_name"]:
                print(Tasks)
                
    case 4:
        remove = input("enter a task to be removed:")
        for pop in remove:
            if pop["task_name"] == remove:
                Task.remove(pop)
                print("task removed!")
                break
            else:
                print("task not found.")




