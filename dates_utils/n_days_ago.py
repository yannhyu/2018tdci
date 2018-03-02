from datetime import datetime, timedelta

N = 2

date_N_days_ago = datetime.now() - timedelta(days=N)

print(datetime.now())
print(type(datetime.now()))
print(date_N_days_ago)

N = 3
string_date = '2018-03-01'
dt_string_date = datetime.strptime(string_date, "%Y-%m-%d")
dt_N_days_ago = dt_string_date - timedelta(days=N)
print(dt_N_days_ago)
print(dt_N_days_ago.strftime('%Y-%m-%d'))


