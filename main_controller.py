# Main controller for Qiskit on Raspberry PI SenseHat.

# Start by importing and simplifying required modules. 
from sense_hat import SenseHat
#from sense_emu import SenseHat
hat = SenseHat()
import time

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

#Check if online
from urllib.request import urlopen

def internet_on():
    try:
        response = urlopen('https://www.google.com', timeout=10)
        return True
    except:
        return False

#Import Qiskit classes
from qiskit import IBMQ, execute
from qiskit import BasicAer as Aer #<-Workaround
import Qconfig_IBMQ_experience
# from qiskit.tools.monitor import job_monitor
print("Getting provider...")
if not IBMQ.active_account():
    if internet_on():
        #IBMQ.enable_account(Qconfig_IBMQ_experience.APItoken)
        IBMQ.load_account()
        provider = IBMQ.get_provider()
    else:
        hat.show_message("Offline mode")

# Set default SenseHat configuration.
hat.clear()
hat.low_light = True

# Background icon
X = [255, 0, 255]  # Magenta
Y = [255,192,203] # Pink
P = [255,255,0] #Yellow
O = [0, 0, 0]  # Black
B = [0,0,255] # Blue
#B = [70,107,176] # IBM Blue
W = [255, 255, 255] #White

super_position = [
O, O, O, Y, X, O, O, O,
O, O, Y, X, X, Y, O, O,
O, Y, O, O, X, O, Y, O,
O, Y, O, O, X, O, Y, O,
O, Y, O, O, X, O, Y, O,
O, Y, O, O, X, O, Y, O,
O, O, Y, O, X, Y, O, O,
O, O, O, X, X, X, O, O
]

IBMQ_super_position = [
O, O, O, Y, B, O, O, O,
O, O, Y, B, B, Y, O, O,
O, Y, O, O, B, O, Y, O,
O, Y, O, O, B, O, Y, O,
O, Y, O, O, B, O, Y, O,
O, Y, O, O, B, O, Y, O,
O, O, Y, O, B, Y, O, O,
O, O, O, B, B, B, O, O
]


IBM_Q = [
B, B, B, W, W, B, B, B,
B, B, W, B, B, W, B, B,
B, W, B, B, B, B, W, B,
P, P, P, B, B, B, W, B,
B, W, P, B, B, B, W, B,
P, P, P, B, B, W, B, B,
P, B, B, W, W, B, B, B,
P, P, P, W, W, W, B, B
]

IBM_Q_4 = [
B, B, B, W, W, B, B, B,
B, B, W, B, B, W, B, B,
B, W, B, B, B, B, W, B,
P, W, P, B, B, B, W, B,
P, W, P, B, B, B, W, B,
P, P, P, B, B, W, B, B,
B, B, P, W, W, B, B, B,
B, B, P, W, W, W, B, B
]

IBM_Q_B = [
B, B, B, W, W, B, B, B,
B, B, W, B, B, W, B, B,
B, W, B, B, B, B, W, B,
B, W, B, B, B, B, W, B,
B, W, B, B, B, B, W, B,
B, P, W, B, B, W, B, B,
P, P, P, W, W, B, B, B,
B, P, B, W, W, W, B, B
]




IBM_AER = [
O, O, W, W, W, W, O, O,
O, W, W, O, O, W, W, O,
W, W, W, O, O, W, W, W,
W, W, O, W, W, O, W, W,
W, W, O, O, O, O, W, W,
W, O, W, W, W, W, O, W,
O, W, O, O, O, O, W, O,
O, O, W, W, W, W, O, O
]
         

# Function to set the backend
def set_backend(back):
    from qiskit.providers.ibmq import least_busy
    global backend
    if back == "ibmq" and internet_on():
        hat.show_message("Getting best backend...")
        backend = least_busy(provider.backends(n_qubits=5, operational=True, simulator=False))
        hat.show_message(backend.name())
        status = backend.status()
        is_operational = status.operational
        jobs_in_queue = status.pending_jobs
        hat.show_message(str(jobs_in_queue))
        hat.set_pixels(IBM_Q_B)
    else:
        backend = Aer.get_backend('qasm_simulator')
        hat.show_message(backend.name())
        hat.set_pixels(IBM_AER)
    print(backend.name)                
    
# Load the Qiskit function files. Showing messages when starting and when done.
hat.show_message("Qiskit")

import q2_calling_sense_func
import q3_calling_sense_func
import bell_calling_sense_func
import GHZ_calling_sense_func
#import set_backend

# Initialize the backend to AER
back = "aer" 
set_backend(back)


# The main loop.
# Use the joystick to select and execute one of the Qiskit function files.

while True:
    joy_event = hat.stick.get_events()
    if len(joy_event) > 0 and joy_event[0][2]=="pressed":
        set_display()
        if joy_event[0][1]=="up":
            hat.show_message("Bell")
            if back != "aer"and internet_on():
                hat.set_pixels(IBMQ_super_position)
            else:
                hat.set_pixels(super_position)
            bell_calling_sense_func.execute(backend,back)
        else:
            if joy_event[0][1]=="down":
                hat.show_message("GHZ")
                if back != "aer" and internet_on():
                    hat.set_pixels(IBMQ_super_position)
                else:
                    hat.set_pixels(super_position)
                GHZ_calling_sense_func.execute(backend,back)
            else:
                if joy_event[0][1]=="left":
                    hat.show_message("2Q")
                    if back != "aer" and internet_on():
                        hat.set_pixels(IBMQ_super_position)
                    else:
                        hat.set_pixels(super_position)
                    q2_calling_sense_func.execute(backend,back)
                else:
                    if joy_event[0][1]=="right":
                        hat.show_message("3Q")
                        if back != "aer" and internet_on():
                            hat.set_pixels(IBMQ_super_position)
                        else:
                            hat.set_pixels(super_position)
                        q3_calling_sense_func.execute(backend,back)
                    else:
                        if joy_event[0][1]=="middle":
                            if back == "aer":
                                back = "ibmq"
                                set_backend(back)
                            else:
                                back = "aer"
                                set_backend(back)
                                    

