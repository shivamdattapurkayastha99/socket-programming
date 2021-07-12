
def stuff(sig):
    onec = 0  
    c = 0   
    one = []  
    s = list(sig)
    for i in s:
        c += 1
        if i == '0':
            onec = 0
        else:
            onec += 1
        if onec == 5:
            one.append(c)
            onec = 0
    k = 0  
    for i in one:
        
        s.insert(i + k, '0')
        k += 1
    return s



def destuff(sig):
    onec = 0  
    c = 0   
    one = []  
    sig = list(sig)
    for i in sig:
        c += 1
        if i == '0':
            onec = 0
        else:
            onec += 1
        if onec == 5:
            one.append(c)
            onec = 0
    k = 0  
    for i in one:
        
        sig.pop(i + k)
        k -= 1
    return sig



sig = input("Enter the signal: ")
print("Original Signal : ", sig)

stf = stuff(sig)
print("Stuffed Signal : ", end="")
print("".join([x for x in stf]))

dstf = destuff(stf)
print("Destuffed Signal : ", end="")
print("".join([x for x in dstf]))