from dataclasses import dataclass
import datetime


@dataclass
class Countdown:
    target_datetime: datetime

    @property
    def time_left(self):
        return self.target_datetime - current_datetime

    @property
    def is_expired(self):
        if current_datetime > self.target_datetime:
            return True
        else:
            return False


current_datetime = datetime.datetime.now()

target_datetime1 = datetime.datetime(2024, 2, 16, 11, 0)
target_datetime2 = datetime.datetime(2025, 1, 1, 0, 0)
target_datetime3 = datetime.datetime(2023, 9, 30, 20, 0)

countdown1 = Countdown(target_datetime1)
countdown2 = Countdown(target_datetime2)
countdown3 = Countdown(target_datetime3)

print(countdown1.time_left)
print(countdown1.is_expired)
print()

print(countdown2.time_left)
print(countdown2.is_expired)
print()

print(countdown3.time_left)
print(countdown3.is_expired)
