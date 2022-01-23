import random

from Individual import Individual
from population import Population


class CrossBreeding:

    @staticmethod
    def getByName(name):
        _registered_crossbreeding_functions = {"onePoint": OnePointCrossing,
                                               "twoPoint": TwoPointCrossing}

        return _registered_crossbreeding_functions.get(name)

    def perform(self) -> Population:
        pass


class OnePointCrossing(CrossBreeding):

    def __init__(self, population: Population):
        self.oldPopulation = population

    def perform(self) -> Population:
        newPopulation = Population()
        populationLenght = len(self.oldPopulation.individuals)

        for i in range(populationLenght):
            mother = self.oldPopulation.individuals[i]
            father = self.oldPopulation.individuals[(i + 1) % populationLenght]
            newIndividual = OnePointCrossing.crossParents(mother, father)
            newPopulation.addIndividual(newIndividual)
        return newPopulation

    @staticmethod
    def crossParents(mother: Individual, father: Individual) -> Individual:
        crossingPoint = random.randint(1, len(mother.chromosome) - 2)
        motherChromosomePart = mother.chromosome[:crossingPoint]
        fatherChromosomePart = father.chromosome[crossingPoint:]
        newChromosome = motherChromosomePart + fatherChromosomePart
        newIndividual = Individual(initChromosome=False, chromosome=newChromosome)
        return newIndividual
class TwoPointCrossing(CrossBreeding):
    pass
