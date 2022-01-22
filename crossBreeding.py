class CrossBreeding:

    @staticmethod
    def getByName(name):
        _registered_crossbreeding_functions = {"onePoint": OnePointCrossing,
                                               "twoPoint": TwoPointCrossing}

        return _registered_crossbreeding_functions.get(name)


class OnePointCrossing(CrossBreeding):
    pass


class TwoPointCrossing(CrossBreeding):
    pass
