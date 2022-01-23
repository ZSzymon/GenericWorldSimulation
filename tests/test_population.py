import os
from unittest import TestCase
from population import Population
from settings import Settings
from userConfig import Config


class TestPopulation(TestCase):
    config = Config.configFromFile(os.path.join(Settings.CONFIG_DIR, "config.json"), 'testConfig')
    def test_create_population(self):
        population = Population()
        self.assertIsNotNone(population)

    def test_initialize_individuals(self):
        population = Population()
        population.initializeIndividuals()
        self.assertEqual(len(population.individuals), self.config.populationSize)


    def test_perform_population_evaluation(self):
        population = Population()
        population.initializeIndividuals()
        population.performPopulationEvaluation(Settings.defaultEvaluationFunction)
        self.assertTrue(all(individual.evaluationScore is not None for individual in population.individuals))