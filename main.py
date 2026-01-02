import argparse
import json
import os
import uuid

if not os.path.exists("tasks.json"):
    with open("tasks.json", "x") as f:
        f.write("{}")

f = open('tasks.json')
tasks = json.load(f)

parser = argparse.ArgumentParser(prog="task-cli", description="Manage your tasks on your terminal")
subparsers = parser.add_subparsers(dest="command", required=True)

parser_add = subparsers.add_parser("add", help="Add a new task.")
parser_add.add_argument("name", help="The name of your task.")

parser_update = subparsers.add_parser("update", help="Update an existing task.")
parser_update.add_argument("id", help="The id of the task you want to update.")
parser_update.add_argument("update", help="Your updated task.")

parser_delete = subparsers.add_parser("delete", help="Delete an existing task.")
parser_delete.add_argument("id", help="The id of the task you want to delete.")

parser_progress = subparsers.add_parser("mark-in-progress", help="Mark your task as 'in progress'.")
parser_progress.add_argument("id", help="The id of the task you want to mark as 'in progress'.")

parser_done = subparsers.add_parser("mark-done", help="Mark your task as 'done'.")
parser_done.add_argument("id", help="The id of the task you want to mark as 'done'.")

parser_list = subparsers.add_parser("list", help="List all of your tasks.")

args = parser.parse_args()

match args.command:
    case "add":
        tasks[f"{uuid.uuid4()}"] = {"name" : args.name, "progress" : "todo"}
    case "update":
        tasks[args.id]["name"] = args.update
    case "delete":
        tasks.pop(args.id)
    case "mark-in-progress":
        tasks[args.id]["progress"] = "in progress"
    case "mark-done":
        tasks[args.id]["progress"] = "done"
    case "list":
        for id in tasks:
            print(f"id: {id} | name: {tasks[id]["name"]} | progress: {tasks[id]["progress"]}")

with open('tasks.json', 'w', encoding='utf-8') as f:
    json.dump(tasks, f, ensure_ascii=False, indent=4)