import random
from abc import abstractmethod
from typing import Tuple, List

from Individual import IndividualA, Individual, IndividualB
from population import PopulationA, PopulationB, Population


# TODO prapre for botch modes.

class CrossBreeding:

    def __init__(self, population: Population, IndividualClass):
        # self.selectedIndividuals: List[IndividualClass] = []
        self.oldPopulationLength = len(population.individuals)
        self.__currentClass__ = CrossBreeding
        self.__IndividualClass = IndividualClass

    @staticmethod
    def getByName(name, mode):
        _registered_crossbreeding_functions = {("onePoint".lower(), "mode_a"): OnePointCrossingA,
                                               ("twoPoint".lower(), "mode_a"): TwoPointCrossingA,
                                               ("onePoint".lower(), "mode_b"): OnePointCrossingB,
                                               ("twoPoint".lower(), "mode_b"): TwoPointCrossingB}

        return _registered_crossbreeding_functions.get((name.lower(), mode))

    def perform(self, selectedIndividuals, oldPopulationSize) -> List[Individual]:
        individuals = selectedIndividuals
        newGeneration: List[Individual] = []

        for i in range(0, oldPopulationSize - 1, 2):
            mother, father = self.getMotherAndFather(individuals, i)
            firstIndividual, secondIndividual = self.crossParents(mother, father)
            # assert (len(firstIndividual.chromosomes[0]) == 150)
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
        crossPoints = []
        for i in range(mother.chromosomesInIndividual):
            crossingPointBegin = random.randint(0, int(mother.genesInChromosome) - 2)
            crossPoints.append(crossingPointBegin)

        firstChromosome = cls.createChromosome(mother, father, crossPoints)
        secondChromosome = cls.createChromosome(father, mother, crossPoints)
        firstIndividual = type(mother)(initChromosomes=False, chromosomes=firstChromosome)
        secondIndividual = type(mother)(initChromosomes=False, chromosomes=secondChromosome)

        return firstIndividual, secondIndividual


class OnePointCrossingA(OnePointCrossing):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def createChromosome(cls, first: IndividualA, second: IndividualA, _crossingPoint) -> List[int]:
        stop = 1
        return first.chromosomes[:_crossingPoint[0]] + second.chromosomes[_crossingPoint[0]:]


class OnePointCrossingB(OnePointCrossing):

    def __init__(self, population: PopulationB, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def createChromosome(cls, first: IndividualB, second: IndividualB, _crossingPoints: List[int]) -> List[List[int]]:
        chromosomes = []
        for i, crossPoint in enumerate(_crossingPoints):
            chromosome = first.chromosomes[i][:crossPoint] + second.chromosomes[i][crossPoint:]
            chromosomes.append(chromosome)
            assert (len(chromosome) == len(first.chromosomes[i]))
        return chromosomes


class TwoPointCrossing(CrossBreeding):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @classmethod
    def crossParents(cls, mother: Individual, father: Individual) -> Tuple[Individual, Individual]:
        crossPoints = []
        for i in range(mother.chromosomesInIndividual):
            crossingPointBegin = random.randint(0, mother.genesInChromosome // 2)
            crossingPointEnd = random.randint(crossingPointBegin, int(mother.genesInChromosome) - 2)
            crossPoints.append((crossingPointBegin, crossingPointEnd))

        firstChromosome = cls.createChromosome(mother, father, crossPoints)
        secondChromosome = cls.createChromosome(father, mother, crossPoints)
        firstIndividual = type(mother)(initChromosomes=False, chromosomes=firstChromosome)
        secondIndividual = type(mother)(initChromosomes=False, chromosomes=secondChromosome)

        return firstIndividual, secondIndividual


class TwoPointCrossingA(TwoPointCrossing):

    def __init__(self, population: PopulationA, IndividualClass):
        super().__init__(population, IndividualClass)

    @staticmethod
    def createChromosome(first: Individual, seconds: Individual,
                         crossPoints) -> List[int]:
        crossingPointBegin, crossingPointEnd = crossPoints[0]
        return first.chromosomes[:crossingPointBegin] + \
               seconds.chromosomes[crossingPointBegin:crossingPointEnd] + \
               first.chromosomes[crossingPointEnd:]


class TwoPointCrossingB(TwoPointCrossing):

    def __init__(self, population: PopulationB, IndividualClass):
        super().__init__(population, IndividualClass)

    @staticmethod
    def createChromosome(first: Individual, seconds: Individual, _crossingPoints: List[Tuple[int, int]]) \
            -> List[List[int]]:
        chromosomes = []
        for i, crossPoint in enumerate(_crossingPoints):
            begin, end = crossPoint
            chromosome = first.chromosomes[i][:begin] + \
                         seconds.chromosomes[i][begin:end] + \
                         first.chromosomes[i][end:]
            chromosomes.append(chromosome)
        return chromosomes
