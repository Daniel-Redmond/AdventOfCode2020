import json
from expense_report import expense_report
from password_validator import password_validator

import logging
logging.basicConfig(level='ERROR')

def get_input(input_file_name):

    logging.info('Retrieving Task Input...')

    with open(f'Input/{input_file_name}') as f:
        task_input = f.read()

    logging.info('Task Input Retrieved')

    return task_input

def main():
    """

    DAY 2:

    https://adventofcode.com/2020/day/2

    """

    task_input = get_input("day_2.txt")
   
    validator = password_validator(logging)

    task_num = input('Task Number: ')
    
    if task_num == '1': 

        validator.set_validation_method('character_count')

    elif task_num == '2':

        validator.set_validation_method('character_position')

    else:

        print('Task does not exist...')
        validator.set_validation_method(input('Validation Method: '))

    validator.load_passwords(task_input)
    task_result = validator.validate()

    print(f"Valid Count: { len( task_result['valid'] ) }")
    print(f"Invalid Count: { len( task_result['invalid'] ) }")
    

if __name__ == "__main__":

    main()

    
    