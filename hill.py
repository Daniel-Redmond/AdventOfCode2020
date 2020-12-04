class hill:

    def __init__(self,logging,hill_definition_str):
        self.logging = logging
        self.process_hill_definition(hill_definition_str)

    def process_hill_definition(self,hill_definition_str):
        self.logging.debug('Loading Hill Definition')
        self.hill_definition = hill_definition_str.split('\n')  
        self.boundary_x = len(self.hill_definition[0])  
        self.boundary_y = len(self.hill_definition) - 1
        self.logging.debug('Hill Definition Loaded')
        self.logging.debug(f'Boundary X: {self.boundary_x}')
        self.logging.debug(f'Boundary Y: {self.boundary_y}')