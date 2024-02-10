# def create_date(dd,mm,year):
#     print(f"{dd}/{mm}/{year}")


  




# dd,mm,year=map(int,input().split())
# create_date(dd,mm,year)
from datetime import datetime

def Create_date(day_num, month_num, year_num):
    # Create a datetime object using the given day, month, and year
    date = datetime(year=year_num, month=month_num, day=day_num)
    return date

# Example usage:
day_num = 1
month_num = 1
year_num = 2000

date_object = Create_date(day_num, month_num, year_num)
print(date_object)  # Output: 2000-01-01 00:00:00

# If you want to format the output as "01/01/2000"
formatted_date = date_object.strftime('%d/%m/%Y')
print(formatted_date)  # Output: 01/01/2000
