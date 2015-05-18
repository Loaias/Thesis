from creater import np, POPULATION_SIZE, CROSSOVER_RATIO, MUTATION_RATIO


def evaluation(population, elite):
    """
    do evaluation before evolve
    if the evaluation is smaller, the individual is better
    :param population:
    :param elite: a chromosome
    """
    for individual in population:
        chromosome = np.array(individual["chromosome"].values())
        difference = chromosome - np.array(elite.values())
        individual["evaluation"] = difference.dot(difference)


def breeding(population, elite):
    next_population_chromosome = []
    evaluation(population, elite)

    flags = np.random.random(POPULATION_SIZE) < CROSSOVER_RATIO

    while len(next_population_chromosome) < POPULATION_SIZE:
        if flags[len(next_population_chromosome)] < CROSSOVER_RATIO:
            parent_chromosome1 = selection(population)
            parent_chromosome2 = selection(population)

            child_chromosome1, child_chromosome2 = crossover(parent_chromosome1, parent_chromosome2)
            next_population_chromosome.append(child_chromosome1)
            next_population_chromosome.append(child_chromosome2)
        else:
            parent_chromosome = selection(population)
            next_population_chromosome.append(parent_chromosome)

    for i, individual in enumerate(population):
        individual["chromosome"].update(next_population_chromosome[i])

    mutation(population)


def selection(population):
    """
    binary_tournament
    :param population:
    :return: selected chromosome
    """
    (p1, p2) = np.random.choice(population, 2, False)
    return p1["chromosome"] if p1["evaluation"] < p2["evaluation"] else p2["chromosome"]


def crossover(p1, p2):
    """
    uniform crossover
    :param p1: parent_chromosome1
    :param p2: parent_chromosome2
    :return: child chromosomes
    """
    chromosome_length = len(p1)
    flags = np.random.random(chromosome_length) < 0.5

    c1, c2 = {}, {}

    for i, key in enumerate(p1):
        c1[key], c2[key] = (p1[key], p2[key]) if flags[i] else (p2[key], p1[key])

    return c1, c2

def mutation(population):
    chromosome = selection(population)

    chromosome_length = len(chromosome)
    flags = np.random.random(chromosome_length) < MUTATION_RATIO

    random_chromosome = np.random.random(chromosome_length) * 2 - 1
    random_chromosome = np.round(random_chromosome, 2)

    for i, key in enumerate(chromosome):
        if flags[i]:
            chromosome[key] = random_chromosome[i]