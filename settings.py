import os
from evaluationFunction import IndividualEvaluateFunctions
from userConfig import Config

class Settings:
    PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_DIR = os.path.join(PROJECT_DIR, "config")
    DEBUG = False

    CONFIG_FILE_PATH_A = os.path.join(CONFIG_DIR, "configA.json")
    CONFIG_FILE_PATH_B = os.path.join(CONFIG_DIR, "configB.json")

    if DEBUG:
        configA = Config.configFromFile(CONFIG_FILE_PATH_A, "testConfig")
    else:
        configA = Config.configFromFile(CONFIG_FILE_PATH_A)

    if DEBUG:
        configB = Config.configFromFile(CONFIG_FILE_PATH_B, "testConfig")
    else:
        configB = Config.configFromFile(CONFIG_FILE_PATH_B)


