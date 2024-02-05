from datetime import datetime

print("The Timer program\n")

start = input("Press Enter to start...")
starttime = datetime.now()
print(f"Start time {starttime}")

stop = input("\nPress Enter to stop...")
stoptime = datetime.now()
print(f"Start time {stoptime}")

print("\nELAPSED TIME \nTime: ", stoptime - starttime)
