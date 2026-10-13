import json

def refresh(save_data):
    with open(save_data, "r+") as file:
            tasks = json.load(file)
            task_id = 1
            for task in tasks:
                task["id"] = task_id
                task_id += 1
            file.seek(0)
            file.truncate()
            json.dump(tasks, file, indent=4)
    print("Task IDs successfully updated")            