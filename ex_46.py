hours = input('Enter hours worked: ')
rate = input ('Enter rate: ')
h = float(hours)
r = float (rate)
def computepay(h,r):
    if h<=40:
        pass
        pay = h * r
        return pay
    else:
        extra = ((h-40)/2)+(h-40)
        pay = (40*r) + (extra*r)
        return pay
print(computepay(h,r))
