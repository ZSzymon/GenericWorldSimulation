from Individual import IndividualA, IndividualB
from crossBreeding import CrossBreeding
from evaluationFunction import IndividualEvaluateFunctions
from population import PopulationA, PopulationB
from selection import SelectionFunctionClass

from settings import Settings


class WorldA:

    def __init__(self):
        config = Settings.configA
        population = PopulationA(config)
        population.initializeIndividuals()
        evaluationFunctionName = config.evaluationFunction
        evaluationFunction = IndividualEvaluateFunctions.getByName(evaluationFunctionName)
        population.performPopulationEvaluation(evaluationFunction)
        selectionObject: SelectionFunctionClass = \
            SelectionFunctionClass.getByName(config["selectionFunction"])(population, evaluationFunction)
        crossingFunctionObject: CrossBreeding = CrossBreeding.getByName(config["crossingFunctionName"], "mode_a")(
            population, IndividualA)
        maxGeneration: int = config["maxGeneration"]
        currentGeneration: int = 0

        while currentGeneration < 1:
            selectedIndividuals: [IndividualA] = selectionObject.perform()
            crossingFunctionObject.population.individuals = selectedIndividuals
            newIndividuals = crossingFunctionObject.perform()
            population.individuals = newIndividuals
            population.performMutation()
            population.performPopulationEvaluation(IndividualEvaluateFunctions.evenBestOddWorst)
            currentGeneration += 1
            print(f"Best: {population.getBestIndividual().evaluationScore}")

class WorldB:


    def __init__(self):
        config = Settings.configB
        population = PopulationB()
        population.initializeIndividuals()
        evaluationFunctionName = config.evaluationFunction
        evaluationFunction = IndividualEvaluateFunctions.getByName(evaluationFunctionName)
        population.performPopulationEvaluation(evaluationFunction)
        selectionObject: SelectionFunctionClass = \
            SelectionFunctionClass.getByName(config["selectionFunction"])(population, evaluationFunction)
        crossingFunctionObject: CrossBreeding = CrossBreeding.getByName(config["crossingFunctionName"], "mode_b")(
            population,
            IndividualB)
        maxGeneration: int = config["maxGeneration"]
        currentGeneration: int = 0

        while currentGeneration < 20000:
            selectedIndividuals: [IndividualA] = selectionObject.perform()
            crossingFunctionObject.population.individuals = selectedIndividuals
            newIndividuals = crossingFunctionObject.perform()
            population.individuals = newIndividuals
            population.performMutation()
            population.performPopulationEvaluation(IndividualEvaluateFunctions.coefficientEvaluationFunction)
            currentGeneration += 1
            if currentGeneration % 100:
                print(f"Best: {population.getBestIndividual().evaluationScore}")


if __name__ == '__main__':
    # world = WorldA()

    worldB = WorldB()
