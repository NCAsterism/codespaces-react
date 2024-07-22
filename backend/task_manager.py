import csv
from datetime import datetime

class TaskManager:
    def __init__(self, file_name='tasks.csv'):
        self.file_name = file_name

    def load_tasks(self):
        tasks = []
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(row)
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self, tasks):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['task', 'priority', 'deadline', 'mode'])
            writer.writeheader()
            writer.writerows(tasks)

    def add_task(self, task, priority, deadline, mode):
        tasks = self.load_tasks()
        tasks.append({'task': task, 'priority': priority, 'deadline': deadline, 'mode': mode})
        self.save_tasks(tasks)

    def get_next_task(self, mode):
        tasks = [task for task in self.load_tasks() if task['mode'] == mode]
        if not tasks:
            return None
        tasks.sort(key=lambda x: (x['priority'], datetime.strptime(x['deadline'], '%Y-%m-%d')))
        return tasks[0]

# Example usage:
if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task('Complete project report', 'High', '2024-07-25', 'work')
    manager.add_task('Meditate', 'Low', '2024-07-22', 'relax')
    next_task = manager.get_next_task('work')
    print(f"Next task: {next_task['task']}" if next_task else "No tasks available")
