from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    name: str = ''
    location: str = ''
    start_date: datetime = datetime(1, 1, 1)
    end_date: datetime = datetime(1, 1, 1)

    def duration(self):
        # Calculates the amount of days of the event
        time = (self.end_date-self.start_date).days
        return time


@dataclass
class Conference(Event):
    attendees: int = 0

    def duration(self):
        # Changes the amount of days into the amount of hours of the conference
        return Event.duration(self) * 24


event = Event("Birthday Party", "New York", datetime(2023, 8, 25),
              datetime(2023, 8, 26))
conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9, 15),
                        datetime(2023, 9, 17), 500)

print("Event:")
print("Name:", event.name)
print("Location:", event.location)
print("Start Date:", event.start_date)
print("End Date:", event.end_date)
print("Duration (days):", event.duration())

print()

print("Conference:")
print("Name:", conference.name)
print("Location:", conference.location)
print("Start Date:", conference.start_date)
print("End Date:", conference.end_date)
print("Attendees:", conference.attendees)
print("Duration (hours):", conference.duration())
