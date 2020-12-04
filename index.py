import json
from hill import hill
from toboggan import toboggan

import logging
logging.basicConfig(level='INFO')

def get_input(input_file_name):

    logging.info('Retrieving Task Input...')

    with open(f'Input/{input_file_name}') as f:
        task_input = f.read()

    logging.info('Task Input Retrieved')

    return task_input

def main():
    """

    DAY 3:

    https://adventofcode.com/2020/day/3

    """

    task_input = get_input("day_3.txt")
   
    hill_to_traverse = hill(logging,task_input)
    shiny_new_toboggan = toboggan(logging)
    shiny_new_toboggan.place_on_hill(hill_to_traverse)


    task_num = input('Task Number: ')
    
    if task_num == '1': 

        shiny_new_toboggan.slide(
            distance_right = 3,
            distance_down = 1
        )

    elif task_num == '2':

        routes = [
            {
                'distance_right':1,
                'distance_down':1
            },
            {
                'distance_right':3,
                'distance_down':1
            },
            {
                'distance_right':5,
                'distance_down':1
            },
            {
                'distance_right':7,
                'distance_down':1
            },
            {
                'distance_right':1,
                'distance_down':2
            }
        ]

        multiplied_value = 1

        for route in routes: 
            shiny_new_toboggan.place_on_hill(hill_to_traverse)

            trees_hit = shiny_new_toboggan.slide(
                distance_right = route['distance_right'],
                distance_down = route['distance_down']
            )

            multiplied_value = multiplied_value * trees_hit

            route['trees_hit'] = trees_hit

        print(f'Routes: {routes}')
        print(f'Result: {multiplied_value}')

    else:

        print('Task does not exist...')
        distance_right_input = int(input('Distance Right: '))
        distance_down_input = int(input('Distance Down: '))

        trees_hit = shiny_new_toboggan.slide(
            distance_right = distance_right_input,
            distance_down = distance_down_input
        )

        print(f'Trees Hit: {trees_hit}')


if __name__ == "__main__":

    main()

    
    