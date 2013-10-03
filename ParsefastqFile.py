import sys
from itertools import islice

input_file = sys.argv[1]


with open(input_file) as f:
    lines=[]
    while True:
        line=list(islice(f,4))
        #islice returns an iterator ,so you convert it to list here.
        if line:                     
            #do something with current set of <=4 lines here
            lines.append(line)       # may be store it 
        else:
            break
    print lines
