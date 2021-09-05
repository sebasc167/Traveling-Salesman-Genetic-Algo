import random
from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
from CityClass import City
from SolutionClass import Solution

seed(10)
cityList = []
for i in range(25):
    cityList.append(City(randint(0,200),randint(0,200)))

class Mappy:
    def __init__(self,population_num:int):
        '''
        Population number is the number of total solutions
        to play with and NOT the number of cities
        '''
        self.bestSolution = None
        self.solutions = [Solution(sample(cityList,25)) for _ in range(population_num)]
        self.pop_num = population_num
    def sortSolutions(self):
        '''
        This function will not return anything but will simply
        sort the solution list in descending order according to the
        solution's fitness attribute
        return:
            None
        '''
        self.solutions.sort(key = lambda k: k.fitness, reverse=True)

    def updateBest(self):
        self.bestSolution = max(self.solutions,key=lambda k: k.fitness)
        print(f'The best solution has route {self.bestSolution.route}\nfitness {1/self.bestSolution.fitness}')
        return int(1/self.bestSolution.fitness)

    def nextGeneration(self):
        '''
        This function will first add the top half solutions to the nextGeneration
        and then add the next top performing solutions to the pool and replace the
        array with a new generation
        return:
            None, updates the solutions pool
        '''
        nextGen = [] #next generation of cities
        first_half_gen = self.elitism()
        nextGen.extend(first_half_gen) #adding the first half of the generation
        self.solutions = nextGen #now update the solutions with the nextGen

        second_half_gen = []
        for _ in range(self.pop_num//2):
            parents = self.rouletteWheelSelection()
            parent1,parent2 = parents[0], parents[1] #the parent solutions
            second_half_gen.append(self.breed(parent1,parent2))

        nextGen.extend(second_half_gen) #adding the next half of the generation

    def elitism(self):
        '''
        This function will simply add on the top half performing routes
        to the population
        return:
            A list of cities, half the size
        '''
        halfGen=[self.solutions[i] for i in range(self.pop_num//2)]
        return halfGen

    def totalFitness(self):
        '''
        This function simply adds the fitness of the individuals
        '''
        fitness = [solution.fitness for solution in self.solutions]
        return sum(fitness)

    def rouletteWheelSelection(self):
        '''
        return two parents for breeding as a list
        '''
        parents = [] #two parents
        total = 0
        roulette = []
        for i in range(len(self.solutions)):
            total_fit = self.totalFitness()
            portion = self.solutions[i].fitness / total_fit
            roulette.append((i, total, total + portion))
            total += portion
        spin = random()
        #print(f'this is the roulette values: {roulette}')
        picked = [i for i in roulette if i[1] <= spin < i[2]]
        spin2 = random()
        picked2 = [i for i in roulette if i[1] <= spin2 < i[2]]
        while picked[0][0] == picked2[0][0]:
            #print("PICKED THE SAME PARENT")
            spin2 = random()
            picked2 = [i for i in roulette if i[1] <= spin2 < i[2]]
        parents.append(self.solutions[picked[0][0]])
        parents.append(self.solutions[picked2[0][0]])
        return parents

    def breed(self,sol1:Solution,sol2:Solution)->Solution:
        '''
        parameters:
            sol1: A solution parent picked by rank selection
        return
            A solution child from solutions 1 and 2
        '''
        assert (len(sol1.route) == len(sol2.route))
        child = []

        gene1 = randint(0, len(sol1.route))
        gene2 = randint(0, len(sol2.route))
        while gene1 == gene2:
            gene2 = randint(0, len(sol2.route))
        generange = (gene1, gene2) if gene1 < gene2 else (gene2, gene1)
        slicey = sol1.route[generange[0]:generange[1] + 1]
        child1 = [i for i in sol2.route if i not in slicey]

        child.extend([child1[i] for i in range(0, generange[0])])
        child.extend(slicey)
        child.extend([child1[i] for i in range(generange[0], len(child1))])
        childSolution = Solution(route=child) #type is Solution
        return childSolution

    def execute(self,generations,mutation_rate):
        y_axis = []
        x_axis = []
        self.sortSolutions()
        print("------ Generation 0---------------")
        for sol in self.solutions:
            print(sol)
        print("----------------------------------")
        dist = self.updateBest()
        x_axis.append(0)
        y_axis.append(dist)
        for i in range(generations):
            self.nextGeneration()
            self.mutation(mutation_rate)
            self.sortSolutions()
            print(f'--------Generation {i+1} ----------------')
            #for sol in self.solutions:
                #print(sol)
            dist = self.updateBest()
            x_axis.append(i+1)
            y_axis.append(dist)
            print("-----------------------------------------")
        plt.xlabel("Generations")
        plt.ylabel("Route Distance")
        plt.plot(np.array(x_axis,dtype=np.int32),np.array(y_axis,dtype=np.int32))
        plt.suptitle("Travelling Distances vs Generations")
        plt.show()


    def mutate(self,index,gene1,gene2):
        '''
        This function will swap city locations to visit randomly
        on a random route
        return:
            None
        '''
        self.solutions[index].route[gene1], self.solutions[index].route[gene2] = self.solutions[index].route[gene2], self.solutions[index].route[gene1]
        print(f'Mutation has occurred at gene{gene1} and gene{gene2} at solution number {index+1}')

    def mutation(self,mutation_rate):
        '''
        This function is the mutation driver, so it will
        pick a random route solution and two random
        '''
        wheel = []
        total = 0
        wheel.append((total,total + mutation_rate))
        total+=mutation_rate
        wheel.append((total,1))
        spin = random()
        if wheel[0][0] <= spin <= wheel[0][1]:
            gene1 = randint(0,24)
            gene2 = randint(0,24)
            while(gene1 == gene2):
                gene2 = randint(0, 24)
            self.mutate(randint(0,self.pop_num-1),gene1,gene2)
        else:
            pass

TSP1 = Mappy(20)
TSP1.execute(generations=500,mutation_rate=0.31)
