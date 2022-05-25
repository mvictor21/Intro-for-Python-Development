from datetime import datetime, timedelta
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print("Today is " + str(today))
print("Yesterday was " + str(yesterday))