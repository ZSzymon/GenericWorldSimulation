import random

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

    def getBestIndividual(self):
        self.individuals = sorted(self.individuals, key=lambda individual: individual.evaluationScore)
        return self.individuals[0]

    def performPopulationEvaluation(self, evaluationFunction=None):
        if evaluationFunction is None:
            evaluationFunction = Settings.defaultEvaluationFunction

        populationScore = 0
        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
            populationScore += individual.evaluationScore
        self.populationScores.append(populationScore)


    def performMutation(self):
        for individual in self.individuals:
            if Individual.willMutate(1):
                individual.mutate(Individual.mutationFunction)
