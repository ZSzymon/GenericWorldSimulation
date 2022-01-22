from typing import List

from Individual import Individual

class IndividualEvaluateFunctions:

    @staticmethod
    def evenBestOddWorst(individual: Individual) -> int:
        chromosome = individual.chromosome
        evaluationScore = 0

        def isEven(index):
            return index % 2 == 0

        for i, gene in enumerate(chromosome):
            if isEven(i):
                evaluationScore += gene - individual.genesMinVal
            else:
                evaluationScore += individual.genesMaxVal - gene
        return evaluationScore

