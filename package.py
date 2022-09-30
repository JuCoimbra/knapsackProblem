import random

itens = []

def geraItens():

    for i in range(16):

        gene = {
            "id": i,
            "value": random.randint(5, 30),
            "weigth": random.randint(3, 11)
        }

        itens.append(gene)

def createIndividual():
    individual = []
    for i in random.sample(range(0, 16), 8):
        individual.append(itens[i])

    return individual


def createPopulation():
    population = []

    for i in range(8):
        population.append((createIndividual(), 0))

    return population

def fitness(individual):
    totalWeigth = 0
    totalValue = 0
    for item in individual:
        if totalWeigth < 15:
            totalWeigth += item['weigth']
            totalValue += item['value']
        else:
            totalValue += item['value'] - (totalWeigth + item['weigth'] - 15)

    return (totalValue, totalWeigth) 

def roletaPopulation(afnd, name):
    roleta = []
    for i in range(afnd):
        roleta.append(name)

    return roleta

def sortRoleta(population):
    roleta = []
    for individual in population:
        print(individual[0])
        afnd = fitness(individual[0])
        ind = population.index(individual)
        indv = list(population[ind])
        indv[1] = afnd[0]
        population[ind] = tuple(indv)
        roleta += roletaPopulation(afnd[0], ind)

    return (roleta, population)

if __name__ == '__main__':
    geraItens()
    print(itens)
    population = createPopulation()
    
    roleta, population = sortRoleta(population)
    choiceOne = random.choice(roleta)
    choiceTwo = random.choice(roleta)
    
    print(population[choiceOne][0][0:4])
    print(population[choiceTwo][0][4:8])

    newIndividual = population[choiceOne][0][0:4] + population[choiceTwo][0][4:8]
    print(newIndividual)

