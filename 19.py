'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import date
from datetime import datetime
from datetime import timedelta

count=0
start_date=date(1900,12,30)
end_date=date(2000,12,31)
print start_date, start_date.weekday()


while True :
  start_date+=timedelta(days=7)
  #print start_date, start_date.weekday(), start_date.day
  if (start_date.weekday()==6) and (start_date.day==1) : count+=1
  if start_date >= end_date : break

print start_date
print count