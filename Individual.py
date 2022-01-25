from evaluationFunction import IndividualEvaluateFunctions
from exceptions import WrongInitializeConditions
from settings import Settings
import random
from typing import List, Optional, Tuple


class Individual:

    def __init__(self, IndividualClass, initChromosome=True, performEvaluation=True,
                 chromosome: Optional[list] = None):
        self.IndividualClass = IndividualClass
        Individual.checkChoosenConditions(initChromosome, performEvaluation, chromosome)
        self.config = IndividualClass.config
        self.genesInChromosome = IndividualClass.config["genesInChromosome"]
        self.mutationChance = IndividualClass.config["mutationChance"]
        self.genesMinVal = IndividualClass.config["geneMinVal"]
        self.genesMaxVal = IndividualClass.config["geneMaxVal"]

    @staticmethod
    def checkChoosenConditions(initChromosome, performEvaluation, chromosome):
        """A method for checking that the given conditions are not mutually exclusive

        :param initChromosome: Boolean representing is Chromosome is initialized on init.
        :param performEvaluation: Boolean representing is evaluation is performed in init.
        :param chromosome: List representing the chromosomes
        :return: None or raising Exception.
        """

        if chromosome is None and not initChromosome and performEvaluation:
            raise WrongInitializeConditions("You have to provide chromosomes or accept to init chromosomes")

    def performEvaluation(self, evaluationFunction=None):
        """Method for performing evaluation

        :param evaluationFunction: Function responsible for evaluation of individual
        """
        if evaluationFunction is None:
            evaluationFunction = IndividualEvaluateFunctions.getByName(self.config.evaluationFunction)
        self.evaluationScore = evaluationFunction(self)


    def mutate(self, mutationFunction):
        """API function for calling mutation function.

        :param mutationFunction:
        :return:
        """
        newChromosome = self.IndividualClass.mutationFunction(self.chromosomes, self.genesMinVal, self.genesMaxVal)
        self.chromosomes = newChromosome

    @staticmethod
    def willMutate(chance):
        return random.randint(0, 100) in range(0, chance)

    @staticmethod
    def mutationFunction(chromosomes, geneMinVal, geneMaxVal) -> List:
        """ Method performing mutation on chromosomes

        :param chromosomes:
        :param geneMinVal:
        :param geneMaxVal:
        :return: Chromosome with mutation
        """

        if isinstance(chromosomes[0], int):
            randIndex = random.randint(0, len(chromosomes) - 1)
            randValue = random.randint(geneMinVal, geneMaxVal)
            chromosomes[randIndex] = randValue
            return chromosomes

        for chromosome in chromosomes:
            randIndex = random.randint(0, len(chromosome) - 1)
            randValue = random.randint(geneMinVal, geneMaxVal)
            chromosome[randIndex] = randValue
        return chromosomes


class IndividualA(Individual):
    config = Settings.configA
    evaluationScore: int
    relativeEvaluationScore: int
    chromosomes: List[int]

    def __init__(self, initChromosomes=True, performEvaluation=True, chromosomes: Optional[list] = None):

        super().__init__(type(self), initChromosomes, performEvaluation, chromosomes)
        self.chromosomes = chromosomes if chromosomes else []
        if initChromosomes:
            self.initializeChromosome(self.config.genesInChromosome, self.config.geneMinVal, self.config.geneMaxVal)

        if performEvaluation:
            self.performEvaluation()

        self.relativeEvaluationScore = None

    def initializeChromosome(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        """A method for initializing chromosomes.

        :param genesInChromosome: Length of genes in one chromosomes
        :param geneMinVal:
        :param geneMaxVal:
        :return: None
        """

        for i in range(genesInChromosome):
            randValue = random.randint(geneMinVal, geneMaxVal)
            self.chromosomes.append(randValue)

class IndividualB(Individual):
    config = Settings.configB
    relativeEvaluationScore: int
    chromosomes: List[List[int]]
    genesInChromosome: int
    mutationChance: float
    genesMinVal: int
    genesMaxVal: int
    chromosomesInIndividual: int
    attractivityCoefficient: float
    diseaseResistanceCoefficient: float

    def __init__(self, config=Settings.configB, initChromosomes=True, performEvaluation=True,
                 chromosomes: Optional[Tuple[list, list]] = None):
        super().__init__(type(self), initChromosomes, performEvaluation)
        self.chromosomesInIndividual = config["chromosomesInIndividual"]
        self.chromosomes = chromosomes if chromosomes else list([] for _ in range(config["chromosomesInIndividual"]))
        if initChromosomes:
            self.initializeChromosome(config.chromosomesInIndividual, config.genesInChromosome, config.geneMinVal,
                                      config.geneMaxVal)

        self.diseaseResistanceCoefficient = 0
        self.attractivityCoefficient = 0
        if performEvaluation:
            self.performEvaluation()

    @staticmethod
    def checkChoosenConditions(initChromosome, performEvaluation, chromosome):
        """A method for checking that the given conditions are not mutually exclusive

        :param initChromosome: Boolean representing is Chromosome is initialized on init.
        :param performEvaluation: Boolean representing is evaluation is performed in init.
        :param chromosome: List representing the chromosomes
        :return: None or raising Exception.
        """

        if chromosome is None and not initChromosome and performEvaluation:
            raise WrongInitializeConditions("You have to provide chromosomes or accept to init chromosomes")

    def initializeChromosome(self, chromosomesInIndividual, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        """A method for initializing chromosomes.

        :param chromosomesInIndividual: number of chromosomes in each individual.
        :param genesInChromosome: Length of genes in one chromosomes
        :param geneMinVal:
        :param geneMaxVal:
        :return: None
        """
        for i in range(chromosomesInIndividual):
            for j in range(genesInChromosome):
                self.chromosomes[i].append(random.randint(geneMinVal, geneMaxVal))

    def performEvaluation(self, evaluationFunction=None):
        """Method for performing evaluation

        :param evaluationFunction: Function responsible for evaluation of individual
        """
        if evaluationFunction is None:
            evaluationFunction = IndividualEvaluateFunctions.getByName(self.config.evaluationFunction)

        self.attractivityCoefficient, self.diseaseResistanceCoefficient = evaluationFunction(self)
        self.evaluationScore = self.attractivityCoefficient

    # @staticmethod
    # def mutationFunction(chromosomes, geneMinVal, geneMaxVal) -> List:
    #     """ Method performing mutation on chromosomes
    #
    #     :param chromosomes:
    #     :param geneMinVal:
    #     :param geneMaxVal:
    #     :return: Chromosome with mutation
    #     """
    #     for chromosome in chromosomes:
    #         randIndex = random.randint(0, len(chromosome) - 1)
    #         randValue = random.randint(geneMinVal, geneMaxVal)
    #         chromosome[randIndex] = randValue
    #     return chromosomes
