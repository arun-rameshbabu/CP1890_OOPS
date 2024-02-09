from datetime import datetime, date, time, timedelta

datetime_now = datetime.now()
halloween = ("2024-10-31")
halloween2 = datetime.strptime(halloween, "%Y-%m-%d")

date2 = str(halloween2 - datetime_now)
date2 = date2.split(',')
date1 = date2[0].removesuffix("s")

print(f"{date1}(s)")

print(type(datetime_now))