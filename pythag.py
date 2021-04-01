import random
import pygame


#colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,24)

# distance between point using pythagorean theorem
def calculate_distance(points):
    total = 0
    for n in range(len(points)-1):
        #distance formula
        distance = ((points[n].x - points[n+1].x) ** 2 + (points[n].y - points[n+1].y) ** 2) ** 0.5
        total += distance
    return total


def output_vis(screen, points, dist, record_distance, count):
    smallest_path = points.copy()
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
        
    return count, record_distance