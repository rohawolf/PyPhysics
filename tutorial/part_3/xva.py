"""
ref : https://computation.physics.utoronto.ca/tutorials/learning-physics-pylab/
"""
from pylab import *


# define time array
t = arange(0, 20.5, 0.5)

# terminal speed
s_t = 20.0

# time constant
tau = 5.0

def v_mps(t):
    return -s_t * (1 - exp(-t / tau))

def x_m(t):
    return -s_t * (t + tau * (1 - exp(-t / tau)))

def a_mps2(t):
    return -s_t * exp(-t / tau) / tau

print("%8s %8s %8s %8s" % ('t', 'x(t)', 'v(t)', 'a(t)'))
for _t in t:
    print("%8.1f %8.1f %8.1f %8.1f" % (_t, x_m(_t), v_mps(_t), a_mps2(_t)))

subplot(3,1,1) 
plot(t, x_m(t))
ylabel('x(m)')
title('Position')
    
subplot(3,1,2)
plot(t, v_mps(t))
ylabel('v(m/s)')
title('Velocity')

subplot(3,1,3)
plot(t, a_mps2(t))
xlabel('time(s)')
ylabel('a(m/s^2)')
title('acceleration')

show()