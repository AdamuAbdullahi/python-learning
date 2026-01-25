from datetime import datetime
import time

try:
    while True:
        now = datetime.now()
        Current_time = now.strftime("%H:%M:%S")
        print("Current Time:", Current_time)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped. Goodbye!")