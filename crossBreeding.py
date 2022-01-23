import random
from abc import abstractmethod
from typing import Tuple, List

from Individual import Individual
from population import Population


class CrossBreeding:

    def __init__(self, oldPopulation):
        self.oldPopulation = oldPopulation
        self.__currentClass__ = CrossBreeding

    @staticmethod
    def getByName(name):
        _registered_crossbreeding_functions = {"onePoint": OnePointCrossing,
                                               "twoPoint": TwoPointCrossing}

        return _registered_crossbreeding_functions.get(name)

    def _perform(self, CurrentClass) -> Population:
        newPopulation = Population()
        populationLenght = len(self.oldPopulation.individuals)

        for i in range(0, populationLenght - 1, 2):
            mother, father = CurrentClass.getMotherAndFather(self.oldPopulation.individuals, i)
            firstIndividual, secondIndividual = CurrentClass.crossParents(mother, father)
            newPopulation.addIndividual(firstIndividual)
            newPopulation.addIndividual(secondIndividual)
        return newPopulation

    @abstractmethod
    def perform(self) -> Population:
        """"""

    @staticmethod
    @abstractmethod
    def crossParents(first, second) -> Tuple[Individual, Individual]:
        """Method to perform parentCrossing."""

    @staticmethod
    def getMotherAndFather(individuals, i) -> Tuple[Individual, Individual]:
        populationLenght = len(individuals)
        # TODO % populationLenght
        mother = individuals[i]
        father = individuals[(i + 1)]
        return mother, father


class OnePointCrossing(CrossBreeding):

    def __init__(self, population: Population):
        super().__init__(population)

    def perform(self) -> Population:
        return super()._perform(OnePointCrossing)

    @staticmethod
    def crossParents(mother: Individual, father: Individual) -> Tuple[Individual, Individual]:
        crossingPoint = int(random.randint(1, len(mother.chromosome) - 2))
        firstChromosome = OnePointCrossing.createChromosome(mother, father, crossingPoint)
        secondChromosome = OnePointCrossing.createChromosome(father, mother, crossingPoint)
        firstIndividual = Individual(initChromosome=False, chromosome=firstChromosome)
        secondIndividual = Individual(initChromosome=False, chromosome=secondChromosome)

        return firstIndividual, secondIndividual

    @staticmethod
    def createChromosome(first: Individual, second: Individual, _crossingPoint) -> List[int]:
        return first.chromosome[:_crossingPoint] + second.chromosome[_crossingPoint:]


class TwoPointCrossing(CrossBreeding):

    def __init__(self, population: Population):
        super().__init__(population)

    def perform(self) -> Population:
        return super()._perform(TwoPointCrossing)

    @staticmethod
    def crossParents(mother: Individual, father: Individual) -> Tuple[Individual, Individual]:
        crossingPointBegin = random.randint(0, int(len(mother.chromosome) / 2))
        crossingPointEnd = random.randint(crossingPointBegin, int(len(mother.chromosome)))

        firstChromosome = TwoPointCrossing.createChromosome(mother, father, crossingPointBegin, crossingPointEnd)
        secondChromosome = TwoPointCrossing.createChromosome(father, mother, crossingPointBegin, crossingPointEnd)
        firstIndividual = Individual(initChromosome=False, chromosome=firstChromosome)
        secondIndividual = Individual(initChromosome=False, chromosome=secondChromosome)

        return firstIndividual, secondIndividual

    @staticmethod
    def createChromosome(first: Individual, seconds: Individual,
                         crossingPointBegin, crossingPointEnd) -> List[int]:
        return first.chromosome[:crossingPointBegin] + \
               seconds.chromosome[crossingPointBegin:crossingPointEnd] + \
               first.chromosome[crossingPointEnd:]
