import random

# Swaps the positions of 2 random cities in a tour
def mutate(tour):
    i = random.randint(0, len(tour) - 1)
    j = i
    while j == i:
        j = random.randint(0, len(tour) - 1)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def crossover(tour1, tour2):
    i = random.randint(0, len(tour1) - 1)
    j = random.randint(0, len(tour1) - 1)
    i, j = min(i,j), max(i,j)
    tour2_unique = []
    for city in tour2:
        if city not in tour1[i:j]:
            tour2_unique.append(city)
    child = tour2_unique[:i] + tour1[i:j] + tour2_unique[i:]
    return child

