import random
from abc import abstractmethod
from typing import Tuple, List

from Individual import IndividualA, Individual, IndividualB
from population import PopulationA, PopulationB, Population


# TODO prapre for botch modes.

class CrossBreeding:

    def __init__(self, population: Population, IndividualClass):
        self.population = population
        self.selectedIndividuals: List[IndividualClass] = []
        self.oldPopulationLength = len(population.individuals)
        self.__currentClass__ = CrossBreeding
        self.__IndividualClass = IndividualClass

    @staticmethod
    def getByName(name):
        _registered_crossbreeding_functions = {"onePoint".lower(): OnePointCrossingA,
                                               "twoPoint".lower(): TwoPointCrossingA}

        return _registered_crossbreeding_functions.get(name.lower())

    def perform(self) -> List[Individual]:
        individuals = self.population.individuals
        newGeneration: List[Individual] = []
        populationLength = self.oldPopulationLength
        for i in range(0, populationLength - 1, 2):
            mother, father = self.getMotherAndFather(individuals, i)
            firstIndividual, secondIndividual = self.crossParents(mother, father)
            newGeneration.append(firstIndividual)
            newGeneration.append(secondIndividual)
        return newGeneration

    @staticmethod
    def getMotherAndFather(individuals, i) -> Tuple[Individual, Individual]:
        # In selection function == ranking. N percentage of best individuals is selected to crossing.
        # This method is calling oldPopulation times. That's why i >= len(individuals).
        # where individuals == selected N Percentage of best individuals.
        # That's why i%individualSize is used.
        individualsSize = len(individuals)
        mother = individuals[i % individualsSize]
        father = individuals[(i + 1) % individualsSize]

        return mother, father


class OnePointCrossing(CrossBreeding):

    @classmethod
    def crossParents(cls, mother, father) -> Tuple[Individual, Individual]:
        crossingPoint = random.randint(0, mother.genesInChromosome // 2)

        firstChromosome = cls.createChromosome(mother, father, crossingPoint)
        secondChromosome = cls.createChromosome(father, mother, crossingPoint)
        firstIndividual = type(mother)(initChromosomes=False, chromosomes=firstChromosome)
        secondIndividual = type(mother)(initChromosomes=False, chromosomes=secondChromosome)

        return firstIndividual, secondIndividual


class OnePointCrossingA(OnePointCrossing):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def createChromosome(cls, first: IndividualA, second: IndividualA, _crossingPoint) -> List[int]:
        return first.chromosomes[:_crossingPoint] + second.chromosomes[_crossingPoint:]

class OnePointCrossingB(OnePointCrossing):

    def __init__(self, population: PopulationB, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def createChromosome(cls, first: IndividualB, second: IndividualB, _crossingPoints: List[int]) -> List[List[int]]:
        chromosomes = []
        for i, crossPoint in _crossingPoints:
            chromosome = first.chromosomes[i][:crossPoint] + second.chromosomes[i][:crossPoint]
            chromosomes.append(chromosome)
        return chromosomes


class TwoPointCrossing(CrossBreeding):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def crossParents(cls, mother, father) -> Tuple[Individual, Individual]:
        crossingPointBegin = random.randint(0, mother.genesInChromosome // 2)
        crossingPointEnd = random.randint(crossingPointBegin, int(len(mother.chromosomes)) - 2)

        firstChromosome = cls.createChromosome(mother, father, crossingPointBegin, crossingPointEnd)
        secondChromosome = cls.createChromosome(father, mother, crossingPointBegin, crossingPointEnd)
        firstIndividual = type(mother)(initChromosomes=False, chromosomes=firstChromosome)
        secondIndividual = type(mother)(initChromosomes=False, chromosomes=secondChromosome)

        return firstIndividual, secondIndividual


class TwoPointCrossingA(TwoPointCrossing):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @staticmethod
    def createChromosome(first: IndividualA, seconds: IndividualA,
                         crossingPointBegin, crossingPointEnd) -> List[int]:
        return first.chromosomes[:crossingPointBegin] + \
               seconds.chromosomes[crossingPointBegin:crossingPointEnd] + \
               first.chromosomes[crossingPointEnd:]


class TwoPointCrossingB(CrossBreeding):

    def __init__(self, population: PopulationB, IndividualClass):
        super().__init__(population, IndividualClass)

    @staticmethod
    def createChromosome(first: Individual, seconds: Individual, _crossingPoints: List[Tuple[int, int]]) \
            -> List[List[int]]:
        chromosomes = []
        for i, crossPoint in enumerate(_crossingPoints):
            chromosome = first.chromosomes[i][:crossPoint[0]] + \
                         seconds.chromosomes[i][crossPoint[0]:crossPoint[1]] + \
                         first.chromosomes[i][crossPoint[1]:]
            chromosomes.append(chromosome)
        return chromosomes
