import sys
import re
import genetic

if __name__ == "__main__":
    filename = sys.argv[1]
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
        
    population = genetic.create_population(size, 100)
    genetic.distances = distances
    print(population[0])
    print(genetic.tour_length(population[0]))
