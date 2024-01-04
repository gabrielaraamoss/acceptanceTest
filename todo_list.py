import json

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, *tasks):
        initial_length = len(self.tasks)
        for task in tasks:
            self.tasks.append({"description": task, "completed": False})
            print(f"Task '{task}' added successfully.")
        final_length = len(self.tasks)
        return initial_length, final_length

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['description']} - {status}")

    def mark_complete(self, task_index):
            if 1 <= task_index <= len(self.tasks):
                self.tasks[task_index - 1]["completed"] = True
            else:
                print(f"Invalid task index: {task_index}")


    def delete_task(self, index):
            if 1 <= index <= len(self.tasks):
                deleted_task = self.tasks.pop(index - 1)
                print(f"Task '{deleted_task['description']}' deleted successfully.")
                return deleted_task
            else:
                print(f"Invalid task index: {index}")
                return None
            
    def clean_tasks(self):
        self.tasks = []

    def display_tasks(self):
        tasks_text = [f"{task['description']} - {'Completed' if task['completed'] else 'Pending'}" for task in self.tasks]
        return ", ".join(tasks_text) if tasks_text else "No tasks available."

    
    def save_tasks(self, filename="tasks.json"):
            try:
                print("Tasks to be saved:", self.tasks)  
                with open(filename, 'w') as file:
                    json.dump(self.tasks, file, indent=2)  
                print(f"Tasks saved successfully to {filename}.")
            except Exception as e:
                print(f"Error saving tasks: {e}")


    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, 'r') as file:
                loaded_tasks = json.load(file)
                for task in loaded_tasks:
                    task["completed"] = True
                self.tasks = loaded_tasks
            print(f"Tasks loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"No previous tasks found in {filename}.")
        except Exception as e:
            print(f"Error loading tasks: {e}")


if __name__ == "__main__":
    todo_manager = ToDoListManager()
    todo_manager.load_tasks() 
    while True:
        print("\n1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Save tasks")
        print("6. Exit")

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
            todo_manager.save_tasks() 
        elif choice == "6":
            break
        else:
            print("Invalid option. Please select a valid option.")
