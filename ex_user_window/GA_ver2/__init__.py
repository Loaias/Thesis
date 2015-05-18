from creater import create_population, create_presentation, create_chromosome
from evolver import evaluation, breeding


class Genetic_Algorithm:
    def __init__(self, template):

        self.population = None
        self.presentation = None
        self.template = template

        self.init()

    def init(self):
        self.population = create_population(self.template)
        self.presentation = create_presentation(self.population)

    def do_evolve(self, elite_index):
        elite = self.presentation[elite_index]
        elite_chromosome = elite["chromosome"]
        evaluation(self.population, elite_chromosome)
        breeding(self.population, elite_chromosome)
        self.presentation = create_presentation(self.population)

    #******************************************************************************************************************
    # For Test
    def create_test_chromosome(self):
        return create_chromosome(self.template)

    def get_best_evaluation(self):
        return sorted(self.population, key=lambda individual: individual["evaluation"])[0]["evaluation"]
    #******************************************************************************************************************