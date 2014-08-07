#!/usr/bin/env python3

from field import *

class SnakeCrashException(Exception): pass

class Snake:

    def __init__(self, lives):
        self.lives = lives
        self.score = 0

    def start(self):
        row = field.size//2
        for coloumn in range(3):
            field.data[row][coloumn + 1] = 4 - coloumn

    def get_head(self):
        for i, row in enumerate(field.data):
            for j, value in enumerate(row):
                if value == 2:
                    return (i, j)

    def get_tail(self):
        maximum = 4
        x = 0
        y = 0
        for i, row in enumerate(field.data):
            for j, value in enumerate(row):
                if value >= maximum:
                    maximum = value
                    x, y = i, j
        return (x, y)
                
            

    def collide(self, x, y):
        head_position = self.get_head()
        if ((head_position[0] + x < 0) or (head_position[0] + x >= field.size) or
            (0 > head_position[1] + y) or (head_position[1] + y >= field.size)):
            return True
        else:
            return False

    def add(self):
        for i, row in enumerate(field.data):
            for j, value in enumerate(row):
                if value >= 2:
                    field.data[i][j] = value + 1

    def move(self, x, y):
        if self.collide(x, y):
            print(x, y)
            raise SnakeCrashException
        else:
            head_position = self.get_head()
            tail_position = self.get_tail()
            block = field.data[head_position[0] + x][head_position[1] + y]
            if block == -1:
                raise SnakeCrashException
            elif block == 0:
                field.data[tail_position[0]][tail_position[1]] = 0
            elif block == 1:
                pass
            elif block >= 2:
                raise SnakeCrashException
            self.add()
            field.data[head_position[0] + x][head_position[1] + y] = 2


snake = Snake(3)
