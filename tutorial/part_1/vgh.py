# -*- coding: utf-8 -*-

# Initial vertical velocity
v_mps = 15.0

# Gravitational acceleration
g_mps2 = 9.8

# height formular
def vertical_displacement(v_mps):
    h_m = v_mps**2 / (2 * g_mps2)
    return h_m

# print result
print(f'If v = {v_mps} m/s and g = {g_mps2} m/s^2, then vertical_displacement h = {vertical_displacement(v_mps)} m.')


