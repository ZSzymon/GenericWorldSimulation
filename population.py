from settings import Settings
from typing import List
from Individual import Individual


class Population:
    individuals: List[Individual]

    def __init__(self, config=None):
        if config is None:
            config = Settings.config
        self.config = config
        self.individuals = []
        self.populationScores = []

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config.populationSize):
            individual = Individual(initChromosome=True, performEvaluation=True, )
            individuals.append(individual)
        self.individuals = individuals

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def performPopulationEvaluation(self, evaluationFunction=None):
        populationScore = 0
        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
            populationScore += individual.evaluationScore
        self.populationScores.append(populationScore)
