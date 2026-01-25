from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H:%M:%S")

print("Formatted date:", formatted_date)
print("Formatted time:", formatted_time)