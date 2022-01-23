from crossBreeding import CrossBreeding
from population import Population
from selection import SelectionFunction

from settings import Settings

class World:
    config = Settings.config
    population = Population(config)
    selectionFunction = SelectionFunction.getByName(config["selectionFunction"])
    crossingFunction = CrossBreeding.getByName(config["crossingFunctionName"])
    generationCounter: int = 0
    maxGeneration: int = config["maxGeneration"]


