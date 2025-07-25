from datetime import datetime, timedelta
now = datetime.now()
print("Current date and time:", now)

# this will extract exact time and date, real time date and time
print("Year:",now.year)
print("Month:",now.month)
print("Day:", now.day)
print("Hour:",now.hour)

future_date = now + timedelta(days = 10)
print("The date after 10 days: ", future_date)