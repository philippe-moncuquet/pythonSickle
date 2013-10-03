class fastqread:
    def __init__(self,fastq_str):
    ''' Take a string corresponding to a read from a fastq file, return 3 attributes: 
        name of sequence, sequence, quality score
    ''' 
    
    def split_string(self,fastq_str):
    ''' convert the fastq string for a read into a dictionary of 3 string'''
    
    def slide_window(self,qual_str,window_size,quality_threshold):
        ''' slide a window and calculate average. Output the 5 end trim index
            and 3'end trim index
        ''' 
    
    def trim_seq(self,start_index,end_index):
        '''Trim the sequence and quality score given an index for start and end
        '''
    
    def convert_to_fastq_str(self,threshold):
        '''
            create a read in fastq format. Create an empty string if length of sequence is
            lower than threshold
        '''
        
