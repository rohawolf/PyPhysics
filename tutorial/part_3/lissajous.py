"""
ref : https://computation.physics.utoronto.ca/tutorials/learning-physics-pylab/
"""
from pylab import *

# define t range 
t = arange(0, 2 * pi, pi / 200)
x = cos(t)

def draw_subplot(case_num, n, phi):
    subplot(2, 3, case_num)
    plot(x, cos(n * t + phi), 'r.')
    _phi_str = {
        0 : '0',
        (pi / 4) : 'pi/4',
        (pi / 2): 'pi/2',
        (- pi / 3): '- pi/3',
    }.get(phi)
    title(f'n = {n}, phi = {_phi_str}')

sub_plot_args = [
    (1, 0),
    (1, pi / 4),
    (1, pi / 2),
    (2, pi / 2),
    (4, pi / 2),
    (5, - pi / 3),
]

for idx, args in enumerate(sub_plot_args):
    draw_subplot(idx + 1, *args)

show()