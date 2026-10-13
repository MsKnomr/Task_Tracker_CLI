import json

def view(save_data, args):

    requested_tasks = []
    tasks_found = False

    if args.view == "None":
            try:
                with open(save_data, "r") as file:
                    requested_tasks = file.read()
                    tasks_found = True
            except Exception:
                print("No save file currently exists")

    elif args.view == "todo":
        with open(save_data, "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    if task["status"] == args.view:
                        requested_tasks.append(task)
                        tasks_found = True

    elif args.view == "in-progress":
            with open(save_data, "r") as file:
                    tasks = json.load(file)
                    for task in tasks:
                        if task["status"] == args.view:
                            requested_tasks.append(task)
                            tasks_found = True

    elif args.view == "completed":
            with open(save_data, "r") as file:
                    tasks = json.load(file)
                    for task in tasks:
                        if task["status"] == args.view:
                            requested_tasks.append(task)
                            tasks_found = True
    
    if tasks_found == True: 
        print(requested_tasks)
    else:
         print(f"No tasks found with the requested [STATUS]: {args.view}")