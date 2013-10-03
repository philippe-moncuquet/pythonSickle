def trim(x,start,end):
    ''' Trim an object x from start to end index including end index
        Input: 
            x is indexed object (e.g.: list or string)
            start : Integer
            end : Integer
        Output:
            modify x
        
        >>> trim('abc',1,2)
        'bc'
        >>> trim([1,2,3],1,2)
        [2, 3]
        >>> trim('abc',2,1)
        'bc'
        >>> trim('abc',-2,1)
        'ab'
        >>> trim('abc',1,8)
        'bc'
        >>> trim('abc',-3,8)
        'abc'
        >>> trim('abc',1,1)
        'b'
        >>> trim('abc',4,6)
        ''
        >>> trim([1,2,3],-3,-1)
        []
    '''
    if start>end:
        start, end = end, start
    if len(set(range(len(x))).intersection(set(range(start,end+1)))) == 0:
        end = start - 1
    if start<0: start = 0
    if end > len(x): end = len(x)
    return x[start:end+1]
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
