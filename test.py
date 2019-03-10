#Test

InputDict = {'0x0': 254, '0x1': 227, '0x2': 282, '0x3': 261}
Qbits=2
InputDictList=list()

lst = [bin(x)[2:].rjust(Qbits, '0') for x in range(2**Qbits)]
values = [0]*pow(2,Qbits)
Qdict = dict(zip(lst,values))
    
k = len(InputDict)
print(k)
InputDictList=list(InputDict.keys())
InputDictVal=list(InputDict.values())

#print(InputDictList)
#print(InputDictList[1])
#print(bin(int(InputDictList[1],16))[2:])
#print(InputDict)
#print(Qdict)

for i in range (0,k):
    print(bin(int(InputDictList[i],16))[2:].zfill(2))
    print(Qdict[bin(int(InputDictList[i],16))[2:].zfill(2)])
    Qdict[bin(int(InputDictList[i],16))[2:].zfill(2)]=InputDictVal[i]
    print(Qdict[bin(int(InputDictList[i],16))[2:].zfill(2)])

    
print(Qdict)