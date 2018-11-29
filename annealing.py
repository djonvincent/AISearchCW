import random
import math

START_TEMP = 100
TEMP_COEF = 0.9999

def successor(tour):
    i = random.randint(0, len(tour) - 1)
    j = i
    while j == i:
        j = random.randint(0, len(tour) - 1)
    i, j = min(i,j), max(i,j)
    return tour[:i] + list(reversed(tour[i:j])) + tour[j:]

def tour_length(tour):
    distance = 0
    for i in range(len(tour)):
        d = distances[tour[i]][tour[(i+1) % len(tour)]]
        distance += d
    return distance

def annealing_algorithm():
    t = START_TEMP
    tour = list(range(len(distances[0])))
    random.shuffle(tour)
    while t > 0.01:
        next_tour = successor(tour)
        #print('current', tour)
        #print('next', next_tour)
        #print('next tour length %d'%tour_length(next_tour))
        current_length = tour_length(tour)
        delta = tour_length(next_tour) - current_length
        #print('delta %d'%delta)
        try:
            p = 1/(1+math.exp((float(delta)*START_TEMP)/(current_length*t)))
        except OverflowError:
            p = 0
        #if delta > 0:
            #print('temp %f'%t)
            #print('prob %f'%p)
        if delta < 0 or random.random() < p:
            tour = next_tour
        t = t*TEMP_COEF
    return tour, tour_length(tour)

