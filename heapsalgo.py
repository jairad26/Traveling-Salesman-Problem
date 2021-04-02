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
    for h in range(size):
        config.c.append(0)
    EvaluateSolution(screen, points)
    if config.i < size:
        if config.c[config.i] < config.i:
            if config.i % 2 == 0:
                points[0], points[config.i] = points[config.i], points[0]
            else:
                points[config.c[config.i]], points[config.i] = points[config.i], points[config.c[config.i]]
            EvaluateSolution(screen, points)
            config.c[config.i] += 1
            config.i = 0
        else:
            config.c[config.i] = 0
            config.i += 1
    else:
        config.flag += 1
                
            
def EvaluateSolution(screen, points):
    screen.fill(config.black)
    for n in range(len(config.points)):
        pygame.draw.circle(screen, config.white, (points[n].x, points[n].y), 10)
    config.dist = pythag.calculate_distance(points)
    # for m in range(len(config.points)-1):
    #         pygame.draw.line(screen, config.white, (points[m].x, points[m].y), (points[m+1].x, points[m+1].y), 2)
        
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