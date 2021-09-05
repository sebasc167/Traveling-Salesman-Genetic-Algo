# Traveling-Salesman-Genetic-Algo
In the repo I will solve the travelling salesman problem where we will work with 25 different locations on a grid and find the shortest route while visiting all cities exactly once. The goal will be to solve this problem using a genetic algorithm where we will create a population of different solutions containing the distance of the overall route and the actual route travelled. We will then make new solutions by picking out pairs of parents using the roulette selection method and cross breeding parents to get half the population with new solutions and the other half of the new population will contain the best solutions of the current population (elitism).

After breeding and sorting according to the fitness or distance travelled we will repeat the process a certain number of generations and well as having a mutation rate to randomly change two locations in a random solution route from the population. Found below is the py files with the three classes and a link to the Google Colab developed
