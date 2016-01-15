# multiplier and seed pulled from the current time at execution
# https://en.wikipedia.org/wiki/Linear_congruential_generator

import time, sys

def grab():
    value_1 = value_2 = 0
    while not value_1 and not value_2:
        value_1, value_2 = int(str(time.time()-int(time.time()))[-1]), \
                           int(str(time.time()-int(time.time()))[-2])
    return value_1, value_2

def rr(modulus, increment):
    relation = 0
    while not relation:
        multiplier, seed = grab()
        relation = 0 <= increment < modulus and \
                   0 <= seed < modulus and \
                   multiplier in [1, 3, 7, 9]
    return generate(modulus, multiplier, increment, seed)

def generate(modulus, multiplier, increment, seed):

    output = [seed]
    current_iteration = -1
    switch = False

    while current_iteration != seed and current_iteration != 0:

        if not switch:
            current_iteration = (seed * multiplier) + increment
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + increment
        if current_iteration > modulus:
            current_iteration %= modulus

        output.append(current_iteration)

    return int(str("".join([str(i) for i in output]))[-2])

return_val = rr(10, 0)
print(return_val)

sys.exit(0)
