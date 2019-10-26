fname = input('Enter file name: ')
fhandle = open(fname)
count = 0
for line in fhandle:
    rline = line.rstrip()
    if rline.startswith('From '):
        email = line.split()
        count = count + 1
        print(email[1])
print('There were',count,'lines in the file with From as the first word')
