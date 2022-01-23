import os
from evaluationFunction import IndividualEvaluateFunctions

from userConfig import Config


class Settings:
    PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_DIR = os.path.join(PROJECT_DIR, "config")

    #TODO:
    #   Implement config files for modes
    DEBUG = True
    MODE_CHOICES = ["A", "B"]
    MODE = "A"

    CONFIG_FILE_PATH: str = ""

    if MODE == "A":
        CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "config.json")

    if MODE == "B":
        CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "configB.json")

    if DEBUG:
        config = Config.configFromFile(CONFIG_FILE_PATH, "testConfig")
    else:
        config = Config.configFromFile(CONFIG_FILE_PATH)







    # Default evaluation function for individual.
    defaultEvaluationFunction = IndividualEvaluateFunctions.evenBestOddWorst

    # Percentage of best individuals taken as winners in ranking selection.
    percentageWinnersOfRankingSelection: int = 50
