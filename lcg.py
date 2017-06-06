#! /usr/bin/env python

from time import time

def lcg():
    def grab():
        ''' return two values pulled from current time nanoseconds '''
        value_1 = value_2 = 0  # init both values to zero
        while not value_1 and not value_2:
            try:
                value_1, value_2 = int(str(time()-int(time()))[-1]), \
                                int(str(time()-int(time()))[-2])
            except ValueError:
                grab()
        return value_1, value_2


    def validateInputs(modulus, increment):
        ''' ensures the relationship of the 'ingredients' fits that of an lcg and returns the 'random' result '''
        relation = 0  # init relation to invalid (0 is False in Python)

        while not relation:  # run until relation is valid
            multiplier, seed = grab()  # grab new numbers from current time
            relation = 0 <= increment < modulus and 0 <= seed < modulus and multiplier in [1, 3, 7, 9]  # check validity of relation

        #  return result of generate() using validated 'ingredients'
        return multiplier, seed


    def generate(modulus=10, increment=0):
        ''' the meat of the machine '''
        multiplier, seed = validateInputs(modulus, increment)
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
    return_val = generate(10, 0)

    # print and exit
    return return_val
