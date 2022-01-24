from Individual import Individual
from crossBreeding import CrossBreeding
from evaluationFunction import IndividualEvaluateFunctions
from population import Population
from selection import SelectionFunctionClass

from settings import Settings


class WorldA:
    config = Settings.config
    population = Population(config)
    population.initializeIndividuals()
    population.performPopulationEvaluation()
    evaluationFunction = IndividualEvaluateFunctions.getByName("evenBestOddWorst")
    selectionObject: SelectionFunctionClass = \
        SelectionFunctionClass.getByName(config["selectionFunction"])(population, evaluationFunction)
    crossingFunctionObject: CrossBreeding = CrossBreeding.getByName(config["crossingFunctionName"])(population)
    maxGeneration: int = config["maxGeneration"]
    currentGeneration: int = 0

    while currentGeneration < maxGeneration:
        selectedIndividuals: [Individual] = selectionObject.perform()
        crossingFunctionObject.population.individuals = selectedIndividuals
        newIndividuals = crossingFunctionObject.perform()
        population.individuals = newIndividuals
        population.performMutation()
        population.performPopulationEvaluation(IndividualEvaluateFunctions.evenBestOddWorst)
        currentGeneration += 1
        if currentGeneration % 10:
            print(f"Best: {population.getBestIndividual().evaluationScore}")


if __name__ == '__main__':
    world = WorldA()
