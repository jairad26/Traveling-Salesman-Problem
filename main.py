import pygame
import time
import random
import os
import sys
import pythag
import config
import shuffle
import heapsalgo

from Points import Point


os.environ["SDL_VIDEO_CENTERED"]='1'


#pygame settings
pygame.init()
pygame.display.set_caption("Traveling Salesman Problem")
screen = pygame.display.set_mode((config.width, config.height))
clock = pygame.time.Clock()


# Generate random points on screen
for n in range(config.number_of_points):
    x  = random.randint(config.offset_screen, config.width - config.offset_screen)
    y = random.randint(config.offset_screen, config.height - config.offset_screen)
    
    point = Point(x,y)
    config.points.append(point)


config.dist = pythag.calculate_distance(config.points)
config.shortest_distance = config.dist

config.shortest_path = config.points.copy()
config.count = 0
running = True
while running:
    screen.fill(config.black)
    clock.tick(config.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                  
    # draw points
    for n in range(len(config.points)):
        pygame.draw.circle(screen, config.white, (config.points[n].x, config.points[n].y), 10)
        
        
    '''
    this is where you call your algorithm
    '''    
    # shuffle.shuffle_method(screen) #randomly shuffles points, pretty fast but you never know when to stop
    heapsalgo.heapPermutationNonRecursive(screen, config.points, len(config.points))
    
    pygame.display.update()
pygame.display.quit() 
pygame.quit()
# print("the shortest distance is : ", config.shortest_distance)
sys.exit()