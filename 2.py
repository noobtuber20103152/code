# defined a function that rotates a input in clockwise direction.
def clockwise(l):
    newstring = ''  # take a variable empty string
    a = {'d': 'l', 'r': 'd', 'u': 'r', 'l': 'u'}  # defined a dictionary
    i = 0
    while i < len(l):  # applied a for loop for range l
        newstring = newstring+a[l[i]]
        i = i+1  # delevering values in empty string using dictionary
    return newstring  # take its return


def anti(l):  # defined a function that rotates a input in anticlockwise direction.
    newstring = ''  # take a variable empty string
    a = {'d': 'r', 'r': 'u', 'u': 'l', 'l': 'd'}  # defined a dictionary
    i = 0
    while i < len(l):  # applied for loop in range l
        newstring = newstring+a[l[i]]
        i = i+1  # delevering values in empty string using dictionary
    return newstring  # taking its return


def rev(l):  # defined a reverse function that reverses input
    newstring = ''
    i = 1  # take a empty string
    while i< len(l) + 1:  # applied for loop
        newstring = newstring+l[-i]  # appending values in empty string
        i = i+1
    return newstring  # take defined functions return


def compo(l):  # defined a function that takes composite of given input
    newstring = ''  # defined a empty string
    a = {'d': 'u', 'u': 'd', 'l': 'r', 'r': 'l'}  # making a dictionary
    i = 0
    while i < len(l):  # applying a for loop
        newstring = newstring+a[l[i]]
        i = i+1  # appending values in empty string by changing with dictionary
    return newstring  # take this functions return


# defined a function that change strings in cordinates using dictionary
def changeCoordinates(l):

    # strings in cordinates using dictionary
    a = {'d': (1, 0), 'u': (-1, 0), 'r': (0, 1), 'l': (0, -1)}
    return a[l]  # take functions return


def move(point, l):                    # defined a function that takes two input a point and a string
    # using previous function changing cordinates accordinly
    return (point[0]+changeCoordinates(l)[0], point[1]+changeCoordinates(l)[1])


def function1(n):  # defining a function that takes input and executes accordingly
    base = 'dru'  # take a variable
    if n == 1:  # if taken input is 1
        return base  # then simply return the same

    else:                        # if taken input is not 1 then execute this
        i = 0
        while i < n-1:  # applying for loop for pattern accordingly
            newstring = rev(compo(anti(base)))+'d'+base + 'r' + base + 'u' + \
                rev(compo(clockwise(base))
                    )  # defining a pattern for next input
            base = newstring  # changing base to newstring for again input
            i = i+1
        return newstring  # returning newstring for executing function


def display(n):  # defined a function that takes input and making a final pattern according to input
    s = []  # take a empty list
    t = (1, 1)  # defined a tuple for starting coordinate
    s.append(t)  # appending t in s list
    str = function1(n)
    i = 0
    while i< len(str): # applying for loop
        t = move(t, str[i])  # using another move function creating values in t
        s.append(t)  # appending t values in s
        i = i+1
    return s  # taking functions return


print(display(2))
