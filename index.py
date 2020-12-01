import json
from expense_report import expense_report

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

    DAY 1:

    https://adventofcode.com/2020/day/1

    """

    task_input = get_input("day_1.txt")
    report = expense_report(logging,task_input)

    task_num = input('Task Number: ')
    
    if task_num == '1': 

        total_aggregate = 2020
        numbers_aggregated_count = 2

    elif task_num == '2':

        total_aggregate = 2020
        numbers_aggregated_count = 3

    else:

        print('Task does not exist...')
        total_aggregate = int(input('Total Aggregate: '))
        numbers_aggregated_count = int(input('Numbers Aggregated Count: '))

    task_result = report.repair_report(total_aggregate,numbers_aggregated_count)

    print(f'Result: {task_result}')
    print(f'Iterations: {report.total_iterations}')
    

if __name__ == "__main__":

    main()

    
    