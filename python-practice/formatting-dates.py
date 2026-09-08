import datetime

now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d")
print(formatted)

formatted2 = now.strftime("%B %d, %Y")
print(formatted2)