import random
from abc import abstractmethod
from typing import Tuple, List

from Individual import IndividualA
from population import PopulationA


class CrossBreedingA:

    def __init__(self, population: PopulationA):
        self.population = population
        self.selectedIndividuals: List[IndividualA] = []
        self.oldPopulationLength = len(population.individuals)
        self.__currentClass__ = CrossBreedingA

    @staticmethod
    def getByName(name):
        _registered_crossbreeding_functions = {"onePoint".lower(): OnePointCrossing,
                                               "twoPoint".lower(): TwoPointCrossing}

        return _registered_crossbreeding_functions.get(name.lower())

    def _perform(self, CurrentClass) -> List[IndividualA]:
        individuals = self.population.individuals
        newGeneration: List[IndividualA] = []
        populationLength = self.oldPopulationLength

        for i in range(0, populationLength - 1, 2):
            mother, father = CurrentClass.getMotherAndFather(individuals, i)
            firstIndividual, secondIndividual = CurrentClass.crossParents(mother, father)
            newGeneration.append(firstIndividual)
            newGeneration.append(secondIndividual)
        return newGeneration

    @abstractmethod
    def perform(self) -> List[IndividualA]:
        """"""

    @staticmethod
    @abstractmethod
    def crossParents(first, second) -> Tuple[IndividualA, IndividualA]:
        """Method to perform parentCrossing."""

    @staticmethod
    def getMotherAndFather(individuals, i) -> Tuple[IndividualA, IndividualA]:
        # In selection function == ranking. N percentage of best individuals is selected to crossing.
        # This method is calling oldPopulation times. Thats why i >= len(individuals).
        # where individuals == selected N Percentage of best individuals.
        # That's why i%individualSize is used.
        individualsSize = len(individuals)
        mother = individuals[i % individualsSize]
        father = individuals[(i + 1) % individualsSize]

        return mother, father


class OnePointCrossing(CrossBreedingA):

    def __init__(self, population: PopulationA):
        super().__init__(population)

    def perform(self) -> List[IndividualA]:
        return super()._perform(OnePointCrossing)

    @staticmethod
    def crossParents(mother: IndividualA, father: IndividualA) -> Tuple[IndividualA, IndividualA]:
        crossingPoint = int(random.randint(1, len(mother.chromosome) - 2))
        firstChromosome = OnePointCrossing.createChromosome(mother, father, crossingPoint)
        secondChromosome = OnePointCrossing.createChromosome(father, mother, crossingPoint)
        firstIndividual = IndividualA(initChromosome=False, chromosome=firstChromosome,)
        secondIndividual = IndividualA(initChromosome=False, chromosome=secondChromosome)

        return firstIndividual, secondIndividual

    @staticmethod
    def createChromosome(first: IndividualA, second: IndividualA, _crossingPoint) -> List[int]:
        return first.chromosome[:_crossingPoint] + second.chromosome[_crossingPoint:]


class TwoPointCrossing(CrossBreedingA):

    def __init__(self, population: PopulationA):
        super().__init__(population)

    def perform(self) -> List[IndividualA]:
        return super()._perform(TwoPointCrossing)

    @staticmethod
    def crossParents(mother: IndividualA, father: IndividualA) -> Tuple[IndividualA, IndividualA]:
        crossingPointBegin = random.randint(0, int(len(mother.chromosome) / 2))
        crossingPointEnd = random.randint(crossingPointBegin, int(len(mother.chromosome))-2)

        firstChromosome = TwoPointCrossing.createChromosome(mother, father, crossingPointBegin, crossingPointEnd)
        secondChromosome = TwoPointCrossing.createChromosome(father, mother, crossingPointBegin, crossingPointEnd)
        firstIndividual = IndividualA(initChromosome=False, chromosome=firstChromosome)
        secondIndividual = IndividualA(initChromosome=False, chromosome=secondChromosome)

        return firstIndividual, secondIndividual

    @staticmethod
    def createChromosome(first: IndividualA, seconds: IndividualA,
                         crossingPointBegin, crossingPointEnd) -> List[int]:
        return first.chromosome[:crossingPointBegin] + \
               seconds.chromosome[crossingPointBegin:crossingPointEnd] + \
               first.chromosome[crossingPointEnd:]


