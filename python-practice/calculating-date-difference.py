import datetime

date1 = datetime.datetime(2023, 1, 1)
date2 = datetime.datetime(2023, 12, 31)

difference = date2 - date1
print(difference)
print("Days:", difference.days)