from unittest import TestCase

from crossBreeding import OnePointCrossing
from population import Population


class TestOnePointCrossing(TestCase):


    def test_cross_parents(self):
        population = Population()
        population.initializeIndividuals()
        crossingPoint = int(len(population.individuals)/2)
        mother, father = OnePointCrossing.getMotherAndFather(population.individuals, 9)
        child = OnePointCrossing.crossParents(mother, father, crossingPoint)
        motherChromosomePart = mother.chromosome[:crossingPoint]
        fatherChromosomePart = father.chromosome[crossingPoint:]

        self.assertEqual(child.chromosome, motherChromosomePart+fatherChromosomePart)

    def test_getMotherAndFather(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding: OnePointCrossing = OnePointCrossing(population)
        for i in range(len(crossBreeding.oldPopulation.individuals)):
            mother, father = OnePointCrossing.getMotherAndFather(crossBreeding.oldPopulation.individuals, i)

    def test_perform(self):
        population = Population()
        population.initializeIndividuals()
        crossBreeding = OnePointCrossing(population)
        newPopulation = crossBreeding.perform()
        self.assertEqual(len(population.individuals), len(newPopulation.individuals))

