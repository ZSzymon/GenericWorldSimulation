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
        crossingFunctionClass: CrossBreeding = CrossBreeding.getByName(config["crossingFunctionName"], "mode_a")
        crossingFunctionObject = crossingFunctionClass(population, IndividualA)
        maxGeneration: int = config["maxGeneration"]
        currentGeneration: int = 0

        while currentGeneration < maxGeneration:
            selectedIndividuals: [IndividualA] = selectionObject.perform()
            populationSize = len(population.individuals)
            newIndividuals = crossingFunctionObject.perform(selectedIndividuals, populationSize)
            population.individuals = newIndividuals
            population.performMutation()
            population.performPopulationEvaluation(IndividualEvaluateFunctions.evenBestOddWorst)
            currentGeneration += 1
            print(f"Best: {population.getBestIndividual().evaluationScore}")


class WorldB:
    data = []

    def __init__(self):
        self.population = PopulationB()
        self.population.initializeIndividuals()
        self.config = Settings.configB
        self.evaluationFunctionName = self.config.evaluationFunction
        self.evaluationFunction = IndividualEvaluateFunctions.getByName(self.evaluationFunctionName)
        self.population.performPopulationEvaluation(self.evaluationFunction)
        self.selectionObject: SelectionFunctionClass = \
            SelectionFunctionClass.getByName(self.config["selectionFunction"])(self.population, self.evaluationFunction)
        self.crossingFunctionObject: CrossBreeding = CrossBreeding.getByName(self.config["crossingFunctionName"],
                                                                             "mode_b")(
            self.population,
            IndividualB)
        self.maxGeneration: int = self.config["maxGeneration"]

    def run(self):
        isAlive = True
        currentGeneration: int = 0
        self.population.reinitIndividuals()
        while currentGeneration < self.maxGeneration:
            if len(self.population.individuals) <= 1:
                print("Population to small. ")
                isAlive = False
                break
            populationSize = len(self.population.individuals)
            selectedIndividuals: [IndividualB] = self.selectionObject.perform()
            if len(selectedIndividuals) <= 1:
                print("To less of selected Individuals.")
                isAlive = False
                break
            newIndividuals = self.crossingFunctionObject.perform(selectedIndividuals, populationSize)
            self.population.individuals = newIndividuals
            self.population.performMutation()
            self.population.performPopulationEvaluation(IndividualEvaluateFunctions.coefficientEvaluationFunction)
            self.population.performElemination()

            if self.population.isHerdImmunity():
                isAlive = True
                break
            currentGeneration += 1
        return self.population.getStatistic(), currentGeneration, 1 if isAlive else 0


from statistics import mean, StatisticsError

if __name__ == '__main__':
    # world = WorldA()



    print("Population survived in : " + str(mean([i[2] for i in data]) * 100) + "%")
