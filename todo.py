# 📂 File used for saving tasks
TASK_FILE = "tasks.txt"

# ✅ Load tasks from tasks.txt using open()
def load_tasks():
    tasks = []
    try:
        file = open(TASK_FILE, "r")  # Open file in read mode
        for line in file:
            cleaned = line.strip()   # Remove newline characters
            if cleaned:
                tasks.append(cleaned)
        file.close()
    except FileNotFoundError:
        # If file doesn't exist yet, return empty list
        pass
    return tasks

# ✅ Save tasks to tasks.txt using open()
def save_tasks(tasks):
    file = open(TASK_FILE, "w")  # Open file in write mode
    for task in tasks:
        file.write(task + "\n")
    file.close()

# ➕ Add task to list and file
def add_task(tasks):
    new_task = input("Enter a task to add: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Task added: {new_task}")
    else:
        print("⚠️ Task cannot be empty.")

# ❌ Remove a task by index
def remove_task(tasks):
    if not tasks:
        print("📭 No tasks to remove.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"❌ Removed task: {removed}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

# 📋 View all current tasks
def view_tasks(tasks):
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# 🧠 Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do App. Tasks saved.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
