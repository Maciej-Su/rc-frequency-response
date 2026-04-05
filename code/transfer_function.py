import numpy as np

def transfer_function(omega, R, C):
    return 1 / (1 + 1j * omega * R * C)