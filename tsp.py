import sys
import re
import genetic
import annealing

if __name__ == "__main__":
    filename = sys.argv[2]
    f = open(filename, "r")
    pattern = 'NAME\s*=\s*(\w+)\s*,\s*SIZE\s*=\s*(\d+)\s*,\s*([\s\S]*)'
    m = re.search(pattern, "".join(f.readlines()))
    name = m.group(1)
    size = int(m.group(2))
    numbers = [int(x) for x in "".join(m.group(3).split()).split(",")]
    print("Name:", name)
    print("Size:", size)
    
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
        
    algorithm = sys.argv[1]
    if algorithm == 'genetic':
        genetic.distances = distances
        solution, length = genetic.genetic_algorithm()
    elif algorithm == 'annealing':
        annealing.distances = distances
        solution, length = annealing.annealing_algorithm()
    print(solution)
    print(length)
