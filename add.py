import json
from os import path
from datetime import datetime

def add(save_data, args):

    id = 1
    new_task: dict [str: str] = {}

    if path.exists(save_data) and path.isfile(save_data):
        with open(save_data, "r+") as file:
            tasks = json.load(file)
            #Loads the stored list into a new variable
            for task in tasks:
                id += 1
            new_task["task name"] = args.add
            new_task["id"] = id
            new_task["status"] = args.status
            new_task["description"] = args.desc
            new_task["created at"] = datetime.now().strftime("%H:%M %b %d, %Y")
            tasks.append(new_task)
            #Appends the new task to the end of the list
            file.seek(0)
            file.truncate()
            #Returns the pointer to the start of the file and then deletes the stored list
            json.dump(tasks, file, indent=4)
            #Writes the newly updated list to data.json
        # Opens the existing file and appends to it
    else:
        new_task["task name"] = args.add
        new_task["id"] = id
        new_task["status"] = args.status
        new_task["description"] = args.desc
        new_task["created at"] = datetime.now().strftime("%H:%M %b %d, %Y")
        with open(save_data, "x+") as file:
            json.dump([new_task], file, indent=4)
            # Will create a new file named 'data.json', create a list containing only the new task dictionary
            # Will raise a FileExistsError if 'data.json' already exists (should be covered by previous if statement)
