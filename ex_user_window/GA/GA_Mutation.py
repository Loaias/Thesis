import random
import GA_Head
import numpy as np


def mutation(pop):
    matrix = pop['gene'].reshape(-1, 1)
    count = len(matrix)
    flags = np.random.random(count) < GA_Head.MUTATION_RATIO

    matrix[flags] = random.random()
    pop['gene'] = matrix.reshape(-1, GA_Head.GENE_LENGTH)
