import doctest

class DNAsequence:
    def __init__(self, dna_str):
        '''create a sequence attribute (string)'''
        self.dna_str = dna_str
    
    def window_size(self):
        '''Calculate the window size for averaging quality control.
           Window size will depend on the full size of the read.
           window across them whose length is 0.1 times the length of the read.
           If this length is less than 1, then the window is set to be 
           equal to the length of the read
            
        >>> short_case = DNAsequence(short_read)
        >>> short_case.window_size()
        1
        >>> long_case = DNAsequence(long_read)
        >>> long_case.window_size()
        2
        >>> exact_case = DNAsequence(exact_length_read)
        >>> exact_case.window_size()
        1
        >>> float_read = DNAsequence(float_read)
        >>> float_read.window_size()
        3
        '''
    #get the read length as an integer. Rounds down using the int function
        read_length = len(self.dna_str)
        window_length = int(0.1 * read_length)
        if window_length < 1:
            window_length = 1
        
        return window_length


if __name__ == '__main__':
    #Test window function with some dummy sequencing reads.
    #One read under threshold of 1, one over 1.
    short_read = 'TTTAAAAC'
    long_read = 'TTTAAAACTTTAAAACGTAC'
    float_read = 'TCCTTCCTTTAAAATCCTTCCTTTAAAATCCTTTAG'
    exact_length_read = 'CCTTTAAAAC'
    
    doctest.testmod()
