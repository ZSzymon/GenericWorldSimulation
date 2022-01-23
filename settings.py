import os
from evaluationFunction import IndividualEvaluateFunctions

from userConfig import Config

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIR = os.path.join(PROJECT_DIR, "config")

config = Config.configFromFile()

# Default evaluation function for individual.
defaultEvaluationFunction = IndividualEvaluateFunctions.evenBestOddWorst

# Percentage of best individuals taken as winners in ranking selection.
percentageWinnersOfRankingSelection: int = 50
