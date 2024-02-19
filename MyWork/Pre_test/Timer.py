from datetime import datetime, time


def main():
    print("The Timer program\n")

    # Start timer
    input("Press Enter to start...")
    start = datetime.now()
    print(f"Start time: {start}")

    # Stop timer
    input("\nPress Enter to stop...")
    stop = datetime.now()
    print(f"Stop time:  {stop}")

    # Difference
    elapsed = stop - start
    days = elapsed.days
    minutes = elapsed.seconds // 60
    seconds = elapsed.seconds % 60
    microseconds = elapsed.microseconds

    hours = minutes // 60
    minutes = minutes % 60

    time_ob = time(hours, minutes, seconds, microseconds)

    print("\nELAPSED TIME \nTime: ", end="")
    if days > 0:
        print(f"{days}:", end="")
    print(f"{time_ob}")


if __name__ == "__main__":
    main()
