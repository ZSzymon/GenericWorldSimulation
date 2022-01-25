from unittest import TestCase

from Individual import IndividualA
from exceptions import WrongInitializeConditions
from settings import Settings


class TestIndividual(TestCase):

    def test_initialize(self):
        individual = IndividualA()

    def test_check_choosen_conditions(self):
        with self.assertRaises(WrongInitializeConditions):
            IndividualA(initChromosomes=False, performEvaluation=True)

    def test_initialize_chromosome(self):
        config = Settings.config
        individual = IndividualA(initChromosomes=False, performEvaluation=False)
        individual.initializeChromosome(config.genesInChromosome, config.geneMinVal, config.geneMaxVal)

    def test_perform_evaluation(self):
        individual = IndividualA(initChromosomes=True, performEvaluation=True)
        individual.performEvaluation()

    def test_mutation_function(self):
        individual = IndividualA(initChromosomes=True, performEvaluation=True)
        individual.mutate(IndividualA.mutationFunction)

    def test_10000_mutation_function(self):
        for i in range(10000):
            self.test_mutation_function()

