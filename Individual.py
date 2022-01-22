import random
from typing import List


class Individual:
    chromosome: List[int]
    genesInChromosome: int

    def __init__(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        self.genesInChromosome = genesInChromosome
        self.initializeChromosome(genesInChromosome, geneMinVal, geneMaxVal)

    def initializeChromosome(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        for i in range(genesInChromosome):
            randValue = random.randint(geneMinVal, geneMaxVal)
            self.chromosome.append(randValue)
