import pandas as pd
from datetime import datetime

class TaskManagerWithPandas:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Title', 'Description', 'Due Date', 'Completed'])

    def add_task(self, title, description, due_date_str):
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        new_task = pd.DataFrame({
            'Title': [title],
            'Description': [description],
            'Due Date': [due_date],
            'Completed': [False]
        })
        self.df = pd.concat([self.df, new_task], ignore_index=True)

    def remove_task(self, title):
        self.df = self.df[self.df['Title'] != title]

    def mark_as_completed(self, title):
        self.df.loc[self.df['Title'] == title, 'Completed'] = True

    def mark_as_not_completed(self, title):
        self.df.loc[self.df['Title'] == title, 'Completed'] = False

    def get_pending_tasks(self):
        return self.df[self.df['Completed'] == False]

    def get_completed_tasks(self):
        return self.df[self.df['Completed'] == True]

    def __str__(self):
        return f"TaskManager with {len(self.df)} tasks"

    def display_tasks(self, tasks_df, title="Tasks", col_space=20, wrap_width=30):
        if tasks_df.empty:
            print(f"\n{title}:\n{'-' * 40}\nNo tasks found.\n")
        else:
            wrapped_df = tasks_df.copy()
            for col in wrapped_df.columns:
                wrapped_df[col] = wrapped_df[col].astype(str).apply(lambda x: self.wrap_text(x, wrap_width))
            print(f"\n{title}:\n{'-' * 40}")
            print(wrapped_df.to_string(index=False, col_space=col_space))
            print('-' * 40 + '\n')

    def wrap_text(self, text, width):
        """Wraps text to the specified width."""
        return '\n'.join(text[i:i+width] for i in range(0, len(text), width))


def main():
    task_manager = TaskManagerWithPandas()
    task_manager.add_task("Buy groceries", "Buy milk, eggs, and bread", "2024-08-06")
    task_manager.add_task("Workout", "Morning run for 30 minutes", "2024-08-06")
    task_manager.add_task("Learn Python", "Complete Python course, practice exercises, and build projects", "2024-08-10")

    while True:
        print("\nCommands:")
        print("1. Show all tasks")
        print("2. Show pending tasks")
        print("3. Show completed tasks")
        print("4. Mark a task as completed")
        print("5. Mark a task as not completed")
        print("6. Remove a task")
        print("7. Exit")
        command = input("Enter a command number: ").strip()

        if command == "1":
            task_manager.display_tasks(task_manager.df, "All Tasks")
        elif command == "2":
            task_manager.display_tasks(task_manager.get_pending_tasks(), "Pending Tasks")
        elif command == "3":
            task_manager.display_tasks(task_manager.get_completed_tasks(), "Completed Tasks")
        elif command == "4":
            title = input("Enter the title of the task to mark as completed: ").strip()
            if title in task_manager.df['Title'].values:
                task_manager.mark_as_completed(title)
                print(f"Task '{title}' marked as completed.")
            else:
                print(f"No task found with title '{title}'.")
        elif command == "5":
            title = input("Enter the title of the task to mark as not completed: ").strip()
            if title in task_manager.df['Title'].values:
                task_manager.mark_as_not_completed(title)
                print(f"Task '{title}' marked as not completed.")
            else:
                print(f"No task found with title '{title}'.")
        elif command == "6":
            title = input("Enter the title of the task to remove: ").strip()
            if title in task_manager.df['Title'].values:
                task_manager.remove_task(title)
                print(f"Task '{title}' removed.")
            else:
                print(f"No task found with title '{title}'.")
        elif command == "7":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
