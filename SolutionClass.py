from math import sqrt
from CityClass import City

class Solution:
    '''
    This Class will represent a solution to the problem
    consisting of the route and the fitness which is the
    reciprocal of the distance travelled
    @author Sebastian Castro
    '''
    def __init__(self,route):
        self.route = route
        self.fitness = self.get_Fitness()

    def distance(self,a,b):
        '''
        Distance between two cities
        Returns:
            the distance between cities
        '''
        sum = (b.y - a.y)**2 + (b.x-a.x)**2
        return sqrt(sum)

    def distance_travelled(self):
        '''
        Find the distance between two cities moving
        along the route array two at a time and the last one
        returns:
            The distance travelled along the route
        '''
        distance = 0
        for i in range(len(self.route)-1):
            distance += self.distance(self.route[i],self.route[i+1]) #the cities
        distance += self.distance(self.route[-1],self.route[0]) #last and first city
        return distance

    def get_Fitness(self):
        '''
        Returns the fitness of the individual routes
        as the reciprocal of the distance travelled
        from the previous function
        returns:
            a double
        '''
        return 1/self.distance_travelled()

    def __str__(self):
        return f'Solution fitness: {self.fitness}, route: {self.route}'
    def ___rep__(self):
        return f'Solution fitness: {self.fitness}, route: {self.route}'
