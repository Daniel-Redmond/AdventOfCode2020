class password_validator:

    def __init__(self,logging):

        self.password_objs = []
        self.validation_methods = {
            'character_count':{
                'method':self.validate_password_count,
                'policy_type':password_character_count_policy
            },
            'character_position':{
                'method':self.validate_password_position,
                'policy_type':password_character_position_policy
            }
        }
        

    def load_passwords(self,passwords_str):

        self.passwords_list = passwords_str.split('\n')

        for password in self.passwords_list:
            
            self.password_objs.append( self.parse_password_input(password) )

    def set_validation_method(self,method):

        if method in self.validation_methods.keys():

            self.validation_method = method
        
        else: 
            raise Exception('Invalid method provided')

    def parse_password_input(self,password_and_policy):

        """
        Password Input Structure:
        2-9 z: lhwqvczrrqqhqlfvkbcm


        --------
        2-9 z
        --------
        The password policy:

        2-9 -> The number of occurrences allowed for a character
        z -> the character

        --------
        lhwqvczrrqqhqlfvkbcm
        --------
        The password - must conform to the policy 

        """
        password_split = password_and_policy.split(': ')
        
        policy = self.validation_methods[self.validation_method]['policy_type'](password_split[0])
        password_str = password_split[1]

        return password(password_str,policy)

    def validate(self):
        """
        Validates each password loaded and returns a dict containing passwords sorted based on their validity
        """

        valid_passwords = []
        invalid_passwords = []
 
        for password_obj in self.password_objs:

            # Call the appropriate validation method based on the validation method set on the validator
            if self.validation_methods[self.validation_method]['method'](password_obj):

                valid_passwords.append(password_obj.password_str)

            else:

                invalid_passwords.append(password_obj.password_str)

        return {
            'valid':valid_passwords,
            'invalid':invalid_passwords
        }

    def validate_password_count(self,password_obj):
        """
        If the character specified by passwords policy occurs at least min_occurrences and at most max_occurrences in the 
        password then the password is valid
        """

        char_count = password_obj.password_str.count(password_obj.policy.character)

        if char_count >= password_obj.policy.min_occurrences and char_count <= password_obj.policy.max_occurrences:
            return True
        else:
            return False

    def validate_password_position(self,password_obj):
        """
        If character specified by passwords policy is in ONLY ONE of the positions set by the password policy
        Then the password is valid
        """

        position_1_match = password_obj.password_str[password_obj.policy.position_1 -1 ] == password_obj.policy.character
        position_2_match = password_obj.password_str[password_obj.policy.position_2 -1 ] == password_obj.policy.character

        if position_1_match != position_2_match: 
            return True
        else: 
            return False
    
class password:

    def __init__(self, password, policy):

        self.password_str = password
        self.policy = policy


class base_password_character_policy:

    def __init__(self, character):

        self.character = character

class password_character_count_policy(base_password_character_policy):

    def __init__(self,policy_str):
        """
        
        Example Policy Str: 2-9 z

        We will split this policy to determine min and max character occurrences

        """
        
        
        policy_split = policy_str.split(' ')
        self.process_min_max_occurrences(policy_split[0])

        super().__init__(policy_split[1])
        

    def process_min_max_occurrences(self,min_max_str):
        min_max_split = min_max_str.split('-')

        self.min_occurrences = int(min_max_split[0])
        self.max_occurrences = int(min_max_split[1])

class password_character_position_policy(base_password_character_policy):

    def __init__(self,policy_str):
        """
        
        Example Policy Str: 2-9 z

        We will split this policy to determine allowed character positions

        """
        
        
        policy_split = policy_str.split(' ')
        self.process_character_positions(policy_split[0])

        super().__init__(policy_split[1])
        

    def process_character_positions(self,pos_str):
        pos_split = pos_str.split('-')

        self.position_1 = int(pos_split[0])
        self.position_2 = int(pos_split[1])
