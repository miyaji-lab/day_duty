import os
import sys
import calendar
from datetime import date
from holiday import get_holiday

members=[]
year = date.today().year
month = date.today().month
holyday_list=[d for d,name in get_holiday(year)]

end = calendar.monthrange(year,month)[1]
#member = ["otsuka","shishido","kouno","kodera","qi","nakano","nishida","maezawa","oka","komatsu","sugitani","terada","nishiguchi","nishino","hayashi","matsuoka","wang","fu"]

with open("MemberList.txt") as f:
    for person in f:
        members.append(person[:-1])

f = open("foo.txt","w")

k = 0
for day in range(1,end):
    if date(year,month,day) in holyday_list:
        continue
    if date(year,month,day).isoweekday() < 6:
        f.write(date(year,month,day).strftime("%Y/%m/%d") + ": \t" + members[k] + "\n")
        k =( k + 1 ) %len(members)

f.close()

a=[]
for j in range(len(members)):
    a.append(members[(k+j)%len(members)])

members = a
print(members)
