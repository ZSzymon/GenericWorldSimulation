from unittest import TestCase

from crossBreeding import OnePointCrossing, TwoPointCrossing
from population import Population


class TestOnePointCrossing(TestCase):

    def test_getMotherAndFather(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding: OnePointCrossing = OnePointCrossing(population)
        for i in range(0, len(crossBreeding.oldPopulation.individuals), 2):
            mother, father = OnePointCrossing.getMotherAndFather(crossBreeding.oldPopulation.individuals, i)

    def test_perform(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding = OnePointCrossing(population)
        newPopulation = crossBreeding.perform()
        self.assertEqual(len(population.individuals), len(newPopulation.individuals))

    def test1000Times_test_perform(self):
        for i in range(1000):
            self.test_perform()


class TestTwoPointCrossing(TestCase):

    def test_perform(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding = TwoPointCrossing(population)
        newPopulation = crossBreeding.perform()
        self.assertEqual(len(population.individuals), len(newPopulation.individuals))

    def test_getMotherAndFather(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding: TwoPointCrossing = TwoPointCrossing(population)
        for i in range(0, len(crossBreeding.oldPopulation.individuals), 2):
            mother, father = TwoPointCrossing.getMotherAndFather(crossBreeding.oldPopulation.individuals, i)

    def test1000Times_test_perform(self):
        for i in range(1000):
            self.test_perform()
