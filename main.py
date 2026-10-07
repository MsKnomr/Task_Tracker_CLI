import argparse
from view import view
from add import add
from update import update

parser = argparse.ArgumentParser(description="Task_Tracker")


parser.add_argument("--add", type=str, metavar ='', help="Input name of new task")
parser.add_argument("--desc", type=str, default="No description provided", metavar='', help="Description of task")
parser.add_argument(
    "--status", choices=["todo", "in-progress", "completed"], default="todo", metavar ='',
    help="Current status of task \n Options: ['todo', 'in-progress', 'completed']"
    )
parser.add_argument("--view", default=False, action="store_true", help="Provides a list of current tasks")
parser.add_argument("--update", type=str, metavar='', help="Update the status of an existing task")
#I added the metavar='' to each of the arguments to make the [-h] and [--help] tags print prettier

args = parser.parse_args()

save_data = "data.json"

if args.view:

    view(save_data)

if args.add:

    add(save_data, args)

if args.update:
    update(save_data, args)