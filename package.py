'''Especificações do projeto
    Tamanho da população: 9 indivíduos;
    Fórmula do grau de aptidão: Soma do valor dos conponentes do indivíduo;
    Método de seleção: Roleta;
    Método de cruzamento: cruzamento com um ponto de corte
    Taxa de mutação: 5%
    Ponto de parada do algortimo: Escolhido pelo usuário;
'''

import random
import pandas as pd

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
    for i in range(int(afnd)):
        roleta.append(name)

    return roleta

def sortRoleta(population):
    roleta = []
    for individual in population:
        afnd = fitness(individual[0])
        ind = population.index(individual)
        indv = list(population[ind])
        indv[1] = afnd[0]
        population[ind] = tuple(indv)
        roleta += roletaPopulation(afnd[0], ind)

    return (roleta, population)

def mutationII(newIndOne, newIndTwo):
    individuals = [newIndOne, newIndTwo]

    for i in individuals:
        for g in i:
            if random.uniform(0, 1) < 0.05:
                ind = i.index(g)
                i[ind]['value'] = int(i[ind]['value']) * round(random.uniform(-1.5, 1.5), 1)
                
    return individuals

def realoc(population):
    fitness = []
    for individual in population:
        fitness.append(individual)

    fitness.sort(key=lambda tup: tup[1])
    return (population.index(fitness[0]), population.index(fitness[1]))

if __name__ == '__main__':
    geraItens()
    population = createPopulation()
    
    generations = input("Insert the number of generations: ")

    df = pd.DataFrame.from_records(population)
    df.columns = ['Individual', 'Value']
    print("Initial population")
    print(df)

    for g in range(int(generations)):
        roleta, population = sortRoleta(population)
        choiceOne = random.choice(roleta)
        choiceTwo = random.choice(roleta)
        
        newIndividualOne = population[choiceOne][0][0:4] + population[choiceTwo][0][4:8]
        newIndividualTwo = population[choiceTwo][0][0:4] + population[choiceOne][0][4:8]

        #mutation(population)
        newIndividuals = mutationII(newIndividualOne, newIndividualTwo)
        
        ind = realoc(population)
        
        population[ind[0]] = (newIndividuals[0], fitness(newIndividuals[0])[0])
        population[ind[1]] = (newIndividuals[1], fitness(newIndividuals[1])[0])
        
        df = pd.DataFrame.from_records(population)
        df.columns = ['Individual', 'Value']
        print("Generation %d:" %(g))
        print(df)



    
    


