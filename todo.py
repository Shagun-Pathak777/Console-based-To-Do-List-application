
import os

TASK_FILE = "tasks.txt"  


def load_tasks():
    tasks = []
    if not os.path.exists(TASK_FILE):
        return tasks
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                parts = line.split("|", 1)
                if len(parts) == 2:
                    status, text = parts
                    done = status == "1"
                    tasks.append((done, text))
                else:
                    tasks.append((False, line))
    except Exception as e:
        print(f"Error reading task file: {e}")
    return tasks

def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            for done, text in tasks:
                status = "1" if done else "0"
                f.write(f"{status}|{text}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. Your list is empty.\n")
        return
    print("\nYour tasks:")
    for i, (done, text) in enumerate(tasks, start=1):
        mark = "[x]" if done else "[ ]"
        print(f"{i}. {mark} {text}")
    print()

def add_task(tasks):
    text = input("Enter new task (leave empty to cancel): ").strip()
    if not text:
        print("Add cancelled.")
        return
    tasks.append((False, text))
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove (0 to cancel): "))
    except ValueError:
        print("Invalid number.")
        return
    if idx == 0:
        print("Remove cancelled.")
        return
    if 1 <= idx <= len(tasks):
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"Removed: {removed[1]}")
    else:
        print("Task number out of range.")

def toggle_task_completion(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to toggle complete/incomplete (0 to cancel): "))
    except ValueError:
        print("Invalid number.")
        return
    if idx == 0:
        print("Operation cancelled.")
        return
    if 1 <= idx <= len(tasks):
        done, text = tasks[idx - 1]
        tasks[idx - 1] = (not done, text)
        save_tasks(tasks)
        state = "completed" if not done else "marked as not completed"
        print(f"Task '{text}' {state}.")
    else:
        print("Task number out of range.")

def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? Type 'yes' to confirm: ")
    if confirm.lower() == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks removed.")
    else:
        print("Clear cancelled.")

def show_menu():
    print("""\n===== TO-DO LIST MANAGER =====
1. View Tasks
2. Add Task
3. Remove Task
4. Toggle Complete/Incomplete
5. Clear All Tasks
6. Exit
""")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            toggle_task_completion(tasks)
        elif choice == "5":
            clear_all_tasks(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
