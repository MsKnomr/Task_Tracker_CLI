# Task_Tracker_CLI

A simple CLI tool that stores a task and its status in a list.

## Features

- Creates and modifies a .json document to store task information
- Tasks can be assigned a name, status, and description
- Tasks receive an identification number automatically
- View all current tasks, or filter to view tasks with a specific status
- Refer to a task by its name or ID in order to modify or delete that task
- Refresh you task IDs to keep them in order (if desired)

## Usage

### Add new task

`python3 main.py --add "Example Task" --desc "This is an example." --status "in-progress"`

### Modify existing task

`python3 main.py --update "Example Task" --status "completed"`

### View all tasks

`python3 main.py --view`

### View in-progress tasks

`python3 main.py --view "in-progress"`

### Delete an existing task

`python3 main.py --delete "Example Task"`

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `--add` | Add a new task to the list | required |
| `--status` | **Requires `--add`**; Task status (`todo` / `in-progress` / `completed`) | todo |
| `--desc` | **Requires `--add`**; Task description | "No description provided" |
| `--update` NAME_OR_ID | **Requires `--status` or `--desc`**; Update an existing task | required |
| `--delete` NAME_OR_ID | Delete an existing task | required |
| `--refresh` | Refresh all task IDs | false |

Project Idea provided by: https://roadmap.sh/projects/task-tracker