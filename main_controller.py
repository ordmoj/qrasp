from sense_hat import SenseHat
 
hat = SenseHat()

hat.clear()
hat.low_light = True

def set_display():
        acceleration = hat.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x=round(x,0)
        y=round(y,0)
        z=round(z,0)
        #print("x={0}, y={1}, z={2}".format(x,y,z))
        if x == 1:
            hat.set_rotation(270)
        else:
            if x == -1:
                hat.set_rotation(90)
            else:
                if y == 1:
                    hat.set_rotation(0)
                else:
                    hat.set_rotation(180)

set_display()                

hat.show_message("Load")

import bell_calling_sense_func
import q2_calling_sense_func
import q3_calling_sense_func
import GHZ_calling_sense_func

hat.show_message("OK")


while True:
    joy_event = hat.stick.get_events()
    if len(joy_event) > 0 and joy_event[0][2]=="pressed":
        # print (joy_event[0][1])
        # hat.show_message(joy_event[0][1])
        set_display()
        if joy_event[0][1]=="up":
            hat.show_message("Bell")
            bell_calling_sense_func.execute()
        else:
            if joy_event[0][1]=="down":
                hat.show_message("GHZ")
                GHZ_calling_sense_func.execute()
            else:
                if joy_event[0][1]=="left":
                    hat.show_message("2Q")
                    q2_calling_sense_func.execute()
                else:
                    if joy_event[0][1]=="right":
                        hat.show_message("3Q")
                        q3_calling_sense_func.execute()


# Works one time. Need to figure out how to restart.