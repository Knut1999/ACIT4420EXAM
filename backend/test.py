from datetime import date, datetime, timedelta
import random
print(type(str(date.today())))
departureStr = random.choice(["11:00", "12:00", "13:00"])
departure = datetime.strptime(departureStr, "%H:%M")
departure += timedelta(hours=4.5)
print(departure.strftime("%H:%M"))
print(round(random.uniform(4.0, 5.0), 1))