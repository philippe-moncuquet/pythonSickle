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
    
    def trim(self,start,end):
        '''Trim the sequence from start to end. Takes as input 2 integers
        
        #>>> test_read = DNAsequence(read)
        #>>> test_read.trim(start_no_cut, end_no_cut)
        'NTTTTTCCTTCCTTTAAAAC'
        #>>> test_read = DNAsequence(read)
        #>>> test_read.trim(start_small_cut, end_small_cut)
        'TCCTTCCTTTA'
        '''
        self.dna_str = self.dna_str[start:end+1]


if __name__ == '__main__':
    #Test window function with some dummy sequencing reads.
    #One read under threshold of 1, one over 1.
    short_read = 'TTTAAAAC'
    long_read = 'TTTAAAACTTTAAAACGTAC'
    float_read = 'TCCTTCCTTTAAAATCCTTCCTTTAAAATCCTTTAG'
    exact_length_read = 'CCTTTAAAAC'
    
    #Testing trimming function with different positions for starting and ending trim
    read = 'NTTTTTCCTTCCTTTAAAAC'
    start_no_cut, end_no_cut = 0, 20
    start_small_cut, end_small_cut = 5, 15
    
    doctest.testmod()
