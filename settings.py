import os
from evaluationFunction import IndividualEvaluateFunctions

from userConfig import Config


class Settings:
    PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_DIR = os.path.join(PROJECT_DIR, "config")

    #TODO:
    #   Implement config files for modes
    MODE_CHOICES = ["A", "B"]
    MODE = "A"

    config = Config.configFromFile(os.path.join(CONFIG_DIR, "config.json"))

    DEBUG = True
    if DEBUG:
        config = Config.configFromFile(os.path.join(CONFIG_DIR, "config.json"), "testConfig")


    # Default evaluation function for individual.
    defaultEvaluationFunction = IndividualEvaluateFunctions.evenBestOddWorst

    # Percentage of best individuals taken as winners in ranking selection.
    percentageWinnersOfRankingSelection: int = 50
