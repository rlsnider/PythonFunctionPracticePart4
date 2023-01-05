"""Write a Python function called max_num() to find the maximum of three numbers."""

def max_num(a,b,c):
        return max([a,b,c])
   

print(max_num(199, 205, 300))

"""Write a Python function called mult_list() to multiply all the numbers in a list."""
def mult_list(lst):
    if len(lst) == 0:
        return 0
    num = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            num = num * i
    return num
print(mult_list([1,2,3,4]))
    
"""Write a function called num_within() to check wheter a number falls in a given range???Had to look to see what they wanted on this one"""
def num_within(x,a,b):
    return x in range(a,b+1)

print(num_within(3,2,4))
"""I looked up the answer, and still don't get it."""

"""Write a Python function called pascal() that prints out the first n rows of Pascal's triangle."""

def pascal(rows):
    t = []
    for i in range(rows):
        t.append([])
        t[i].append(1)
        for j in range(1,i):
            t[i].append(t[i-1][j-1]+t[i-1][j])
        if i !=0:
            t[i].append(1)
    return t
print(pascal(0))   

def printPascal(t):
    printString = " "
    for i in range(0, len(t)):
        printString = " " * (len(t)-i)
        for j in range(0, len(t[i])):
            printString = printString + str(t[i][j]) + " "
        print(printString)
printPascal(pascal(0))

"""I checked my answer with the solution guide. This way makes more sense to me. I studied the solution guide and then this one, and I really am still not 100%. I'm going to be spending a lot of time outside of class in the next couple of weeks on w3schools and free Code Camp."""