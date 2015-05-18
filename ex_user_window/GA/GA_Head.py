import numpy as np

GENE_LENGTH = 4
PRESENTATION_SIZE = 9
POPULATION_SIZE = 200
CROSSOVER_RATIO = 0.7
MUTATION_RATIO = 0.01

Individual = None


# class Head:
# 	def __init__(self):
# 		self.GENE_LENGTH = 4
# 		self.PRESENTATION_SIZE = 9
# 		self.POPULATION_SIZE = 200
# 		self.CROSSOVER_RATIO = 0.7
# 		self.MUTATION_RATIO = 0.01
#
# 		self.Individual = np.dtype({'names': ['pid', 'gene', 'evaluation'], 'formats': ['i', ('f', self.GENE_LENGTH), 'f']})
# Head = Head()

# def head(length):
# 	GENE_LENGTH = 4
# 	PRESENTATION_SIZE = 9
# 	POPULATION_SIZE = 200
# 	CROSSOVER_RATIO = 0.7
# 	MUTATION_RATIO = 0.01
#
# 	def set_length():
# 		GENE_LENGTH = length
#
# 	return set_length


def create_random_chromosome():
	return np.round(np.random.random(GENE_LENGTH), 2)


def calc_evaluation(individual, other):
	a = individual['gene'] - other
	individual['evaluation'] = a.dot(a)