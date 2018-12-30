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

## Requirements  

These scripts were developed and tested with the following hard- and software:
- Hardware
   - Raspberry PI 2B (a21041)
   - Raspberry Pi Sense HAT (v1.0)
- Software
  - Raspbian GNU/Linux 9 (stretch)
  - qiskit 0.6.1
  - sense-hat 2.2.0
