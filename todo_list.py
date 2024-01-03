class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, *tasks):
        for task in tasks:
            self.tasks.append({"description": task, "completed": False})
            print(f"Task '{task}' added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['description']} - {status}")

    def mark_task_completed(self, *task_descriptions):
        for task_description in task_descriptions:
            for task in self.tasks:
                if task["description"] == task_description:
                    task["completed"] = True
                    print(f"Task '{task_description}' marked as completed.")
                    break
            else:
                print(f"Task '{task_description}' not found.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared successfully.")


if __name__ == "__main__":
    todo_manager = ToDoListManager()
    while True:
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            tasks = input("Enter task descriptions (comma-separated): ").split(',')
            todo_manager.add_task(*tasks)
        elif choice == "2":
            todo_manager.list_tasks()
        elif choice == "3":
            task_descriptions = input("Enter task descriptions to mark as completed (comma-separated): ").split(',')
            todo_manager.mark_task_completed(*task_descriptions)
        elif choice == "4":
            todo_manager.clear_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please select a valid option.")
