import random
import pygame
import config
import pythag
import sys

def shuffle_method(screen):
    random.shuffle(config.points)
    config.dist = pythag.calculate_distance(config.points)
    if config.dist < config.record_distance:
        config.count = 0
        config.record_distance = config.dist
        print("the smallest distance right now is : " + str(config.record_distance))
        config.smallest_path = config.points.copy()
    config.count += 1
    for m in range(len(config.points)-1):
        pygame.draw.line(screen, config.white, (config.points[m].x, config.points[m].y), (config.points[m+1].x, config.points[m+1].y), 2)
    
    for m in range(len(config.smallest_path)-1):
        pygame.draw.line(screen, config.green, (config.smallest_path[m].x, config.smallest_path[m].y), (config.smallest_path[m+1].x, config.smallest_path[m+1].y), 4)

    pygame.display.update()
    if(config.count > 2500*config.number_of_points): #no real end to this sol, so just set a random parameter to stop it
        pygame.display.quit() 
        pygame.quit()
        print("the smallest distance is : ", config.record_distance)
        sys.exit()