import os
import json
from dataclasses import dataclass
from settings import CONFIG_DIR

@dataclass
class Config:
    populationSize: int
    selectionMethod: str
    crossingFunctionName: str
    genesMinVal: int
    genesMaxVal: int
    genesInChromosome: int

    @staticmethod
    def configFromFile(configPath=None, configType: str = "defaultConfig"):
        if configPath is None:
            configPath = os.path.join(CONFIG_DIR, "config.json")
        config = None
        with open(configPath, "r") as jsonFile:
            config = json.load(jsonFile)
            configObj = Config(**config[configType])

        return configObj
