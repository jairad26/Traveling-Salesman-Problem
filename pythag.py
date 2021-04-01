

# distance between point using pythagorean theorem
def calculate_distance(points):
    total = 0
    for n in range(len(points)-1):
        #distance formula
        distance = ((points[n].x - points[n+1].x) ** 2 + (points[n].y - points[n+1].y) ** 2) ** 0.5
        total += distance
    return total

