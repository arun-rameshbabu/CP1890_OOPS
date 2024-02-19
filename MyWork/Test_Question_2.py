from datetime import datetime


class Countdown:
    def __init__(self, date: datetime):
        """
        This function initializes the class attribute.
        :param date: datetime object
        """
        self.datetime = date

    @property
    def time_left(self):
        """
        This function returns the time left between the datetime and the current date, without microseconds.
        :return:
        """
        return self.datetime - (datetime.now().replace(microsecond=0))

    @property
    def is_expired(self):
        """
        This function checks if the datetime is before the current date.
        :return: Bool value for whether the datetime is before the current date or not.
        """
        if self.datetime < datetime.now():
            return True
        else:
            return False


def main():
    """
    Test values for class.
    """
    target_datetime1 = datetime(2024, 2, 16, 10, 0)
    target_datetime2 = datetime(2025, 1, 1, 0, 0)
    target_datetime3 = datetime(2024, 1, 30, 20, 0)

    countdown1 = Countdown(target_datetime1)
    countdown2 = Countdown(target_datetime2)
    countdown3 = Countdown(target_datetime3)

    print("countdown1 = Countdown(target_datetime1)")
    print("countdown2 = Countdown(target_datetime2)\ncountdown3 = Countdown(target_datetime3)\n")

    print(countdown1.time_left)
    print(countdown1.is_expired, "\n")

    print(countdown2.time_left)
    print(countdown2.is_expired, "\n")

    print(countdown3.time_left)
    print(countdown3.is_expired, "\n")


if __name__ == '__main__':
    main()
