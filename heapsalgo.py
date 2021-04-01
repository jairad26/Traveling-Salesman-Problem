import config
import pythag
import pygame

'''
recursive heap permutation algorithm
'''    
def heapPermutationRecursive(screen, points, size):
    if(size==1):
        EvaluateSolution(screen, points)
        return
    for i in range(size):
        heapPermutationRecursive(screen, points, size-1)
        
        #if size is odd, swap 0th and (size-1)th element
        #if size is even, swap ith and (size-1)th element
        if size & 1:
            points[0], points[size-1] = points[size-1], points[0]
        else:
            points[i], points[size-1] = points[size-1], points[i]
            
            
'''
non-recursive heap permutation algorithm
''' 
def heapPermutationNonRecursive(screen, points, size):
    c = []
    for h in range(size):
        c.append(0)
    EvaluateSolution(screen, points)
    i = 0
    while i < size:
        if c[i] < i:
            if i % 2 == 0:
                points[0], points[i] = points[i], points[0]
            else:
                points[c[i]], points[i] = points[i], points[c[i]]
            EvaluateSolution(screen, points)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
                
            
def EvaluateSolution(screen, points):
    config.dist = pythag.calculate_distance(points)
    if(config.dist < config.shortest_distance):
        config.shortest_distance = config.dist
        config.shortest_path = points.copy()
    for m in range(len(config.shortest_path)-1):
        pygame.draw.line(screen, config.green, (config.shortest_path[m].x, config.shortest_path[m].y), (config.shortest_path[m+1].x, config.shortest_path[m+1].y), 4)
    
        myFont = pygame.font.SysFont('arial', 14)

        info_text2 = myFont.render("the shortest distance is :", False, config.white)
        shortest_distance_text = myFont.render(str(config.shortest_distance), False, config.white)
        
        screen.blit(info_text2,(4,0))
        screen.blit(shortest_distance_text,(4,14))