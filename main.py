from statistics import mean, StatisticsError

from world import WorldB, WorldA


def mode_a():
    """Konfiguracja całego trybu odbywa się poprzez plik  config/configB.json"""
    world = WorldA()


def mode_b():
    """Konfiguracja całego trybu odbywa się poprzez plik  config/configB.json"""
    worldB = WorldB()
    data = []
    for i in range(10):
        row = worldB.run()
        data.append(row)
    print("End of simulation")
    print("Average population cost: " + str(mean([i[0] for i in data if i[2] == 1])))

    print("Average last Generation if population gain herd immunity: " + str(mean([i[1] for i in data if i[2] == 1])))
    try:
        print("Average last Generation if population extinguish: " + str(mean([i[1] for i in data if i[2] == 0])))
    except StatisticsError as e:
        pass


if __name__ == '__main__':
    mode_a()
    mode_b()
