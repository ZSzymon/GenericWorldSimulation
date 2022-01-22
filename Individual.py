import random
from typing import List


class Individual:
    evaluationScore: int
    relativeEvaluationScore: int
    chromosome: List[int]
    genesInChromosome: int
    mutationChance: float
    individualId: int
    genesMinVal: int
    genesMaxVal: int

    def __init__(self, config, individualId):
        self.genesInChromosome = config["genesInChromosome"]
        self.initializeChromosome(config["genesInChromosome"], config["geneMinVal"], config["geneMaxVal"])
        self.mutationChance = config["mutationChance"]
        self.individualId = individualId
        self.genesMinVal = config["genesMinVal"]
        self.genesMaxVal = config["genesMaxVal"]
        self.evaluationScore = None
        self.relativeEvaluationScore = None

    def initializeChromosome(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        for i in range(genesInChromosome):
            randValue = random.randint(geneMinVal, geneMaxVal)
            self.chromosome.append(randValue)

    def performEvaluation(self, evaluationFunction):
        self.evaluationScore = evaluationFunction(self)
        return self.evaluationScore

    def mutate(self, mutationFunction):
        newChromosome = mutationFunction(self.chromosome)
        self.chromosome = newChromosome
