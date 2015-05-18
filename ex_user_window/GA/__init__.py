__author__ = 'Loaias'

import GA_Head
import numpy as np
from GA_Kernel import create_population, select_presentation, evaluation, breeding


class GAHelper:
	def __init__(self):
		self.population = create_population()
		self.presentation = select_presentation(self.population)

	def do_evolve(self, elite):
		evaluation(self.population, elite)
		breeding(self.population, elite)
		self.presentation = select_presentation(self.population)

	def get_presentation(self):
		return self.population[self.presentation]['gene']

	@staticmethod
	def set_gene_length(length):
		GA_Head.GENE_LENGTH = length

		GA_Head.Individual = np.dtype({'names': ['pid', 'gene', 'evaluation'], 'formats': ['i', ('f', length), 'f']})

	@staticmethod
	def get_gene_length():
		return GA_Head.GENE_LENGTH
