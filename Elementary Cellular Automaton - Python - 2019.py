class CA:
    """Elementary Cellular Automaton - by Paul Panaitescu
    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""
    
    def __init__(self, rule, init_state='0'*20+'1'+'0'*20):
        """Initialize the CA with the given rule and initial state."""
        self.binary = f'{rule:08b}'        # transform the rule number to a binary code (Example: rule 90 is 01011010 in binary code)
        self.dict= {                       # make a dictionary to store the 8 possible pairs of 3 neighbourhood elements (with values 1 and 0)
          "111": (self.binary[0]),         # assign to each key, a value equivalent to a character from the binary code (from index 0 to index 7)
          "110": (self.binary[1]),
          "101": (self.binary[2]),
          "100": (self.binary[3]),
          "011": (self.binary[4]),
          "010": (self.binary[5]),
          "001": (self.binary[6]),
          "000": (self.binary[7])
        }
        self.init_state = init_state
        self.current_state = ""
#         print(self.binary)
#         print(self.dict)
#         print(self.init_state)
    
    def state(self):
        """Returns the current state."""
        return self.current_state
    
    def next(self):
        """Progress one step and then return the current state."""
        self.init_state = '0' + self.init_state + '0'  # add '0' to simulate the neighbourhood elements of the first and last element of the string
        self.current_state = ''                        # clean self.current_state, to start with new values
        group=''                                       # group will have 3 characters to compare the 3 current neighbourhood elements with a series from dictionary 
        for i in range(1, len(self.init_state)-1):     # iterate through self.init_state, without first and last element
            for j in range(i-1, i+2):                  # get groups of 3 elements (left, center, right)
                group+=self.init_state[j]              # add elemnts to group
#             print(group)
            self.current_state+=self.dict[group]       # add value (1 or 0) in self.current_state, after corresponding dictionary value of the 3 group characters 
            group = ''                                 # clean group string
        self.init_state = self.state()                 # prepare self.init_state for next itteration
        return self.current_state
        
    def run(self, num=18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        print(self.init_state.replace("0", " ").replace("1", "*"))        # print the first line
        for i in range(1,num):
            print(self.next().replace("0", " ").replace("1", "*"))        # continue printing the next 17 lines

# ca = CA(90).run()
ca = CA(129).run()