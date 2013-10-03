import doctest
from QualityScore import qualityScore
from DNASequence import DNAsequence

class fastqread:
    def __init__(self,fastq_str):
        ''' Take a string corresponding to a read from a fastq file, return 3 attributes: 
            name of sequence, sequence, quality score
            self.seq is a DNAsequence object
            self.score is a qualityScore object
        '''
        input = fastq_str.split("/n")
        self.name = input[0]
        self.seq = DNAsequence(input[1])
        self.score = qualityScore(input[3])
    
    def slide_window(self,threshold):
        ''' slide a window and calculate average. Output the 5 end trim index
            and 3'end trim index according to the threshold. When average is above threshold, the 
            start of the window becomes the 5 end trim index. When the average becomes lower than threshold 
            again, the start of the window is used for 3 end trimming index.
        '''
        windowLen = self.seq.window_size()
        self.score.convert()
        start_cut = 0
        end_cut = 0
        aver = 0
        flag = False
        for i in range(len(self.score.qualList)/windowLen):
            subscore = self.score.qualList[i*windowLen:(i+1)*windowLen]
            aver = sum(subscore)/len(subscore)
            if aver > threshold:
                start_cut = i*windowLen
                flag == True
            if aver < threshold and flag == True:
                end_cut = i*windowLen
        self.trim_seq(start_cut,end_cut)
            

    def trim_seq(self,start_index,end_index):
        '''Trim the sequence and quality score given an index for start and end
        '''
        self.seq.trim(start_index,end_index)
        self.score.trim(start_index,end_index)
    
    def convert_to_fastq_str(self):
        '''
            create a read in fastq format. Create an empty string if length of sequence is
            lower than threshold
        '''
        return '\n'.join([self.name,self.seq.dna_str,"+",self.score.qualString])
     
if __name__ == '__main__':
    import doctest
    doctest.testmod()
