import random

distances = []

MUTATE_PROB = 0.1
CROSSOVER_PROB = 0.7
TOURNAMENT_SIZE = 30
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
    tour2_unique = []
    for city in tour2:
        if city not in tour1[i:j]:
            tour2_unique.append(city)
    child = tour2_unique[:i] + tour1[i:j] + tour2_unique[i:]
    return child

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
    distances = [tour_length(tour) for tour in population]
    for i in range(SELECTION_SIZE):
        competitors = random.sample(range(len(population)), TOURNAMENT_SIZE)
        winner = min(competitors, key=lambda j: distances[j])
        winners.append(population[winner])
        del(population[winner])
        del(distances[winner])
    return winners

def genetic_algorithm():
    population = create_population()
    for i in range(GENERATIONS):
        selected = tournament_selection(population)
        children = []
        for j in range(POPULATION_SIZE - SELECTION_SIZE):
            parents = random.sample(selected, 2)
            if random.random() < CROSSOVER_PROB:
                child = crossover(*parents)
            else:
                child = random.choice(parents)[:]
            if random.random() < MUTATE_PROB:
                mutate2(child)
            children.append(child)
        population = selected + children

    solution = min(population, key=tour_length)
    return solution, tour_length(solution)
