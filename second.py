from datetime import datetime
def Create_date(name,reg_num,dd,mm,year):
  date=datetime(day=dd,month=mm,year=year)
  formated=date.strftime('%d/%m/%Y')
  print(name,reg_num,formated)
  
  
name=input()
reg_num=int(input())
dd,mm,year=map(int,input().split())
Create_date(name,reg_num,dd,mm,year)