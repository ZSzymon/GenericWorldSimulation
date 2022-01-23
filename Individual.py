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
        self.genesMinVal = config["geneMinVal"]
        self.genesMaxVal = config["geneMaxVal"]

        self.chromosome = chromosome if chromosome else []

        if initChromosome:
            self.initializeChromosome(config.genesInChromosome, config.geneMinVal, config.geneMaxVal)

        if performEvaluation:
            self.evaluationScore = self.performEvaluation()

        self.relativeEvaluationScore = None

    @staticmethod
    def checkChoosenConditions(initChromosome, performEvaluation, chromosome):
        """A method for checking that the given conditions are not mutually exclusive

        :param initChromosome: Boolean representing is Chromosome is initialized on init.
        :param performEvaluation: Boolean representing is evaluation is performed in init.
        :param chromosome: List representing the chromosome
        :return: None or raising Exception.
        """

        if chromosome is None and not initChromosome and performEvaluation:
            raise WrongInitializeConditions("You have to provide chromosome or accept to init chromosome")

    def initializeChromosome(self, genesInChromosome: int, geneMinVal: int, geneMaxVal: int):
        """A method for initializing chromosome.

        :param genesInChromosome: Length of genes in one chromosome
        :param geneMinVal:
        :param geneMaxVal:
        :return: None
        """

        for i in range(genesInChromosome):
            randValue = random.randint(geneMinVal, geneMaxVal)
            self.chromosome.append(randValue)

    def performEvaluation(self, evaluationFunction=None):
        """Method for performing evaluation

        :param evaluationFunction: Function responsible for evaluation of individual
        """
        if evaluationFunction is None:
            evaluationFunction = Settings.defaultEvaluationFunction

        self.evaluationScore = evaluationFunction(self)


    @staticmethod
    def mutationFunction(chromosome, geneMinVal, geneMaxVal) -> List:
        """ Method performing mutation on chromosome

        :param chromosome:
        :param geneMinVal:
        :param geneMaxVal:
        :return: Chromosome with mutation
        """
        randIndex = random.randint(0, len(chromosome) - 1)
        randValue = random.randint(geneMinVal, geneMaxVal)
        chromosome[randIndex] = randValue
        return chromosome

    def mutate(self, mutationFunction):
        """API function for calling mutation function.

        :param mutationFunction:
        :return:
        """
        newChromosome = mutationFunction(self.chromosome, self.genesMinVal, self.genesMaxVal)
        self.chromosome = newChromosome
