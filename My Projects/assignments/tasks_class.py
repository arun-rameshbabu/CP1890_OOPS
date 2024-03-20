from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    task_name: str = ''
    task_description: str = ''
    due_date: datetime = None

    def status(self):
        