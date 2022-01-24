class IndividualEvaluateFunctions:


    @staticmethod
    def getByName(name):
        _registered_functions = {"evenBestOddWorst".lower(): IndividualEvaluateFunctions.evenBestOddWorst}
        return _registered_functions[name.lower()]

    @staticmethod
    def evenBestOddWorst(individual) -> int:
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
