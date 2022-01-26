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

        while currentGeneration < maxGeneration:
            if len(population.individuals) <= 1:
                print("Population To small. ")
                break
            populationSize = len(population.individuals)
            selectedIndividuals: [IndividualB] = selectionObject.perform()
            if len(selectedIndividuals) <= 1:
                print("To less of selected Individuals.")
                break
            # crossingFunctionObject.population = population
            newIndividuals = crossingFunctionObject.perform(selectedIndividuals, populationSize)
            population.individuals = newIndividuals
            population.performMutation()
            population.performPopulationEvaluation(IndividualEvaluateFunctions.coefficientEvaluationFunction)
            population.performElemination()
            currentGeneration += 1

            if currentGeneration:
                print(f"Gen: {currentGeneration} " + population.printInfo())


if __name__ == '__main__':
    # world = WorldA()

    worldB = WorldB()
