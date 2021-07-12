bitstring=(input())
data=list(bitstring)
i=0
c=0
while i<len(data):
    if data[i]=='1':
        c+=1
    else:
        c=0
    if c==6:
        data.insert(i,'0')
        c=0
    i+=1
x=''
x=''.join(data)
print(x)