import numpy as np
from const import *


def create_chromosome(template):
    chromosome_template = chromosome_templates[template]
    chromosome_data = np.random.random(len(chromosome_template)) * 2 - 1
    chromosome_data = np.round(chromosome_data, 2)

    for i, key in enumerate(chromosome_template):
        chromosome_template[key] = chromosome_data[i]

    chromosome = {}
    chromosome.update(chromosome_template)
    return chromosome


def create_individual(index, template):
    individual = {
        "index": index,
        "chromosome": create_chromosome(template),
        "evaluation": 0
    }
    return individual


def create_population(template):
    population = [
        create_individual(index, template) for index in xrange(POPULATION_SIZE)
    ]
    return population


def create_presentation(population):
    presentation = np.random.choice(population, PRESENTATION_SIZE, False)
    return presentation