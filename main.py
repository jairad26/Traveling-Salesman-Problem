import pygame
import time
import random
import os
import sys
import pythag

from points import Point


os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 500,500

#colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,24)

#pygame settings
pygame.init()
pygame.display.set_caption("Traveling Salesman Problem")
screen = pygame.display.set_mode((width, height))

#variables
points = []
offset_screen = 50
smallest_path = []
number_of_points = 10

# Generate random points on screen
for n in range(number_of_points):
    x  = random.randint(offset_screen, width - offset_screen)
    y = random.randint(offset_screen, height - offset_screen)
    
    point = Point(x,y)
    points.append(point)
    
# shuffle points position in the list
def shuffle(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp
    
#must set here and pass as parameters to function
dist = pythag.calculate_distance(points)
record_distance = dist

# smallest_path = points.copy()
count = 0
running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # draw points
    for n in range(len(points)):
        pygame.draw.circle(screen, white, (points[n].x, points[n].y), 10)
    
    #draw lines between points, record distance, current calcs, etc.
    count, record_distance = pythag.output_vis(screen, points, dist, record_distance, count)
        
    pygame.display.update()
    if(count > 5000*number_of_points):
        pygame.display.quit() 
        pygame.quit()
        print("the smallest distance is : ", record_distance)
        sys.exit()