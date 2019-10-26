import re
num=list()
fhandle=open('regex_sum_244355.txt')
for line in fhandle:
    words=line.split()
    for word in words:
        numbers=re.findall('[0-9]+',word)
        if len(numbers)<1: continue
        elif len(numbers)>1:
            for i in numbers:
                s=float(i)
                num.append(s)
        else:
            newnumb=float(numbers[0])
            num.append(newnumb)
print(sum(num))
