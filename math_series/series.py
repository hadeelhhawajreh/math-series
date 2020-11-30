# true 
'''
def fibonacci(x):
    if x == 0:
        return(x)
    elif x == 1:
        return(x)
    else:
        empty = []
        empty.append(0)
        empty.append(1)
        for i in range(2, x):
            empty.append(empty[i-1]+empty[i-2])
        return empty

def lucas(x):
    if x == 0:
        return(x)
    elif x == 1:
        return(x)
    else:
        arr = []
        a = 1
        b = 2
        arr.append(a)
        arr.append(b)
        for j in range(2, x):
            arr.append(arr[j-1]+arr[j-2])
        return arr
'''

def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1 
    return fibonacci(x-1)+fibonacci(x-2)

def lucas(x):
    if x == 0:
        return 2
    if x == 1:
        return 1 
    return lucas(x-1)+lucas(x-2)

def other(x,y,z):
    if x == 0:
        return y
    if x == 1:
        return z
    return other(x-1,y,z)+other(x-2,y,z)


def sum_series(n,y=0,j=1):
    if y==0 and j==1:
        return fibonacci(n)
    elif y==2 and j==1:
        return lucas(n)
    else:
        return other(n,y,j)

print('sum =',sum_series(5,0,1))
print('sum =',sum_series(5,2,1))
print('sum =',sum_series(5,5,3))