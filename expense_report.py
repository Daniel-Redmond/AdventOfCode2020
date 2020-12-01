import json
MAX_ITERATIONS_ALLOWED = 10000

class expense_report:

    def __init__(self,logging,report_values_str):
        self.logging = logging
        self.load_report(report_values_str)
        

    def load_report(self,report_values_str):
        
        self.report_values = report_values_str.split('\n')
        self.logging.info(f'Report Record Count: {len(self.report_values)}')

    def repair_report(self, total_aggregate, numbers_aggregated_count):
        """

        Repairs expense report by finding occurrences of {numbers_aggregated_count} numbers that, when added, 
        equal {total_aggregate}, and multiplying them together 

        Input: 
        - total_aggregate: Int

        The total value that the numbers should add up to

        - numbers_aggregated_count: Int

        The count of numbers that, when aggregated, equal the total_aggregate value 

        Output: 

        A multiplication of all numbers that, when aggregated, equal the total_aggregate value - Int

        """


        self.total_iterations = 0
        result = 1
        
        numbers_to_multiply = self.find_additions(total_aggregate,numbers_aggregated_count)

        for i in numbers_to_multiply:
            result = result * i
        
        return result

    def find_additions(self, total_aggregate, numbers_aggregated_count):
        """

        Finds occurrences of numbers that, when aggregated, equal the total_aggregate value and returns them

        Input: 
        - total_aggregate: Int

        The total value that the numbers should add up to

        - numbers_aggregated_count: Int

        The count of numbers that, when aggregated, equal the total_aggregate value 

        Output: 

        Occurrences of all numbers that, when aggregated, equal the total_aggregate value - List

        """

        self.logging.info(f'Looking for {numbers_aggregated_count} numbers that add up to {total_aggregate}')

        numbers = []
        report_dict = { int(self.report_values[i]) : total_aggregate - int( self.report_values[i] ) for i in range(0,len( self.report_values ) ) }

        if numbers_aggregated_count == 2:
            

            for key in report_dict:

                if self.total_iterations == MAX_ITERATIONS_ALLOWED: 
                    raise Exception(f'MAX ITERATIONS LIMIT EXCEEDED - {MAX_ITERATIONS_ALLOWED}')

                self.total_iterations = self.total_iterations + 1

                self.logging.debug(f'Working with: { json.dumps({key:report_dict[key]}) }')

                if report_dict.get(report_dict[key]):

                    self.logging.debug(f'We have found a match!')

                    numbers.append(key)
                    numbers.append(report_dict[key])

                    return numbers

        else:

            for key in report_dict:

                if self.total_iterations == MAX_ITERATIONS_ALLOWED: 
                    raise Exception(f'MAX ITERATIONS LIMIT EXCEEDED - {MAX_ITERATIONS_ALLOWED}')

                self.total_iterations = self.total_iterations + 1

                self.logging.debug(f'Working with: { json.dumps({key:report_dict[key]}) }')

                self.logging.debug(f'Recursively searching for {numbers_aggregated_count-1} that equal {report_dict[key]}')
                found = self.find_additions(report_dict[key],numbers_aggregated_count-1)

                if found != None:
                    self.logging.debug(f'Found: {found}')
                    self.logging.debug(f'key: {key}')
                    found.append(key)
                    return found


        return None