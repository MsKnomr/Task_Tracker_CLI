import argparse
import json
from os import path

parser = argparse.ArgumentParser(description="Task_Tracker")

parser.add_argument("--add", type=str, help="Input name of task")
parser.add_argument("--desc", type=str, default="No description provided", help="Description of task")
parser.add_argument(
    "--status", choices=["todo", "in-progress", "done"], default="todo",
    help="Current status of task. Options: ['todo', 'in-progress', 'done']"
    )
parser.add_argument("--view", default=False, action="store_true", help="Provides a list of current tasks")

args = parser.parse_args()

save_data = "data.json"

if args.view:
    try:
        with open(save_data, "r") as file:
            contents = file.read()
            print(contents)
    except Exception:
        print("No save file currently exists")

if args.add:

    new_task: dict [str: str] = {}

    new_task["task name"] = args.add
    new_task["description"] = args.desc
    new_task["status"] = args.status

    if path.exists(save_data) and path.isfile(save_data):
        with open(save_data, "r+") as f:
            data = json.load(f)
            #Loads the stored list into a new variable
            data.append(new_task)
            #Appends the new task to the end of the list
            f.seek(0)
            f.truncate()
            #Returns the pointer to the start of the file and then deletes the stored list
            json.dump(data, f, indent=4)
            #Writes the newly updated list to data.json
    # Opens the existing file and appends to it
    else:
        with open(save_data, "x+") as f:
            json.dump([new_task], f, indent=4)
    # Will create a new file named 'data.json', create a list containing only the new task dictionary
    # Will raise a FileExistsError if 'data.json' already exists (should be covered by previous if statement)