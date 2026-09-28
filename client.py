"""Quantum Fourier Transform (QFT) Engine.
100% Python Standard Library.
"""

import cmath
import math

class QFTCircuit:
    """Quantum Fourier Transform matrix operator on statevectors."""
    def __init__(self, num_qubits=2):
        self.n = num_qubits
        self.dim = 1 << num_qubits

    def transform(self, statevector):
        n = self.dim
        transformed = [complex(0, 0)] * n
        inv_sqrt_n = 1.0 / math.sqrt(n)
        for j in range(n):
            val = complex(0, 0)
            for k in range(n):
                angle = 2.0 * math.pi * j * k / n
                phase = cmath.exp(complex(0, angle))
                val += statevector[k] * phase
            transformed[j] = val * inv_sqrt_n
        return transformed
