from unittest import TestCase

from Individual import Individual
from exceptions import WrongInitializeConditions


class TestIndividual(TestCase):

    def test_initialize(self):
        individual = Individual()

    def test_check_choosen_conditions(self):
        with self.assertRaises(WrongInitializeConditions):
            Individual(initChromosome=False, performEvaluation=True)


    def test_initialize_chromosome(self):
        self.fail()

    def test_perform_evaluation(self):
        self.fail()

    def test_mutation_function(self):
        self.fail()

    def test_mutate(self):
        self.fail()
