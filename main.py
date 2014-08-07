#!/usr/bin/env python3

from timer import *
from field import *
from snake import *

class Main:

    def __init__(self):
        pass

    def game_out(self):
        for row in field.data:
            for value in row:
                if value == -1:
                    print("#", end="")
                elif value == 0:
                    print(" ", end="")
                elif value == 1:
                    print("+", end="")
                elif value == 2:
                    print("O", end="")
                else:
                    print("X", end="") 
            else:
                print()

    def game_in(self):
        result = input().lower()
        if result == "w":
            return (-1, 0)
        elif result == "s":
            return (1, 0)
        elif result == "a":
            return (0, -1)
        elif result == "d":
            return (0, 1)
        else:
            return (0, 0)

    def mainloop(self):
        snake.start()
        while True:
            try:
                field.reset()
                snake.start()
                while snake.lives:
                    self.game_out()
                    move = self.game_in()
                    snake.move(*move)
            except SnakeCrashException:
                    print("You failed!")
                    snake.lives -= 1
                    if snake.lives == 0:
                        break

main = Main()
main.mainloop()
            
