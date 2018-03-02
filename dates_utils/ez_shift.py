from datetime import datetime, timedelta

start = '06/11/2013'
start = datetime.strptime(start, "%m/%d/%Y") #string to date
end = start - timedelta(days=10) # date - days
print(start, end)

def days_ago(base, n=0):
     start = datetime.strptime(base, "%Y-%m-%d") #string to date
     return (start - timedelta(days=n)).strftime('%Y-%m-%d')

print(days_ago('2018-03-01', 3))     