hours = input('Enter hours: ')
rate = input('Enter rate: ')
h = float(hours)
r = float(rate)
if h<=40:
    pass
    pay =h*r
else:
    overtime = h - 40
    newrate = r*1.5
    pay = (40*r)+(overtime*newrate)
print(pay)
