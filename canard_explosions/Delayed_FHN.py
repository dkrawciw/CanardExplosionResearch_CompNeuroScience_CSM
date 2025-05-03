import numpy as np

def Delayed_FHN(Y,t,d:float, g_c:float = 0.25, u_syn:float = 0.8, a:float = 0.7, b:float = 0.8, c:float = 3):
    y_now = Y(t)
    y_delay = Y(t-d)

    u,v = y_now
    u_delay,_ = y_delay

    dudt = u - 1/3*u**3 + v + g_c * np.tanh(u_delay - u_syn)
    dvdt = ( -u + a - b*v )/c

    return [dudt, dvdt]