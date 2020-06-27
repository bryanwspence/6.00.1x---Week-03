def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    newTuple = aTup[0::2]
    return(newTuple)

testTuple = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(testTuple))

