"""
ref : https://computation.physics.utoronto.ca/tutorials/learning-physics-pylab/
"""
from pylab import *
from random import randint

# Random results of rolling dice 20 times
roll = [randint(1, 6) for _ in range(20)]

# for normalization
n = len(roll)
weights_array = ones(n) / n

# histogram
figure(1)
hist(roll, 6, weights=weights_array, range=[0.5, 6.5], align='mid')
xticks(range(1,7))
xlabel('Roll')
ylabel('Probability of Roll')
title('Nicely binned normalized histogram')
show()

