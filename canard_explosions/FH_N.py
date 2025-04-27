import numpy as np

def FH_N(t, y, a=5, tau_n=60, I=-4.2):
    v, n = y
    dvdt = v - (v**3) / 3 - n + I
    dndt = (a * v - n) / tau_n

    return np.array([dvdt, dndt])