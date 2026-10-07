import json
from os import path

def add(save_data, args):
    
    new_task: dict [str: str] = {}

    new_task["task name"] = args.add
    new_task["description"] = args.desc
    new_task["status"] = args.status

    if path.exists(save_data) and path.isfile(save_data):
        with open(save_data, "r+") as file:
            data = json.load(file)
            #Loads the stored list into a new variable
            data.append(new_task)
            #Appends the new task to the end of the list
            file.seek(0)
            file.truncate()
            #Returns the pointer to the start of the file and then deletes the stored list
            json.dump(data, file, indent=4)
            #Writes the newly updated list to data.json
        # Opens the existing file and appends to it
    else:
        with open(save_data, "x+") as file:
            json.dump([new_task], file, indent=4)
            # Will create a new file named 'data.json', create a list containing only the new task dictionary
            # Will raise a FileExistsError if 'data.json' already exists (should be covered by previous if statement)
