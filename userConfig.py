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
    tournamentSize: int
    percentageWinnersOfRankingSelection: int
    evaluationFunction: str
    chromosomesInIndividual:int

    @staticmethod
    def configFromFile(configPath, configType: str = "defaultConfig"):
        with open(configPath, "r") as jsonFile:
            configFile = json.load(jsonFile)
            configObj = Config(**configFile[configType])

        return configObj

    def __getitem__(self, item):
        return getattr(self, item)

