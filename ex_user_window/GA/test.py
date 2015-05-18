import GA_Head
import GA_Kernel


def test():
	g_number = 0
	population = GA_Kernel.create_population()
	target = GA_Head.create_random_chromosome()

	GA_Kernel.evaluation(population, target)
	min_evaluation = (0, min(population['evaluation']))
	no_evolve_count = 0

	while g_number < 800 and min_evaluation[1] > 0:
		print "Generation:%d->%f    Count->%d   Mutation->%.2f" % (
			g_number, min_evaluation[1], no_evolve_count, GA_Head.MUTATION_RATIO)

		GA_Kernel.breeding(population, target)
		g_number += 1

		GA_Kernel.evaluation(population, target)
		min_evaluation = (min_evaluation[1], min(population['evaluation']))

		if min_evaluation[0] == min_evaluation[1]:
			no_evolve_count += 1
		else:
			no_evolve_count = 0

		if no_evolve_count > 16:
			GA_Head.MUTATION_RATIO = 0.1
		else:
			GA_Head.MUTATION_RATIO = 0.01

test()
