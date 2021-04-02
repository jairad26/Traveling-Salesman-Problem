import random
import pygame
import config
import pythag
import sys

def shuffle_method(screen):
    
    #printing info on screen
    printable_shortest_path = []
    for i in config.shortest_path:
        printable_shortest_path.append((i.x, i.y))
    myFont = pygame.font.SysFont('arial', 14)
 
    info_text2 = myFont.render("the shortest distance is :", False, config.white)
    shortest_distance_text = myFont.render(str(config.shortest_distance), False, config.white)
    
    screen.blit(info_text2,(4,0))
    screen.blit(shortest_distance_text,(4,14))
    
    
    #actual shuffling and algorithm
    random.shuffle(config.points)
    config.dist = pythag.calculate_distance(config.points)
    if config.dist < config.shortest_distance:
        config.count = 0
        config.shortest_distance = config.dist
        # print("the smallest distance right now is : " + str(config.shortest_distance))
        config.shortest_path = config.points.copy()
    config.count += 1
    
    
    #drawing lines once algorithm runs
    if not (config.count > 500*config.number_of_points):
        for m in range(len(config.points)-1):
            pygame.draw.line(screen, config.white, (config.points[m].x, config.points[m].y), (config.points[m+1].x, config.points[m+1].y), 2)
    else:
        config.flag += 1
        
    for m in range(len(config.shortest_path)-1):
        pygame.draw.line(screen, config.green, (config.shortest_path[m].x, config.shortest_path[m].y), (config.shortest_path[m+1].x, config.shortest_path[m+1].y), 4)

    # pygame.display.update()