# -*- coding: utf-8 -*-
# Qiskit
# Example of Bell, or entangled, states
from sense_hat import SenseHat
hat = SenseHat()

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
#import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
#import matplotlib.pyplot as plt

#Set number of bits and number of shots
n = 3
sh = 1024

# Create a Quantum Register with n qubits
qr = QuantumRegister(n)

# Create a Classical Register with n bits
cr = ClassicalRegister(n)

# Create a Quantum Circuit acting on the qr and cr register
circuit = QuantumCircuit(qr, cr)

# Add gates to the circuit
circuit.h(qr[0])
circuit.h(qr[1])
circuit.x(qr[2])
circuit.cx(qr[1], qr[2])
circuit.cx(qr[0], qr[2])
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])
circuit.measure(qr[0], cr[0])
circuit.measure(qr[1], cr[1])
circuit.measure(qr[2], cr[2])

# Set the backend to execute on
from qiskit import Aer
backend = Aer.get_backend('qasm_simulator')

# Create a Quantum Program for a 1024 shot execution of the circuit on the selected backend
job = execute(circuit, backend, shots=sh)

# Get the result of the execution
result = job.result()

# Privode the results

print ("Results:")
#print (result)
print (result.get_counts(circuit))

#Create a default dictionary with all values 0 
global lst
lst = [bin(x)[2:].rjust(n, '0') for x in range(2**n)]
values = [0]*pow(2,n)
#print(values)
#print(lst)
Qdict = dict(zip(lst,values))

# Update the dictionary with the actual values
Qdictres = result.get_counts(circuit)
Qdict.update(Qdictres)
#Scale by dividing by 1024 (shots)
#Qdict.update({m: (1/sh) * Qdict[m] for m in Qdict.keys()})

# Create the bar diagram
#objects = tuple(lst)
#y_pos = np.arange(len(objects))

# Create the presentation bar diagram from real data
#performance = []
#for i in range(len(lst)):
 #   entry = lst[i]
 #   appval= Qdict[entry]
 #   performance.append(appval)

#print(performance)
#plt.ylim(top=1) 
#plt.bar(y_pos, performance, align='center', alpha=0.5)
#plt.xticks(y_pos, objects, rotation=45)
#plt.ylabel('Probability')
#plt.title('States')
 
#plt.show()

# Still need to add the sensehat stuff, matrix creation etc.
# Start with: https://matplotlib.org/gallery/images_contours_and_fields/matshow.html#sphx-glr-gallery-images-contours-and-fields-matshow-py

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# examples using (x, y, pixel)
hat.clear()
hat.set_pixel(0, 0, red)
hat.set_pixel(0, 0, green)
hat.set_pixel(0, 0, blue)

for key in Qdict:
	y=7-int(key,2)
	for x in range (0,8):
		if (x*128)-Qdict[key]<0:
			hat.set_pixel(x, y, red)
		else:
			hat.set_pixel(x, y, blue)
       # print (Qdict[key])
       # print (int(key,2))

