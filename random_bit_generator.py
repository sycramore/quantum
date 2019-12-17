#initialize a superposition as 1/sqrt(2) (0+1) and then measure in computational basis
#this should deliver a string of random bits with probability 0.5 for each bit

import cirq
print("Bit string length:")
rep = input()
#final number of bits divided by 2
num_bits = 1

#initialize qubits
qubits = [cirq.GridQubit(i, j) for i in range(num_bits) for j in range(2)]

#superpose 2 qubits for every subgrid

superposition_circuit = cirq.Circuit()
superposition_circuit.append(cirq.H(q) for q in qubits)

#measure every qubit in computational basis

superposition_circuit.append(cirq.measure(*qubits, key='z'))

#run simulation of circuit
simulator = cirq.google.XmonSimulator()

results = simulator.run(superposition_circuit, repetitions=rep)
print(results)
