counts = dict()
#fname = input("Enter file name: ")
fhandle = open("mbox-short.txt")
for line in fhandle:
    if line.startswith("From "):
        words=line.split()
        email = words[1]
        counts[email]=counts.get(email,0)+1
print(counts)

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
