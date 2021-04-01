import pygame
import time
import random
import os
import sys

from Points import Point


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
number_of_points = 30

# Generate random points on screen
for n in range(number_of_points):
    x  = random.randint(offset_screen, width - offset_screen)
    y = random.randint(offset_screen, height - offset_screen)
    
    point = Point(x,y)
    points.append(point)
    

    
# distance between point using pythagorean theorem
def calculate_distance(points_list):
    total = 0
    for n in range(len(points)-1):
        #distance formula
        distance = ((points[n].x - points[n+1].x) ** 2 + (points[n].y - points[n+1].y) ** 2) ** 0.5
        total += distance
    return total

dist = calculate_distance(points)
record_distance = dist

smallest_path = points.copy()
count = 0
running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # draw lines and points
    
    for n in range(len(points)):
        pygame.draw.circle(screen, white, (points[n].x, points[n].y), 10)
        
    a = random.randint(0, len(points)-1)
    b = random.randint(0, len(points)-1)
    random.shuffle(points)
    dist = calculate_distance(points)
    if dist < record_distance:
        count = 0
        record_distance = dist
        print("the smallest distance right now is : " + str(record_distance))
        smallest_path = points.copy()
    count += 1
        
    for m in range(len(points)-1):
        pygame.draw.line(screen, white, (points[m].x, points[m].y), (points[m+1].x, points[m+1].y), 2)
    
    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen, green, (smallest_path[m].x, smallest_path[m].y), (smallest_path[m+1].x, smallest_path[m+1].y), 4)
        
    pygame.display.update()
    if(count > 5*pow(2,number_of_points)):
        pygame.display.quit() 
        pygame.quit()
        print("the smallest distance is : ", record_distance)
        sys.exit()