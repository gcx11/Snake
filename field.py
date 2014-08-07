#!/usr/bin/env python3

import math
import random

class Field:

    def __init__(self, size):
        self.size = size
        self.data = [[0 for i in range(size)] for j in range(size)]
        self.make_walls()
        self.generate_bonuses()

    def reset(self):
        for i in range(self.size):
            for j in range(self.size):
                self.data[i][j] = 0
        self.make_walls()
        self.generate_bonuses()

    def make_walls(self):
        for i in range(self.size):
            self.data[i][0] = -1
            self.data[i][self.size - 1] = -1
            self.data[0][i] = -1
            self.data[self.size - 1][i] = -1

    def generate_bonuses(self):
        for x in range(random.randint(self.size//2,
                                      self.size*2)):
            self.data[random.randint(1, self.size - 2)][random.randint(1, self.size - 2)] = 1

field = Field(10)


#test
if __name__ == "__main__":
    from pprint import pprint
    field.data[0][1] = 1
    pprint(field.data)
    input()

    
