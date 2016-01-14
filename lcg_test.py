# this is a linear congruential generator (lcg)
# core function of this pseudo-rng is the recurrence relation (rr):
# Xn+1 = (aXn + c) mod m
# this version is mod 9, generating one random digit using that relation
# with an increment of 0, making it multiplicative
# but that can be changed by adjusting the third argument on line 21
# the multiplier and seed values are the only variables
# and are pulled from the current time at execution
# this lcg only pulls one integer, can be changed by adjusting the
# splice in the output variable on line 50
# for more visit https://en.wikipedia.org/wiki/Linear_congruential_generator

import time, sys

class Recursion(Exception):
    pass

def grab():
    value_1 = value_2 = 0
    while not value_1 and not value_2:
        value_1, value_2 = int(str(time.time()-int(time.time()))[-1]), \
                           int(str(time.time()-int(time.time()))[-2])
    return value_1, value_2

def rr():
    relation = 0
    while not relation:
        multiplier, seed = grab()
        relation = 0 < modulus and \
                   0 < multiplier < modulus and \
                   0 <= increment < modulus and \
                   0 <= seed < modulus
    return generate(9, multiplier, 0, seed)
        
def generate(modulus, multiplier, increment, seed):

    output = [seed]
    current_iteration = -1
    switch = False

    while current_iteration != seed:
        if not switch:
            current_iteration = (seed * multiplier) + increment
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + increment
        if current_iteration > modulus:
            current_iteration = current_iteration % modulus
            if current_iteration == 0:
                current_iteration += 1
        output.append(current_iteration)

    return int(str("".join([str(i) for i in output]))[-2])

sys.exit(0)
