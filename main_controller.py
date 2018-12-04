from sense_hat import SenseHat
 
hat = SenseHat()

hat.show_message("Load")

import bell_calling_sense_func
import GHZ_calling_sense_func

hat.show_message("OK")


hat.clear()
hat.low_light = True
hat.set_rotation(180)



while True:
    joy_event = hat.stick.get_events()
    if len(joy_event) > 0 and joy_event[0][2]=="pressed":
        # print (joy_event[0][1])
        # hat.show_message(joy_event[0][1])
        if joy_event[0][1]=="up":
            hat.show_message("Bell")
            bell_calling_sense_func.execute()
        else:
            if joy_event[0][1]=="down":
                hat.show_message("GHZ")
                GHZ_calling_sense_func.execute()
            else:
                if joy_event[0][1]=="left":
                    hat.show_message("L")
                else:
                    if joy_event[0][1]=="right":
                        hat.show_message("R")
        


# Works one time. Need to figure out how to restart.