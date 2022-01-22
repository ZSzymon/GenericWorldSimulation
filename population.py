from typing import List

from Individual import Individual


class Population:
    individuals: List[Individual]

    def __init__(self, config):
        self.config = config

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config["populationSize"]):
            individual = Individual(self.config, i)
            individuals.append(individual)
        pass

