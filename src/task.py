from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str
    created_at: datetime
    is_completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as complete. Return: None (procedure)."""
        self.is_completed = True