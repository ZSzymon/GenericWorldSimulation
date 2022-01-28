import random

from evaluationFunction import IndividualEvaluateFunctions
from settings import Settings
from typing import List, Set
from Individual import IndividualA, Individual, IndividualB


class Population:
    individuals: List[Individual]

    def __init__(self, config, IndividualClass):
        self.IndividualClass = IndividualClass
        self.config = config
        self.individuals = []
        self.populationScores = []

    def initializeIndividuals(self):
        individuals = []
        for i in range(self.config.populationSize):
            individual = self.IndividualClass(initChromosomes=True, performEvaluation=True)
            individuals.append(individual)
        self.individuals = individuals

    def addIndividual(self, individual):
        self.individuals.append(individual)

    def performElemination(self):
        toEleminate: Set[Individual] = set()
        for individual in self.individuals:
            if individual.willBeEleminated():
                toEleminate.add(individual)
        oldPopulation = set(self.individuals)
        self.individuals = list(oldPopulation - toEleminate)

    def performMutation(self):
        for individual in self.individuals:
            if Individual.willMutate(1):
                individual.mutate(self.IndividualClass.mutationFunction)

    def performPopulationEvaluation(self, evaluationFunction=None):
        pass


class PopulationA(Population):

    def __init__(self, config=None):
        if config is None:
            config = Settings.configA
        super().__init__(config, IndividualA)

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


class PopulationB(Population):

    def __init__(self, IndividualClass=IndividualB, config=Settings.configB):
        super().__init__(config, IndividualClass)

    def getBestIndividual(self) -> Individual:
        self.individuals = sorted(self.individuals, key=lambda individual: individual.evaluationScore, reverse=True)
        return self.individuals[0]

    def performPopulationEvaluation(self, evaluationFunction=None):
        if evaluationFunction is None:
            evaluationFunction = IndividualEvaluateFunctions.getByName(self.config.evaluationFunction)
        attractivityCoefficient, diseaseResistanceCoefficient = 0, 0
        for individual in self.individuals:
            individual.performEvaluation(evaluationFunction)
            attractivityCoefficient = individual.attractivityCoefficient
            diseaseResistanceCoefficient = individual.diseaseResistanceCoefficient

        self.populationScores.append((attractivityCoefficient, diseaseResistanceCoefficient))

    def isHerdImmunity(self):
        return all(individual.attractivityCoefficient > .6 for individual in self.individuals)
    def printInfo(self):
        bestIndividual = self.getBestIndividual()
        populationLen = len(self.individuals)
        """    attractivityCoefficient: float
    diseaseResistanceCoefficient: float
"""

        info = f"Population size: {populationLen}\nBest: attractive -->{bestIndividual.attractivityCoefficient} : " \
               f"{bestIndividual.diseaseResistanceCoefficient}<-- diseaseResistance "

        if self.isHerdImmunity():
            info += f"Population begin: {self.config.populationSize}\n"
            info += f"Got herd immunity with: {len(self.individuals)*100//self.config.populationSize}% of population"
        return info+"\n"
