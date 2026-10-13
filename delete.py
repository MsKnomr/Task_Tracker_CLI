import json

def delete(save_data, args):
    deleted = False
    current_index = 0
    with open(save_data, "r+") as file:
        tasks = json.load(file)
        task_index = 0
        for task in tasks:   
            if task["task name"] == args.delete or args.delete == str(task["id"]):
                #argparse will always return a string while the data.json file stores it as an int 
                #convertion to string is necessary for bool to eval True 
                del tasks[task_index]
                file.seek(0)
                file.truncate()
                json.dump(tasks, file, indent=4)
                deleted = True
            task_index += 1
    if deleted == True:
        print(f"'{args.delete}' successfully deleted")
    else:
        print("Task not found")
