from client import QFTCircuit

qft = QFTCircuit(num_qubits=2)
state = [complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)]
out = qft.transform(state)
print("QFT output amplitudes:", [round(abs(a), 4) for a in out])
