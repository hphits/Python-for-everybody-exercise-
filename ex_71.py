fname=input('enter file name: ')
fhandle=open(fname)
fread=fhandle.read()
textupper=fread.upper()
print(textupper.rstrip())
