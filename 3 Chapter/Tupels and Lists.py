
### Def oddTuples

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    return (aTup[::2])


print (oddTuples(('I', 'am', 'a', 'test', 'tuple')))


#############MAP PURPOSES#####


def add_one(x):
    return x + 1


for num in map(add_one,[1,2,3,4,5,6]):
    print (num)


def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])

###### Doctonaries######


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    summa = 0
    for tab in aDict.values():
        summa += len(tab)
    return  summa

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big=0
    for tab in aDict.keys():
        if len(aDict[tab]) >= big:
            biggest = tab
    return big