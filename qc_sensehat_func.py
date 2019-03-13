# -*- coding: utf-8 -*-
# Using SenseHat 8x8 display to show bar graph of 2 or 3 qubit Qiskit results dictionaries

# Start by importing and simplifying required modules. 
from sense_hat import SenseHat
hat = SenseHat()

# Understand which direction is down, and rotate the SenseHat display accordingly.
def set_display():
        acceleration = hat.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x=round(x,0)
        y=round(y,0)
        z=round(z,0)
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

# Defining the SenseDisplay function.
def SenseDisplay(InputDict,Qbits,back):
    # Create a default Qdict dictionary with all values 0
    global lst
    lst = [bin(x)[2:].rjust(Qbits, '0') for x in range(2**Qbits)]
    values = [0]*pow(2,Qbits)
    Qdict = dict(zip(lst,values))
    
    # Uncomment the 'back' parameter line below if you are running qiskit v0.7 or higher.
    # The local dictionary returned by Aer differs between v0.6 and v0.7+
    # The 'else' process below is made for qiskit v0.6 on the Raspberry PI,
    # with the 'if' process a workaround for v0.7 and IBM Q hardware (back = 'ibmq').
    
    # back = 'ibmq'
    
    # Update the dictionary with the actual dictionary values sent to the function.        
    if back =='ibmq': 
        k = len(InputDict)
        print(k)
        InputDictList=list(InputDict.keys())
        InputDictVal=list(InputDict.values())
        for i in range (0,k):
            Qdict[bin(int(InputDictList[i],16))[2:].zfill(Qbits)]=InputDictVal[i]
            # print(Qdict[bin(int(InputDictList[i],16))[2:].zfill(Qbits)])
    else:
        Qdict.update(InputDict)

    # Scale by dividing by 1024 (shots) - For now assuming 1024, which is set by the sh parameter.
    # Qdict.update({m: (1/sh) * Qdict[m] for m in Qdict.keys()})

    # print(InputDict)
    # print(Qdict)

    # Defining the display colors.
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    # Clear SenseHat display 
    set_display()
    hat.clear()
    
    # Writing to the SenseHat display pixels.
    for key in Qdict:
        y=7-int(key,2)
        for x in range (0,8):
                if (x*128)-Qdict[key]<0:
                        #Set bar color.
                        hat.set_pixel(x, y, red) 
                else:
                        #Set background color
                        hat.set_pixel(x, y, blue) 
       # print (Qdict[key])
       # print (int(key,2))

