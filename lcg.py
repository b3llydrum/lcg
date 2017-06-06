#! /usr/bin/env python

from time import time

def lcg():

    # return two values pulled from current time in nanoseconds
    def get_seeds():

        value_1 = value_2 = 0
        
        while not value_1 and not value_2:
            try:
                value_1, value_2 = int(str(time()-int(time()))[-1]), \
                                int(str(time()-int(time()))[-2])
            except ValueError:
                get_seeds()
        
        return value_1, value_2


    # ensure relationship of seeds fits that of an lcg and return the "random" result
    def validate_inputs(modulus, increment):
        
        # init relation to zero, or invalid
        relation = 0

        while not relation:

            # grab new seeds
            multiplier, seed = get_seeds()

            # check validity of relation
            relation = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]

        #  return result of get_seeds() after validation
        return multiplier, seed


    # main function
    def generate(modulus=10, increment=0):

        multiplier, seed = validate_inputs(modulus, increment)
        output = [seed]
        current_iteration = -1  # initialize out of range to cause auto false in while loop below
        switch = False

        # this part is just magic; i don't even remember how it works. refer to the wikipedia link above
        while current_iteration != seed and current_iteration != 0:
            if not switch:
                current_iteration = (seed * multiplier) + increment
                switch = True
            else:
                current_iteration = (current_iteration * multiplier) + increment
            if current_iteration > modulus:
                current_iteration %= modulus

            output.append(current_iteration)

        # cut out second-to-last character and cast it to an int, then return that. Whew!
        result = int(str(''.join([str(i) for i in output]))[-2])
        return result


    # call main in mod 10 with an iteration of 0 (no more random than it needs to be)
    return generate(10, 0)
