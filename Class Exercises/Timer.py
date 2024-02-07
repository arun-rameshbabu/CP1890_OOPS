from datetime import datetime


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
    minutes = elapsed.seconds
    seconds = elapsed.seconds
    microseconds = elapsed.microseconds

    hours = minutes // 60
    minutes = minutes % 60

    print("\nELAPSED TIME \nTime: ", end="")
    if days > 0:
        print(f"{days}/", end="")
    print(f"{hours}/{minutes}/{seconds}/{microseconds}")


if __name__ == "__main__":
    main()
