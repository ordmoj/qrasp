# -*- coding: utf-8 -*-
# Qiskit
# Example of Bell, or entangled, states
from sense_hat import SenseHat
hat = SenseHat()

# Create SenseHat Display function

def set_display():
        acceleration = hat.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x=round(x,0)
        y=round(y,0)
        z=round(z,0)
        print("x={0}, y={1}, z={2}".format(x,y,z))
        if x == 1:
            hat.set_rotation(180)
        else:
            if x == -1:
                hat.set_rotation(0)
            else:
                if y == 1:
                    hat.set_rotation(270)
                else:
                    hat.set_rotation(90)


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
    set_display()
    for key in Qdict:
        y=7-int(key,2)
        for x in range (0,8):
                if (x*128)-Qdict[key]<0:
                        hat.set_pixel(x, y, red)
                else:
                        hat.set_pixel(x, y, blue)
       # print (Qdict[key])
       # print (int(key,2))

