fname = input("Enter file name: ")
fhandle=open(fname)
listwords=[]
for line in fhandle:
    rline=line.rstrip()
    words = rline.split()
    for word in words:
        if word not in listwords:
            listwords.append(word)
listwords.sort()
print(listwords)
