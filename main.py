import argparse
import json
from os import path

parser = argparse.ArgumentParser(description="Task_Tracker")

parser.add_argument("task_name", type=str, help="Input name of task")
parser.add_argument("--desc", type=str, default="No description provided", help="Description of task")
parser.add_argument(
    "--status", choices=["todo", "in-progress", "done"], default="todo",
    help="Current status of task. Options: ['todo', 'in-progress', 'done']"
    )

args = parser.parse_args()

new_task = {}

new_task["task name"] = args.task_name
new_task["description"] = args.desc
new_task["status"] = args.status

save_data = "data.json"

if path.exists(save_data) and path.isfile(save_data):
    with open(save_data, "a") as f:
        json.dump(new_task, f)
#Opens the existing file and appends to it
else:
    with open(save_data, "x") as f:
        json.dump(new_task, f)
#Will create a new file named 'data.json' but will raise a FileExistsError if it already exists