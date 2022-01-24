import random

from evaluationFunction import IndividualEvaluateFunctions
from settings import Settings
from typing import List
from Individual import IndividualA, IndividualB, Individual


class PopulationA:
    individuals: List[IndividualA]

    def __init__(self, config=None):
        if config is None:
            config = Settings.configA
        self.config = config
        self.individuals = []
        self.populationScores = []

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config.populationSize):
            individual = IndividualA(initChromosome=True, performEvaluation=True)
            individuals.append(individual)
        self.individuals = individuals

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def getBestIndividual(self):
        self.individuals = sorted(self.individuals, key=lambda individual: individual.evaluationScore)
        return self.individuals[0]

    def performPopulationEvaluation(self, evaluationFunction=None):
        if evaluationFunction is None:
            evaluationFunction = IndividualEvaluateFunctions.getByName(self.config.evaluationFunction)

        populationScore = 0
        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
            populationScore += individual.evaluationScore
        self.populationScores.append(populationScore)

    def performMutation(self):
        for individual in self.individuals:
            if IndividualA.willMutate(1):
                individual.mutate(IndividualA.mutationFunction)


class PopulationB:
    IndividualClass: Individual
    individuals: List[Individual]

    def __init__(self, config=Settings.configB):
        self.IndividualClass = IndividualB
        self.config = config
        self.individuals = []
        self.populationScores = []

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config.populationSize):
            individual = self.IndividualClass(initChromosome=True, performEvaluation=True)
            individuals.append(individual)
        self.individuals = individuals

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def getBestIndividual(self):
        self.individuals = sorted(self.individuals, key=lambda individual: individual.evaluationScore, reverse=True)
        return self.individuals[0]

    def performPopulationEvaluation(self, evaluationFunction=None):
        if evaluationFunction is None:
            evaluationFunction = IndividualEvaluateFunctions.getByName(self.config.evaluationFunction)

        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
            attractivityCoefficient = individual.attractivityCoefficient
            diseaseResistanceCoefficient = individual.diseaseResistanceCoefficient
        self.populationScores.append((attractivityCoefficient,diseaseResistanceCoefficient))

    def performMutation(self):
        for individual in self.individuals:
            if self.IndividualClass.willMutate(1):
                individual.mutate(IndividualA.mutationFunction)
