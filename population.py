import settings
from typing import List


from Individual import Individual


class Population:
    individuals: List[Individual]

    def __init__(self, config=None):
        if config is None:
            config = settings.config
        self.config = config

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config["populationSize"]):
            individual = Individual(initChromosome=True, performEvaluation=True,)
            individuals.append(individual)
        pass

    def addIndividual(self, individual):
        self.individuals.append(individual)
    def performPopulationEvaluation(self, evaluationFunction=None):
        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
