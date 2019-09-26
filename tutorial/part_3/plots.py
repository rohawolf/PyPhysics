"""
ref : https://computation.physics.utoronto.ca/tutorials/learning-physics-pylab/
"""
from pylab import *


"""
plot y = x^2 (0 <= x <= 4)

>> x_range = range(5)
>> y_range = [x**2 for x in x_range]
>> plot(x_range, y_range)
>> show()
"""

# default x range
x = arange(1, 10, 0.5)
x_square = x ** 2
x_cube = x ** 3
x_sqr = x ** 0.5

# open figure 1
figure(1)
plot(x, x_square)
xlabel('abscissa')
ylabel('ordinate')
title('A practice plot.')

# open figure 2
figure(2)
plot(x, x_square, 'ro', x, x_cube, 'g+--')
xlabel('abscissa')
ylabel('ordinate')
title('More practice plot.')
legend(('squared', 'cubed'))

# open figure 3
figure(3)

subplot(3, 1, 1)
plot(x, x_sqr, 'k*:')
title('square roots')

subplot(3, 1, 2)
plot(x, x_square, 'r>-')
title('squares')

subplot(3, 1, 3)
plot(x, x_cube, 'mh-')
title('cubes')

# show all figures
show()