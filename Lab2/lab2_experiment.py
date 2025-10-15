import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def experiment():
    balls = ['red'] * 3 + ['blue'] * 4 + ['black'] * 2
    die_faces = [1, 2, 3, 4, 5, 6]
    primes = [2, 3, 5]
    die = np.random.choice(die_faces)
    #print("Die roll: ", die)
    if die in primes:
        balls.append('black')
    elif die == 6:
        balls.append('red')
    else:
        balls.append('blue')
    draw = np.random.choice(balls)
    balls.remove(draw)
    #print("Drawn ball: ", draw)
    #print("Remaining balls: ", balls)
    return draw

def estimate_probability(size = 1000):
    draws = [experiment() for _ in range(size)]
    prob_red = draws.count('red') / size

    return prob_red

print("b) (0.5p) Using the simulation, estimate the probability of drawing a red ball: ", estimate_probability(20000))