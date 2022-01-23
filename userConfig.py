import json
from dataclasses import dataclass


@dataclass
class Config:
    populationSize: int
    selectionFunction: str
    crossingFunctionName: str
    geneMinVal: int
    geneMaxVal: int
    genesInChromosome: int
    maxGeneration: int
    mutationChance: int

    @staticmethod
    def configFromFile(configPath, configType: str = "defaultConfig"):
        with open(configPath, "r") as jsonFile:
            config = json.load(jsonFile)
            configObj = Config(**config[configType])

        return configObj

    def __getitem__(self, item):
        return getattr(self, item)
