
import sys
import calendar
from datetime import date
from holiday import get_holiday

year = 2017
month = 5
holyday_list=[d for d,name in get_holiday(year)]


end = calendar.monthrange(year,month)[1]
member = ["otsuka","shishido","kouno","kodera","qi","nakano","nishida","maezawa","oka"]


f = open("C:/Users/shishido/Desktop/labduty/foo.txt","w",encoding="utf-8")

k = 0
for i in range(1,end):
    if date(year,month,i) in holyday_list:
        continue
    if date(year,month,i).isoweekday() < 6:
        f.write(date(year,month,i).strftime("%Y/%m/%d") + ": \t" + member[(k)%9] + "\n")
        k = k + 1

f.close()


a=[]
for j in range(0,9):
    a.append(member[(k+j)%9])

member = a
print(member)
