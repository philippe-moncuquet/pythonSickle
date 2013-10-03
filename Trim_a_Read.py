from QualityScore import qualityScore

def trim_a_read(read,threshold):
    '''Read is a string corresponding to 4 lines of a fastq file. Threshold is the average threshold used to determine trimming.
        Return a trimmed read in the same format'''
    x = fastqread(read)
    x.slide_window(threshold)
    return x.convert_to_fasq_str()
    

if __name__ == '__main__':
    import doctest
    import sys
    read = sys.argv[1]
    threshold = sys.argv[2]
    print trim_a_read(read,threshold)
