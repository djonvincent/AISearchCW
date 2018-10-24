import random

distances = []

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

def create_population(length, size):
    initial = list(range(length))
    population = []
    for i in range(size):
        tour = initial[:]
        random.shuffle(tour)
        population.append(tour)
    return population

def tour_length(tour):
    distance = 0
    for i in range(len(tour)):
        d = distances[tour[i]][tour[(i+1) % len(tour)]]
        print(d)
        distance += d
    return distance

def tournament_selection(population, size, n):
    winners = []
    for i in range(n):
        random.shuffle(population)
        competitors = population[:n]
        winner = min(competitors, key=tour_length)
        winners.append(winner)
    return winners
