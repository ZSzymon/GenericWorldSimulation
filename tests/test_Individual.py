from unittest import TestCase

from Individual import Individual
from exceptions import WrongInitializeConditions
from settings import Settings


class TestIndividual(TestCase):

    def test_initialize(self):
        individual = Individual()

    def test_check_choosen_conditions(self):
        with self.assertRaises(WrongInitializeConditions):
            Individual(initChromosome=False, performEvaluation=True)

    def test_initialize_chromosome(self):
        config = Settings.config
        individual = Individual(initChromosome=False, performEvaluation=False)
        individual.initializeChromosome(config.genesInChromosome, config.geneMinVal, config.geneMaxVal)

    def test_perform_evaluation(self):
        individual = Individual(initChromosome=True, performEvaluation=True)
        individual.performEvaluation()

    def test_mutation_function(self):
        individual = Individual(initChromosome=True, performEvaluation=True)
        individual.mutate(Individual.mutationFunction)

    def test_10000_mutation_function(self):
        for i in range(10000):
            self.test_mutation_function()

