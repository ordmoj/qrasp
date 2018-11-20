# -*- coding: utf-8 -*-
# Qiskit
# Example of Bell, or entangled, states
from sense_hat import SenseHat
hat = SenseHat()

# Create SenseHat Display function

def SenseDisplay(InputDict,Qbits):
    #Create a default dictionary with all values 0
    global lst
    lst = [bin(x)[2:].rjust(Qbits, '0') for x in range(2**Qbits)]
    values = [0]*pow(2,Qbits)
    #print(values)
    #print(lst)
    Qdict = dict(zip(lst,values))
    # Update the dictionary with the actual values
    Qdict.update(InputDict)
    #Scale by dividing by 1024 (shots)
    #Qdict.update({m: (1/sh) * Qdict[m] for m in Qdict.keys()})
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    # examples using (x, y, pixel)
    hat.clear()
    #hat.set_pixel(0, 0, red)
    #hat.set_pixel(0, 0, green)
    #hat.set_pixel(0, 0, blue)
    for key in Qdict:
        y=7-int(key,2)
        for x in range (0,8):
                if (x*128)-Qdict[key]<0:
                        hat.set_pixel(x, y, red)
                else:
                        hat.set_pixel(x, y, blue)
       # print (Qdict[key])
       # print (int(key,2))

