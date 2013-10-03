class qualityScore:
    def __init__(self,fastqQual):
        '''Create a string attribute which represent the quality score
           Create a quality list which will contain the quality score of each base
           Input:
            A string from the quality score in fastq format
           Output:
            self.qualString : String
            self.qualList : List of integer
        '''
        self.qualString = fastqQual
        self.qualList = []
        
    def convert(self):
        '''Transform the quality score string element into integer and record them in the qualityNumbers list
           Input:
           Output:
            modify self.qualList
            
            >>> x = qualityScore('^ac')
            >>> x.convert()
            [94]
            
            >>> x = qualityScore('')
            >>> x.convert()
            >>> []
        '''
        for el in self.qualString:
            self.qualList.append(ord(el)) #ord transform the ACSII character into integer
            
    
    def trim(self,start,end):
        '''
        Given a start and an end index trim the quality score string attribute and keep the middle.
        start and end are integers.
        Input: 
            start : Integer
            end : Integer
        Output:
            modify self.qualString and self.qualList
        
        >>> x = qualityScore('^acebeg')
        >>> x.convert()
        >>> x.trim(1, 2)
        >>> self.qualString
        'ac'
        >>> self.qualList
        [97,99]
        '''
        if start>end:
            start, end = end, start
        if start<0: start = 0
        if end > len(self.qualString)+1: end = len(self.qualString)
        self.qualString = self.qualString[start:end+1]
        self.qualList = self.qualList[start:end+1]
        assert len(self.qualList) == len(self.qualString)
        
        
        
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
