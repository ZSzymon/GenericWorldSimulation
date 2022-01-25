from unittest import TestCase

from crossBreeding import OnePointCrossingA, TwoPointCrossingA
from population import PopulationA


class TestOnePointCrossing(TestCase):

    def test_getMotherAndFather(self):
        population = PopulationA()
        population.initializeIndividuals()
        crossBreeding: OnePointCrossingA = OnePointCrossingA(population)
        for i in range(0, len(crossBreeding.oldPopulation.individuals), 2):
            mother, father = OnePointCrossingA.getMotherAndFather(crossBreeding.oldPopulation.individuals, i)

    def test_perform(self):
        population = PopulationA()
        population.initializeIndividuals()
        crossBreeding = OnePointCrossingA(population)
        newPopulation = crossBreeding.perform()
        self.assertEqual(len(population.individuals), len(newPopulation.individuals))

    def test1000Times_test_perform(self):
        for i in range(1000):
            self.test_perform()


class TestTwoPointCrossing(TestCase):

    def test_perform(self):
        population = PopulationA()
        population.initializeIndividuals()
        crossBreeding = TwoPointCrossingA(population)
        newPopulation = crossBreeding.perform()
        self.assertEqual(len(population.individuals), len(newPopulation.individuals))

    def test_getMotherAndFather(self):
        population = PopulationA()
        population.initializeIndividuals()
        crossBreeding: TwoPointCrossingA = TwoPointCrossingA(population)
        for i in range(0, len(crossBreeding.oldPopulation.individuals), 2):
            mother, father = TwoPointCrossingA.getMotherAndFather(crossBreeding.oldPopulation.individuals, i)

    def test1000Times_test_perform(self):
        for i in range(1000):
            self.test_perform()
