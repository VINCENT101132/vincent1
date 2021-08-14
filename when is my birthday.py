import datetime
day=input('What is your next birthday')
print(day)
birthday=datetime.datetime.strptime(day,'%m/%d/%Y').date()
days=birthday-datetime.date.today()
print(days)
