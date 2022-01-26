class IndividualEvaluateFunctions:

    @staticmethod
    def getByName(name):
        _registered_functions = {"evenBestOddWorst".lower(): IndividualEvaluateFunctions.evenBestOddWorst,
                                 "coefficientevaluationfunction": IndividualEvaluateFunctions.coefficientEvaluationFunction}
        return _registered_functions[name.lower()]

    @staticmethod
    def evenBestOddWorst(individual) -> int:
        chromosome = individual.chromosomes
        evaluationScore = 0

        def isEven(index):
            return index % 2 == 0

        for i, gene in enumerate(chromosome):
            if isEven(i):
                evaluationScore += gene - individual.genesMinVal
            else:
                evaluationScore += individual.genesMaxVal - gene
        return evaluationScore

    @staticmethod
    def _evaluateAttractiveness(attractivenessChromosome, geneMaxVal):
        maxAttractivenessScore = (geneMaxVal * (151 - 90) / 2) + geneMaxVal * (56 - 10)
        attractivenessScore = sum(geneVal for geneVal in attractivenessChromosome[10:56]) + \
                              sum(geneVal / 2 for geneVal in attractivenessChromosome[90:151])
        attractivenessCoefficient = attractivenessScore / maxAttractivenessScore
        return attractivenessCoefficient

    @staticmethod
    def _evaluateDiseaseResistance(diseaseResistanceChromosome, geneMaxVal):
        # "Odporność na chorobę zapisana jest na drugim chromosomie na pozycjach
        # [45-87] oraz [101-131]" Dodane 1 do 131 oraz 87 gdyż podane zakresy są domknięte.
        maxDiseaseResistance = geneMaxVal * (132 - 101 + 88 - 45)
        diseaseResistanceScore = sum(geneVal for geneVal in diseaseResistanceChromosome[45:88]) \
                                 + sum(geneVal for geneVal in diseaseResistanceChromosome[101:132])
        diseaseResistanceCoefficient = diseaseResistanceScore / maxDiseaseResistance
        return diseaseResistanceCoefficient

    @staticmethod
    def coefficientEvaluationFunction(individual):
        chromosomes = individual.chromosomes
        attractivenessChromosome = chromosomes[0]
        diseaseResistanceChromosome = chromosomes[1]
        attractivenessCoefficient = IndividualEvaluateFunctions._evaluateAttractiveness(
            attractivenessChromosome, individual.genesMaxVal)

        diseaseResistanceCoefficient = IndividualEvaluateFunctions._evaluateDiseaseResistance(
            diseaseResistanceChromosome, individual.genesMaxVal)

        return attractivenessCoefficient, diseaseResistanceCoefficient
