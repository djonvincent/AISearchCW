import sys
import re
import genetic
import annealing

def generate_distance_matrix(filename):
    with open(filename, "r") as f:
        pattern = 'NAME\s*=\s*(\w+)\s*,\s*SIZE\s*=\s*(\d+)\s*,\s*([\s\S]*)'
        m = re.search(pattern, "".join(f.readlines()))
    name = m.group(1)
    size = int(m.group(2))
    numbers = [int(x) for x in "".join(m.group(3).split()).split(",")]
    
    distances = []
    position = 0
    for i in range(size):
        row = []
        for j in range(i):
            row.append(distances[j][i])
        row.append(0)
        row += numbers[position:position+size-i-1]
        position += size -i-1
        distances.append(row)
    return distances

if __name__ == "__main__":
    filename = sys.argv[2]
    distances = generate_distance_matrix(filename)
    algorithm = sys.argv[1]
    if algorithm == 'genetic':
        genetic.distances = distances
        solution, length = genetic.genetic_algorithm()
    elif algorithm == 'annealing':
        annealing.distances = distances
        solution, length = annealing.annealing_algorithm()
    print(solution)
    print(length)
