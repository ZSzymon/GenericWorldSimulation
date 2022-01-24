import os
from unittest import TestCase
from population import PopulationA
from settings import Settings
from userConfig import Config


class TestPopulation(TestCase):
    config = Config.configFromFile(os.path.join(Settings.CONFIG_DIR, "config.json"), 'testConfig')
    def test_create_population(self):
        population = PopulationA()
        self.assertIsNotNone(population)

    def test_initialize_individuals(self):
        population = PopulationA()
        population.initializeIndividuals()
        self.assertEqual(len(population.individuals), self.config.populationSize)


    def test_perform_population_evaluation(self):
        population = PopulationA()
        population.initializeIndividuals()
        population.performPopulationEvaluation(Settings.defaultEvaluationFunction)
        self.assertTrue(all(individual.evaluationScore is not None for individual in population.individuals))