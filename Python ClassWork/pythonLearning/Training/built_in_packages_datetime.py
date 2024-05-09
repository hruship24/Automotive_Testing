import datetime

dob = datetime.date(year=2000,month=10,day=4)
current_date= datetime.date(2024,4,24)
current = datetime.datetime.now().date()
print(current)

age = (current_date - dob).days//365
print('Age is ',age)


tomorrow = current + datetime.timedelta(days=1)
print('Tomorrow : ',tomorrow)

now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print('Formatted_date : ',formatted_date)

date_string = "2024-04-24 08:30:25"
parsed_date = datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print(parsed_date)

print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%H:%M:%S"))
