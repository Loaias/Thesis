import random


def roulette(pop, p0_id):
    accumulated = random.random()
    flags = pop['evaluation'] > accumulated
    p1 = pop[flags][0]

    if p1['pid'] == p0_id:
        p1 = roulette(pop, p0_id)

    return p1


def binary_tournament(pop):
    (p1, p2) = random.sample(pop, 2)
    if p1['evaluation'] > p2['evaluation']:
        return p2
    else:
        return p1
