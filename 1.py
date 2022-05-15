'''pattern'''
'''we use dictionaries here'''
path1 = 'dru'
'''we take a particular direction as main and further we manage it according to'''


def clock(path1):
    '''the path1 rotates in clockwise direction'''
    RC = {'d': 'l', 'r': 'd', 'u': 'r', 'l': 'u'}
    '''according to main one we mentioned in which direction it rotates'''
    newpath1 = ''
    i = 0
    while i < len(path1):
        newpath1 = newpath1+RC[path1[i]]
        i = i+1
    return newpath1


def anti(path1):
    '''the path1 rotates into anti clockwise direction'''
    LA = {'d': 'r', 'r': 'u', 'u': 'l', 'l': 'd'}
    '''according to main one we have mentioned in which direction it rotates'''
    newpath12 = ''
    i = 0
    while i < len(path1):
        newpath12 = newpath12+LA[path1[i]]
        i = i+1
    return newpath12


def opposite(path1):
    '''exact opposite of the path1 we have taken as main'''
    OP = {'d': 'u', 'u': 'd', 'l': 'r', 'r': 'l'}
    '''according to main one we mentioned in which direction it rotates'''
    newpath13 = ''
    i = 0
    while i < len(path1):
        newpath13 = newpath13+OP[path1[i]]
        i = i+1
    return newpath13


def reverseFunc(path1):
    '''we want reverse of opposite so, this fuction is written'''
    k = ''
    i = 0
    while i < len(path1):
        k = path1[i]+k
        i = i+1
    return k


def assign_num(path1):
    '''we have written the code but we have to assign numbers so we written this function'''
    y = {'d': (1, 0), 'r': (0, 1), 'u': (-1, 0), 'l': (0, -1)}
    return y[path1]


def addingpath1(coordi, path1):
    return (coordi[0]+assign_num(path1)[0], coordi[1]+assign_num(path1)[1])


def displayAll(n):
    path1 = 'dru'
    if(n == 1):
        return path1
    else:
        i  = 0
        while i< n-1:
            nxtpath1 = reverseFunc(opposite(anti(path1)))+'d'+path1 + \
                'r'+path1+'u'+reverseFunc(opposite(clock(path1)))
            path1 = nxtpath1
            i = i+1
        return nxtpath1


print(displayAll(2))


def display(n):
    l = []
    j = (1, 1)
    l.append(j)
    for i in displayAll(n):
        j = addingpath1(j, i)
        l.append(j)
    return l


print(display(2))
print(display(3))
'''done'''
