import random
from typing import List

from Individual import Individual
from population import Population
from settings import config


class SelectionFunction:

    @staticmethod
    def getByName(name):
        _registered_selection_functions = {"rouletteWheel": RouletteWheelSelection,
                                           "ranking": RankingSelection,

                                           "tournament": TournamentSelection}

        return _registered_selection_functions.get(name)


class RouletteWheelSelection(SelectionFunction):

    def __init__(self, population: Population, individualEvaluationFunction):
        self.population = population
        self.individualEvaluationFunction = individualEvaluationFunction

    def perform(self) -> List[Individual]:

        def findIndividual(_randScoreVal, _rangesValues):
            """Util function to find individual witch given randScoreVal is in his range."""
            for _range_val, _individual in _rangesValues.items():
                if _randScoreVal in _range_val:
                    return _individual

        individuals = self.population.individuals
        sumOfAllEvaluationScore = 0
        for individual in individuals:
            evaluationScore = individual.performEvaluation(self.individualEvaluationFunction)
            sumOfAllEvaluationScore += evaluationScore

        for individual in individuals:
            individual.relativeEvaluationScore = int(individual.evaluationScore / sumOfAllEvaluationScore)

        rangesValues = {}
        previousRangeBegin = 0
        for individual in individuals:
            rangeValue = range(previousRangeBegin, individual.relativeEvaluationScore)
            rangesValues[rangeValue] = individual

        selectedIndividuals = []

        for i in range(len(individuals)):
            randScore = random.randint(0, 100)
            individual = findIndividual(randScore, rangesValues)
            selectedIndividuals.append(individual)

        return selectedIndividuals


class RankingSelection(SelectionFunction):
    pass


class TournamentSelection(SelectionFunction):
    def __init__(self, population: Population, individualEvaluationFunction):
        self.population = population
        self.individualEvaluationFunction = individualEvaluationFunction
        self.tournamentSize = config["tournamentSize"]

    def performOneTournament(self):
        individuals = self.population.individuals
        tournament: List[List[Individual]] = []
        for i in range(self.tournamentSize):
            row = []
            for j in range(self.tournamentSize):
                randomIndividual = random.choice(individuals)
                randomIndividual.performEvaluation(self.individualEvaluationFunction)
                row.append(randomIndividual)
            tournament.append(row)

        def getBestIndividual(individualsList: List[Individual]) -> Individual:
            max = individualsList[0]
            for _individual in individualsList:
                if _individual.evaluationScore > max.evaluationScore:
                    max = _individual
            return max

        bestIndividuals: List[Individual] = []
        for row in tournament:
            maxValueIndividual = getBestIndividual(row)
            bestIndividuals.append(maxValueIndividual)

        winner = getBestIndividual(bestIndividuals)
        return winner

    def perform(self) -> List[Individual]:

        pass
