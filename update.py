import json
from datetime import datetime

def update(save_data, args):
    updated = False
    with open(save_data, "r+") as file:
        tasks = json.load(file)
        for task in tasks:
            if task["task name"] == args.update or args.update == str(task["id"]):
                task_index = task["id"] - 1
                task["status"] = args.status
                task["description"] = args.desc
                task["updated at"] = datetime.now().strftime("%H:%M %b %d, %Y")
                tasks[task_index] = task
                file.seek(0)
                file.truncate()
                json.dump(tasks, file, indent=4)
                updated = True
    if updated == True: 
        print(f"'{args.update}' successfully updated!")
    else:
        print("Task not found")
                