import json
from typing import List
from task import Task

class TaskRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_tasks(self, tasks: List[Task]) -> None:
        """Guarda uma lista de tarefas no ficheiro JSON."""
        tasks_data = []
        for task in tasks:
            tasks_data.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "created_at": task.created_at.isoformat(),
                "is_completed": task.is_completed
            })
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(tasks_data, f, indent=4, ensure_ascii=False)