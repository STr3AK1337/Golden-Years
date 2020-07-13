import calendar
import datetime

cal = calendar.Calendar()
numList = []

for x in cal.itermonthdays(2020, 2):
    numList.append(x)
    
current = datetime.datetime.now()
y = current.year
m = current.month

print(calendar.month(y, m)) 
