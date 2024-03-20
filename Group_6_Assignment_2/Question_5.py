"""
Assignment 2

Question 5
"""

from Classes import Homework, Meeting
from datetime import datetime

homework_date = datetime.now()
meeting_date = datetime(2024, 9, 20)

homework = Homework("Science Homework", "Complete excersizes 2-7", homework_date, "Science")
meeting = Meeting("Group Meeting", "Discuss Project Updates", meeting_date, "Office B")

print("Homework:")
print("Task Name:", homework.task_name)
print("Task Description:", homework.task_description)
print("Due Date:", homework.due_date)
print("Subject:", homework.subject)
print("Status:", homework.status())

print("\n")

print("Meeting:")
print("Task Name:", meeting.task_name)
print("Task Description:", meeting.task_description)
print("Due Date:", meeting.due_date)
print("Location:", meeting.location)
print("Status:", meeting.status())
