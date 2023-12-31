import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple :
    def __init__(self, parent_screen) :
        self.image = pygame.image.load("ressources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE 
        self.y = SIZE 

    def draw(self) :
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

    def move(self) :
        self.x = random.randint(0,24)*SIZE
        self.y = random.randint(0,19)*SIZE

class Snake :
    def __init__(self, parent_screen, length) :
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("ressources/block.jpg").convert()
        self.x = [SIZE] * self.length
        self.y = [SIZE] * self.length
        self.direction = 'down'

    def increase_length(self) :
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self) :
        self.parent_screen.fill((100, 165, 67))
        for i in range(self.length) :
            self.parent_screen.blit(self.block, (self.x[i],self.y[i]))
        pygame.display.flip() # or update method

    def move_left(self) :
        self.direction = 'left'
    
    def move_right(self) :
        self.direction = 'right'
    
    def move_up(self) :
        self.direction = 'up'

    def move_down(self) :
        self.direction = 'down'

    
    def walk(self) :

        for i in range(self.length -1, 0, -1) :
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


        if self.direction == 'right' :
            self.x[0] += SIZE
        if self.direction == 'left' :
            self.x[0] -= SIZE
        if self.direction == 'up' :
            self.y[0] -= SIZE
        if self.direction == 'down' :
            self.y[0] += SIZE

        self.draw()

class Game :
    def __init__ (self):
        pygame.init()

        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((92,25,84))

        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()

    def play(self) :
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y) :
            print("Collision Detected")
            self.snake.increase_length()
            self.apple.move()
            while self.is_snake_apple_collision() :
                self.apple.move()
            


    def is_collision(self, x1, x2, y1, y2) :
        if x1 >= x2 and x1 < x2 + SIZE :
            if y1 >= y2 and y1 < y2 + SIZE : 
                return True 
        return False

    def is_snake_apple_collision(self) :
        for i in range(self.snake.length) :
            if self.is_collision(self.snake.x[i], self.apple.x, self.snake.y[i], self.apple.y,) :
                return True
        return False

    def run(self) :
        running = True
        while running :
            for event in pygame.event.get() :
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        running = False

                    if event.key == K_UP :
                        self.snake.move_up()
                    if event.key == K_DOWN :
                        self.snake.move_down()
                    if event.key == K_RIGHT :
                        self.snake.move_right()
                    if event.key == K_LEFT :
                        self.snake.move_left()
                    
                if event.type == QUIT :
                    running = False
            

            
            self.play()
            time.sleep(0.2)

    

if __name__ == "__main__" :

    game = Game()
    game.run()


    
    