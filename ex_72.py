fname=input('Enter File Name: ')
fhandle=open(fname)
count=0
totalnum=0
for line in fhandle:
    line = line.rstrip()
    num = None
    if line.startswith('X-DSPAM-Confidence'):
        num = float(line[19:40])
        totalnum = num + totalnum
        count = count +  1
print('Average spam confidence:',totalnum/count)
