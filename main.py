import argparse
from view import view
from add import add
from update import update
from delete import delete
from refresh import refresh

parser = argparse.ArgumentParser(description="Task_Tracker")


parser.add_argument("--add", type=str, metavar ='', help="Input name of new task")
parser.add_argument("--desc", type=str, default="No description provided", metavar='', help="Description of task")
parser.add_argument(
    "--status", choices=["todo", "in-progress", "completed"], default="todo", metavar ='',
    help="Current status of task. \n Options: ['todo', 'in-progress', 'completed']"
    )
parser.add_argument(
    "--view", choices=["todo", "in-progress", "completed", "None"], nargs="?", const="None", 
    metavar='STATUS', help="Provides a list of current tasks based on their status, or all tasks if no argument is given"
    )
    #'nargs="?"' allows --view to be placed with either 0 or 1 positional arguments
    #If there are no positional arguments following --view then the const value is placed ("None")
parser.add_argument("--update", type=str, metavar='', help="Update the status of an existing task")
parser.add_argument("--delete", type=str, metavar='', help="Delete a task from the list")
parser.add_argument("--refresh", action="store_true", help="Refresh all task 'id's ")

#I added the metavar='' to each of the arguments to make the [-h] and [--help] tags print prettier

args = parser.parse_args()

save_data = "data.json"

if args.view:

    view(save_data, args)

if args.add:

    add(save_data, args)

if args.update:

    update(save_data, args)

if args.delete:
    
    delete(save_data, args)

if args.refresh:

    refresh(save_data)