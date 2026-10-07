import json

def update(save_data, args):
    with open(save_data, "r+") as file:
        tasks = json.load(file)
        for task in tasks:
            if task["task name"] == args.update:
                task["status"] = args.status
                task["description"] = args.desc
        file.seek(0)
        file.truncate()
        json.dump(tasks, file, indent=4)
        print(f"'{args.update}' successfully updated!")
                