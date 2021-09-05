class City:
    '''
    This class will hold a city in terms of its
    x and y coordinates
    @author Sebastian Castro
    '''

    def __init__(self, x, y):
        # Holds the x and y components
        self.x = x
        self.y = y
        self.point = (x, y)
    def __str__(self):
        return f'City: {self.point}'
    def __repr__(self):
        return f'City: {self.point}'