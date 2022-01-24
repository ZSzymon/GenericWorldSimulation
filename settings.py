import os
from evaluationFunction import IndividualEvaluateFunctions
from userConfig import Config

class Settings:
    PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_DIR = os.path.join(PROJECT_DIR, "config")


    DEBUG = True
    MODE_CHOICES = ["A", "B", "C"]
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


