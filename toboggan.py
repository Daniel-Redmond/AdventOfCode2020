class toboggan:

    def __init__(self,logging):
        self.logging = logging
        self.pos_x = 0
        self.pos_y = 0
        self.sliding = False

    def place_on_hill(self,hill,start_x=0,start_y=0):
        self.logging.info(f'Placing toboggan on hill at Coords x = {start_x}, y = {start_y}')
        self.hill = hill

        self.pos_x = start_x
        self.pos_y = start_y

    def move_right(self,distance):
        self.logging.debug('Moving Right!')
        self.pos_x = (self.pos_x + distance) % self.hill.boundary_x
        self.logging.debug(f'New Coords: x = {self.pos_x}, y = {self.pos_y}    Value: {self.hill.hill_definition[self.pos_y][self.pos_x]}')

    def move_left(self,distance):
        self.logging.debug('Moving Left!')
        self.pos_x = (self.pos_x - distance) % self.hill.boundary_x 
        self.logging.debug(f'New Coords: x = {self.pos_x}, y = {self.pos_y}    Value: {self.hill.hill_definition[self.pos_y][self.pos_x]}')

    def move_up(self,distance):
        self.logging.debug('Moving Up!')
        self.pos_y = self.pos_y - distance
        self.logging.debug(f'New Coords: x = {self.pos_x}, y = {self.pos_y}    Value: {self.hill.hill_definition[self.pos_y][self.pos_x]}')

    def move_down(self,distance):
        self.logging.debug('Moving Down!')

        if self.pos_y == self.hill.boundary_y:

            print('We have reached the bottom of the hill!')
            self.sliding = False

        else:

            self.pos_y = self.pos_y + distance
            self.logging.debug(f'New Coords: x = {self.pos_x}, y = {self.pos_y}    Value: {self.hill.hill_definition[self.pos_y-1][self.pos_x]}')


    def slide(self,distance_right,distance_down):
        trees_hit = 0
        self.sliding = True
        route = []

        while self.sliding:
            if self.hill.hill_definition[self.pos_y][self.pos_x] == '#':
                self.logging.debug("Ouch - We've hit a tree!")
                trees_hit = trees_hit + 1

            # Store the route taken for debugging purposes
            row = list(self.hill.hill_definition[self.pos_y])
            row[self.pos_x] = '[' + row[self.pos_x] + ']'
            route.append(''.join(row))

            self.move_right(distance_right)
            self.move_down(distance_down)

        self.logging.info(f'Trees Hit: {trees_hit}')

        for i in route:
            
            i.replace('.',' . ')
            
            print(i)

        return trees_hit

        
