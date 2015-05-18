import GA_Head
import numpy as np


def uniform(p1, p2):
    flags = np.random.random(GA_Head.GENE_LENGTH) < GA_Head.CROSSOVER_RATIO

    (c1, c2) = ([], [])

    for i in xrange(GA_Head.GENE_LENGTH):
        c1.append(p1['gene'][i] if flags[i] else p2['gene'][i])
        c2.append(p2['gene'][i] if flags[i] else p1['gene'][i])

    return c1, c2