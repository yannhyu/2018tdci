#!/usr/bin/python3

from datetime import datetime
import arrow

now = arrow.now()

print(now.shift(hours=5).time())
print(now.shift(days=5).date())

print(now.shift(years=-8).date())

string_d1 = '2018-03-01'
d1 = arrow.get(string_d1, 'YYYY-MM-DD')
d1_3_days_ago = d1.shift(days=-3).date()
print(type(d1_3_days_ago))
print(d1_3_days_ago)
print(d1_3_days_ago.strftime('%Y-%m-%d'))
