"""
Assignment 2

Question 4
"""

from Classes import Event, Conference
from datetime import datetime

event = Event('Birthday Party', 'New York', datetime(2023, 8, 25),
              datetime(2023, 8, 26))

print('Event')
print('Name:', event.name)
print('Location:', event.location)
print('Start Date:', event.start_date)
print('End Date:', event.end_date)
print('Duration (days):', event.duration())

print("\n")

conference = Conference('Tech Conference', 'San Francisco', datetime(2023, 9, 15), datetime(2023, 9, 17), 500)

print('Conference')
print('Name:', conference.name)
print('Location:', conference.location)
print('Start Date:', conference.start_date)
print('End Date:', conference.end_date)
print('Attendees:', conference.attendees)
print('Duration (hours):', conference.duration())
