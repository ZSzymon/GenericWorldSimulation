from exceptions import WrongInitializeConditions
from settings import Settings
import random
from typing import List, Optional


class Individual:
    evaluationScore: int
    relativeEvaluationScore: int
    chromosome: List[int]
    genesInChromosome: int
    mutationChance: float
    genesMinVal: int
    genesMaxVal: int

    def __init__(self, config=Settings.config, initChromosome=True, performEvaluation=True,
                 chromosome: Optional[list] = None):
        Individual.checkChoosenConditions(initChromosome, performEvaluation, chromosome)
        self.genesInChromosome = config["genesInChromosome"]
        self.mutationChance = config["mutationChance"]
        self.genesMinVal = config["genesMinVal"]
        self.genesMaxVal = config["genesMaxVal"]
        self.chromosome = []
        if initChromosome:
            self.initializeChromosome(config["genesInChromosome"], config["genesMinVal"], config["genesMaxVal"])

        if performEvaluation:
            self.evaluationScore = self.performEvaluation()

        self.relativeEvaluationScore = None

    @staticmethod
    def checkChoosenConditions(initChromosome, performEvaluation, chromosome):
        if chromosome is None and not initChromosome:
            raise WrongInitializeConditions("You have to provide chromosome or accept to init chromosome")

    def initializeChromosome(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        for i in range(genesInChromosome):
            randValue = random.randint(geneMinVal, geneMaxVal)
            self.chromosome.append(randValue)

    def performEvaluation(self, evaluationFunction=None):
        if evaluationFunction is None:
            evaluationFunction = Settings.defaultEvaluationFunction

        self.evaluationScore = evaluationFunction(self)
        return self.evaluationScore

    @staticmethod
    def mutationFunction(oldChromosome, geneMinVal, geneMaxVal) -> List:
        randIndex = random.randint(0, len(oldChromosome) - 1)
        randValue = random.randint(geneMinVal, geneMaxVal)
        oldChromosome[randIndex] = randValue
        return oldChromosome

    def mutate(self, mutationFunction):
        newChromosome = mutationFunction(self.chromosome, self.genesMinVal, self.genesMaxVal)
        self.chromosome = newChromosome
