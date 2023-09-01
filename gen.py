import random

def generate_individual():
    return [random.randint(0, 255) for _ in range(27)]

def calculate_checksum(bytes):
    return sum(bytes)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)

    child = parent1[:crossover_point] + parent2[crossover_point:]

    return child

def mutate(individual):
    index_to_mutate = random.randint(0, len(individual) - 1)
    individual[index_to_mutate] = random.randint(0, 255)

desired_checksums = [0x056F, 0x0570, 0x0571, 0x0572, 0x0573, 0x0574, 0x0575, 0x0576, 0x0577, 0x0578, 0x0579, 0x057A, 0x057B, 0x057C, 0x057D, 0x057E, 0x057F]

population_size = 100
max_generations = 1000

for desired_checksum in desired_checksums:
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(max_generations):
        fitness_scores = [abs(calculate_checksum(individual) - desired_checksum) for individual in population]

        if 0 in fitness_scores:
            index = fitness_scores.index(0)
            print(f"Sol. found for checksum 0x{desired_checksum:04X} in generation {generation + 1}!")
            print(f"Bytes: {bytes(population[index]).hex()}")
            break

        selected_indices = []
        for _ in range(population_size):
            tournament = random.sample(range(population_size), 5)
            tournament_fitness = [fitness_scores[i] for i in tournament]
            selected_indices.append(tournament[tournament_fitness.index(min(tournament_fitness))])

        new_population = []
        for _ in range(population_size // 2):
            parent1 = population[selected_indices.pop()]
            parent2 = population[selected_indices.pop()]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    else:
        print(f"No solution found for checksum 0x{desired_checksum:04X} after maximum generations.")
