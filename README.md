# Qrasp - Two and three qubit Qiskit user interface on Raspberry PI SenseHat
A set of Python scripts that uses Qiskit to run two or three qubit quantum circuits and display the results as bar graphs on a Raspberry PI SenseHat 8x8 LED display.

![qrasp_3qubit_GHZ.jpg](qrasp_3qubit_GHZ.jpg)

## Contents
Qrasp consists of the following scripts:
1. main_controller.py  
This script loads the required libraries, and uses the SenseHat joystick to select one of the Quantum programs.

2. Quantum program scripts  
These scripts creates and executes the quantum programs, and then calls the display script with the results. 
   - q2_calling_sense_func.py  
Python function that creates a simple, two qubit quantum cirquit and sets up and measures each qubit in a superposition state.
   - q3_calling_sense_func.py  
Python function that creates a simple, three qubit quantum cirquit and sets up and measures each qubit in a superposition state.
   - bell_calling_sense_func.py  
Python function that creates a simple, two qubit quantum cirquit and sets up and measures a Bell, or entangled, state.
   - GHZ_calling_sense_func.py  
Python function that creates a simple, three qubit quantum cirquit and sets up and measures an entangled GHZ state.
3. qc_sensehat_func.py  
Using SenseHat 8x8 display to show bar graph of 2 or 3 qubit Qiskit results dictionaries.

### What you can do with this version...
This version lets you run four different quantum scripts that demo superposition and entanglement with two and three qubits.

You use the joystick to select the script to run: 
- Up: Two qubit Bell state (entanglement)
- Down: Three qubit GHZ state (entanglement)
- Right: Three qubit superposition
- Left: Two qubit superposition

The quantum circuits currently run on the 'qasm_simulator' backend. 

### Planned for the future
- Use of the joystick 'button' to switch between simulator and hardware backend.
- Snazzy 'quantum calculations running' animation on the 8x8 LED display while the simulation is running or while waiting for the hardware backend to return results.
- Color gradients between the red and blue LEDs to indicate results with finer granularity than 1/8 or the bar.
- More...


## Requirements  

These scripts were developed and tested with the following hard- and software:
- Hardware
   - Raspberry PI 2B (a21041)
   - Raspberry Pi Sense HAT (v1.0)
- Software
  - Raspbian GNU/Linux 9 (stretch)
  - qiskit 0.6.1 (seems to run fine on 0.7)
  - sense-hat 2.2.0
