import random
import settings
from typing import List

from Individual import Individual
from population import Population


class SelectionFunctionClass:

    @staticmethod
    def getByName(name):
        _registered_selection_functions = {"rouletteWheel": RouletteWheelSelectionClass,
                                           "ranking": RankingSelectionClass,
                                           "tournament": TournamentSelectionClass}

        return _registered_selection_functions.get(name)

    def perform(self) -> List[Individual]:
        pass


class RouletteWheelSelectionClass(SelectionFunctionClass):

    def __init__(self, population: Population, individualEvaluationFunction):
        self.population = population
        self.individualEvaluationFunction = individualEvaluationFunction

    def perform(self) -> List[Individual]:

        def findIndividual(_randScoreVal, _rangesValues):
            """Util function to find individual witch given randScoreVal is in his range."""
            for _range_val, _individual in _rangesValues.items():
                if _randScoreVal in _range_val:
                    return _individual
            return None

        individuals = self.population.individuals
        sumOfAllEvaluationScore = 0
        for individual in individuals:
            individual.performEvaluation(self.individualEvaluationFunction)
            sumOfAllEvaluationScore += individual.evaluationScore

        previousRangeBegin = 0
        maxRangeEnd = 0
        rangesValues = {}
        for individual in individuals:
            # It looks awful. I know. Individual score behaves acording to normal distribution.
            # Thats why they scores are similar.
            # Using int(individual.evaluationScore / sumOfAllEvaluationScore) almost alweys given 0.
            # thaths why making it 1000 biger before casting will give different numbers.
            ratio = (float(individual.evaluationScore) / float(sumOfAllEvaluationScore)) * 1000
            individual.relativeEvaluationScore = int(ratio)


            rangeValue = range(previousRangeBegin, previousRangeBegin + individual.relativeEvaluationScore+1)
            rangesValues[rangeValue] = individual
            previousRangeBegin += individual.relativeEvaluationScore
            maxRangeEnd = previousRangeBegin

        selectedIndividuals = []

        for i in range(len(individuals)):
            # Sub one to randScore raindint in order to find boundary example.
            # Range in python: range(0,100) == x in <0, 100)
            randScore = random.randint(0, maxRangeEnd-1)
            individual = findIndividual(randScore, rangesValues)
            selectedIndividuals.append(individual)



        return selectedIndividuals


class RankingSelectionClass(SelectionFunctionClass):

    def __init__(self, population: Population, individualEvaluationFunction=None):
        self.population = population
        self.individualEvaluationFunction = individualEvaluationFunction
        self.percentageWinnersOfRankingSelection = settings.percentageWinnersOfRankingSelection

    def perform(self) -> List[Individual]:
        self.population.performPopulationEvaluation(self.individualEvaluationFunction)
        individuals = self.population.individuals
        individuals = sorted(individuals, key=lambda individual: individual.evaluationScore)
        return individuals


class TournamentSelectionClass(SelectionFunctionClass):
    def __init__(self, population: Population, individualEvaluationFunction):
        self.population = population
        self.individualEvaluationFunction = individualEvaluationFunction
        self.tournamentSize = settings.config["tournamentSize"]

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
            bestIndividual = individualsList[0]
            for _individual in individualsList:
                if _individual.evaluationScore > bestIndividual.evaluationScore:
                    bestIndividual = _individual
            return bestIndividual

        bestIndividuals: List[Individual] = []
        for row in tournament:
            maxValueIndividual = getBestIndividual(row)
            bestIndividuals.append(maxValueIndividual)

        winner = getBestIndividual(bestIndividuals)
        return winner

    def perform(self) -> List[Individual]:
        selectionIndividuals: List[Individual] = []
        populationSize = len(self.population.individuals)

        while len(selectionIndividuals) < populationSize:
            tournamentWinner = self.performOneTournament()
            selectionIndividuals.append(tournamentWinner)

        return selectionIndividuals
