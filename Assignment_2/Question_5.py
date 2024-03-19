from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    task_name: str = ''
    task_description: str = ''
    due_date: datetime = datetime(1, 1, 1)

    def status(self):
        # Changes result of the task depending on the date input and the date now
        if datetime.now() > self.due_date:
            return "Completed"
        else:
            return "Pending"


@dataclass
class Homework(Task):
    subject: str = ''
    task_status: str = 'Not Started.'

    def status(self):
        # Changes the status of the task to be homework
        # If task_status has not been changed it returns not started if the day has not been passed.
        if datetime.now() > self.due_date:
            return "Completed"
        else:
            return self.task_status


@dataclass
class Meeting(Task):
    location: str = ''

    def status(self):
        if datetime.now() > self.due_date:
            return "Happened"
        else:
            return "Scheduled"


homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2023, 10, 15), "Math")
meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2024, 9, 20), "Office A")

print("Homework:")
print("Task Name:", homework.task_name)
print("Task Description:", homework.task_description)
print("Due Date:", homework.due_date)
print("Subject:", homework.subject)
print("Status:", homework.status())

print()

print("Meeting:")
print("Task Name:", meeting.task_name)
print("Task Description:", meeting.task_description)
print("Due Date:", meeting.due_date)
print("Location:", meeting.location)
print("Status:", meeting.status())
