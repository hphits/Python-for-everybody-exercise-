largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = fnum
    elif largest < fnum:
        largest = fnum
    if smallest is None:
        smallest = fnum
    elif smallest > fnum:
        smallest=fnum
    if num == "done" :
            break
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
