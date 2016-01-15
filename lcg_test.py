# this is a linear congruential generator (lcg)
# core function of this pseudo-rng is the recurrence relation (rr):
# Xn+1 = (aXn + c) mod m
# this lcg only outputs a single integer - hence modulus 9
# with an increment of 0, making it multiplicative
# the multiplier and seed values are the only variables
# and are pulled from the current time at execution
# for more visit https://en.wikipedia.org/wiki/Linear_congruential_generator

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
        relation = 0 < modulus and \
                   0 < multiplier < modulus and \
                   0 <= increment < modulus and \
                   0 <= seed < modulus and \
                   (multiplier != 3 and multiplier != 6)
    return generate(modulus, multiplier, increment, seed)
        
def generate(modulus, multiplier, increment, seed):

    output = [seed]
    current_iteration = -1
    switch = False
    n = 0

    # here lies the bug
    # either:
        # 9 is never being passed to the output array
        # or
        # 9 is never the last number before cur_it becomes seed again
        # debug for the former

    while current_iteration != seed: 

        if not switch:
            current_iteration = (seed * multiplier) + increment
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + increment
        if current_iteration > modulus:
            current_iteration = current_iteration % modulus
                

        output.append(current_iteration)
        n += 1
        print("Seed: " + str(seed))
        print("Multiplier: " + str(multiplier))
        print("Current iteration: " + str(current_iteration))
        print("----")

    return int(str("".join([str(i) for i in output]))[-2])

return_val = rr(9, 0)
print(return_val)

sys.exit(0)
