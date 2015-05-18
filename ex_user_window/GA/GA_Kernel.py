import random
import numpy as np

import GA_Head
from GA_Selection import binary_tournament as selection
from GA_Crossover import uniform as crossover
from GA_Mutation import mutation as mutation


def timeit(func):
	import time

	def wrapper(*args):
		start = time.clock()
		func(*args)
		end = time.clock()
		print 'used:', end - start

	return wrapper


def create_population(gene_list=None):
	return np.array([(
	                 i,
	                 GA_Head.create_random_chromosome() if gene_list is None else gene_list[i],
	                 0
		) for i in xrange(GA_Head.POPULATION_SIZE)
	], dtype=GA_Head.Individual)


def evaluation(pop, target):
	for el in pop:
		GA_Head.calc_evaluation(el, target)


def select_presentation(pop):
	presentation = random.sample(pop['pid'], GA_Head.PRESENTATION_SIZE)
	presentation[0] = 0
	return presentation


@timeit
def breeding(pop, elite):
	next_population_gene = []
	evaluation(pop, elite)

	while len(next_population_gene) < GA_Head.POPULATION_SIZE:
		mark = random.random()

		if mark < GA_Head.CROSSOVER_RATIO:
			p1 = selection(pop)
			p2 = selection(pop)

			(c1, c2) = crossover(p1, p2)
			next_population_gene.append(c1)
			next_population_gene.append(c2)
		else:
			p1 = selection(pop)
			next_population_gene.append(p1['gene'])

	pop[:] = create_population(next_population_gene)[:]
	mutation(pop)
