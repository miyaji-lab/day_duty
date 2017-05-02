import os
import sys
import calendar
from datetime import date
from holiday import get_holiday

def const_members(count,list):
    return list[count:]+list[:count]

def text_gen(f,members):
    year = date.today().year
    month = date.today().month
    end = calendar.monthrange(year,month)[1]
    holyday_list=[d for d,name in get_holiday(year)]

    k = 0
    for day in range(1,end):
        if date(year,month,day) in holyday_list:
            continue
        if date(year,month,day).isoweekday() < 6:
            f.write(date(year,month,day).strftime("%Y/%m/%d") + ": \t" + members[k] + "\n")
            k =( k + 1 ) %len(members)
    return f,k

def memberlist_gen(f,members):
    for i,v in enumerate (members):
        f.write(v+"\n")
    return f


members=[]

with open("MemberList.txt") as f:
    for person in f:
        members.append(person[:-1])

f,k=text_gen(open("list.txt","w"),members)

f.close()

members=const_members(k,members)

f = memberlist_gen(open("MemberList.txt","w"),members)

f.close()
