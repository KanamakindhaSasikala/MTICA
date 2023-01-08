import datetime
ob=datetime.datetime.now()
print(type(ob))
print("_"*25)
print(ob)
print(ob.year)
print(ob.month)
print(ob.day)
print(ob.hour)
print(ob.minute)
print(ob.second)
str1=str(ob.hour)+':'+str(ob.minute)+':'+str(ob.second)
print(str1)
print("_"*25)
print("1 week ago it was:",ob-datetime.timedelta(weeks=1))
print("100 days ago it was:",  ob-datetime.timedelta(days=100))
print("1 week from now it will be:",ob+datetime.timedelta(weeks=1))
print("1000 days later it will be:",ob+datetime.timedelta(days=100))
bday_sasikala=datetime.datetime(1999,12,17)
print("_"*25)
print("Birthday in ....",ob-bday_sasikala)
print("_"*25)

 '''
output:
==================
<class 'datetime.datetime'>
_________________________
2023-01-08 12:17:12.784575
2023
1
8
12
17
12
12:17:12
_________________________
1 week ago it was: 2023-01-01 12:17:12.784575
100 days ago it was: 2022-09-30 12:17:12.784575
1 week from now it will be: 2023-01-15 12:17:12.784575
1000 days later it will be: 2023-04-18 12:17:12.784575
_________________________
Birthday in .... 8423 days, 12:17:12.784575
