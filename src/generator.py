"""
File: generator.py
Author: Sathish Kumar John Peter
Description: This utility file helps in pattern generator and it's helper functions
"""


class MarchingDoubler:
    """Marching Doubler class generates patterns
        NOTE: Created as class to support higher bandwidth of userbase 
        to run pattern generator in parallel
    """
    def __init__(self) -> None:
        # length of the Run
        self._run_length: int = None
        # total no of term(each no is called term) in the series
        self._terms_length: int = None
    
    @property
    def run_length(self):
        # Getter method for run_length property
        return self._run_length

    @run_length.setter
    def run_length(self, run_length: int):
        if type(run_length) != int:
            raise ValueError('Run Length Should be an Integer')
        self._run_length = run_length
    
    @property
    def terms_length(self):
        # Getter method for terms_length
        return self._terms_length

    @terms_length.setter
    def terms_length(self, terms_length: int):
        if type(terms_length) != int:
            raise ValueError('Terms Length Should be an Integer')
        self._terms_length = terms_length
    
    def generate_pattern(self):
        """
        Generates the below patter if self.run_length = 4 & self.terms_length = 4
        1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3
        
        O(n * (terms/n)) => O(terms) => O(n) leading to linear time complexity
        Space complexity => O(terms) => O(1)
        
        Yields:
            ( < <None> | <int> >, <int> ) : Previous yield term and current value of the term
        """
        
        # index tracker for run length of one set
        idx = 0
        
        terms_length = self._terms_length
        run_length = self._run_length
        
        # Runs to produce series of number == terms_length
        while terms_length > 0:
            # term starts with 1 every one set
            term = 1
            if idx >= run_length-1:
                # start index from 0 for every one set until term runs out
                idx = 0
            # Keeps track of the previous yielded value, always starts with 1
            previous = 1
            
            # produces run length
            for num in range(run_length):
                # Modifies previous term which is already yielded and re-sends
                prev_modified = None
                
                if num == 0:
                    pass
                elif idx == num:
                    term += 1
                    # Make sure always previous term is adjacent
                    # e.g(previous) 1,2,2,3 => (Current) 1,1,3,3 => (Modified) 1,2,3,3
                    if (num+1) - previous != 1:
                        prev_modified = previous + 1
                else:
                    term = num
                
                previous = term
                
                yield prev_modified, term
            
            # Reduce term length each time it runs for 
            terms_length -= run_length
            idx += 1

