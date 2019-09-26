"""
ref: https://computation.physics.utoronto.ca/tutorials/tutorial-part-2-functions-and-modules-focus-numpy/
"""

"""
Function to calculate radioactivity given half-life formula

r(t + delta_t) = r(t) * ((1/2) ** (delta_t / t_h))

current activity is r(t), elapsed time is delta_t, half life is t_h
elapsed time and half life need to be same time units.
"""

def get_new_activity(current_activity, elapsed_time, half_life):
    return current_activity * (0.5 ** (elapsed_time / half_life))

# Initial activity in migrecuries
r = 5.0

# Time increment in years
t = 0
delta_t = 10.0

# Half life in years
t_12 = 30.0

#print activities for various elapsed times.
while t < 5 * delta_t:
    print(f'Time is now {t}, Activity is {get_new_activity(r, t, t_12)}') 
    t += delta_t