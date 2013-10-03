import sys
from itertools import islice

def parse_fastq_file(input_file):
    '''Take an input file in fastq format and read 4 lines in at a time.
    Return the 4 lines that are separated by newlines to the Fastqread class
    This has been implemented yet in the Fastqread class 
    '''
    assert input_file.endswith('.fastq') or input_file.endswith('.fq')
    with open(input_file) as f:
        #while there are lines to read
        while True:
            #read in 4 lines at a time and make them into a list
            read=list(islice(f,4))
            #if there are really 4 lines concatenate them with newlines into a string
            if read:                     
                return '\n'.join(read)
                
            else:
                break

            
if __name__ == '__main__':
    file_name = sys.argv[1]
    parse_fastq_file(file_name)
