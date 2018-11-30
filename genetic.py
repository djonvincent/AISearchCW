import random
import time

distances = []

MUTATE_PROB = 0.75
TOURNAMENT_SIZE = 50
POPULATION_SIZE = 100
GENERATIONS = 1000
SELECTION_SIZE = 10

# Swaps the positions of 2 random cities in a tour
def mutate(tour):
    i = random.randint(0, len(tour) - 1)
    j = i
    while j == i:
        j = random.randint(0, len(tour) - 1)
    tour[i], tour[j] = tour[j], tour[i]

def mutate2(tour):
    i = random.randint(0, len(tour) - 1)
    j = i
    while j == i:
        j = random.randint(0, len(tour) - 1)
    i, j = min(i,j), max(i,j)
    tour[i:j] = list(reversed(tour[i:j]))

def crossover(tour1, tour2):
    i = random.randint(0, len(tour1) - 1)
    j = i
    while i == j:
        j = random.randint(0, len(tour1) - 1)
    i, j = min(i,j), max(i,j)
    tour2_unique = tour2[:]
    for city in tour1[i:j]:
        tour2_unique.remove(city)
    return tour2_unique[:i] + tour1[i:j] + tour2_unique[i:]

def create_population():
    length = len(distances[0])
    initial = list(range(length))
    population = []
    for i in range(POPULATION_SIZE):
        tour = initial[:]
        random.shuffle(tour)
        population.append(tour)
    return population

def tour_length(tour):
    distance = 0
    for i in range(len(tour)):
        d = distances[tour[i]][tour[(i+1) % len(tour)]]
        distance += d
    return distance

def tournament_selection(population):
    winners = []
    population = population[:]
    distances = [tour_length(tour) for tour in population]
    for i in range(SELECTION_SIZE):
        competitors = random.sample(range(len(population)), TOURNAMENT_SIZE)
        winner = min(competitors, key=lambda j: distances[j])
        winners.append(population[winner])
        del(population[winner])
        del(distances[winner])
    return winners

def genetic_algorithm():
    start_time = time.time()
    population = create_population()
    for i in range(GENERATIONS):
        selected = tournament_selection(population)
        children = []
        for j in range(POPULATION_SIZE - SELECTION_SIZE):
            parents = random.sample(selected, 2)
            child = crossover(*parents)
            if random.random() < MUTATE_PROB:
                mutate2(child)
            children.append(child)
        population = selected + children

    solution = min(population, key=tour_length)
    end_time = time.time()
    print('Time', end_time - start_time)
    return solution, tour_length(solution)
