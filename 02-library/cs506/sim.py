def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):

    if x == [] or y == []:
        raise ValueError("lengths must not be zero")

    #Source: https://www.statology.org/manhattan-distance-python/
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    x_set = set(x)
    y_set = set(y)
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    dist = (len(x_set.union(y_set)) - len(x_set.intersection(y_set)))/len(x_set.union(y_set))
    return dist

def cosine_sim(x, y):

    #Check for edge cases
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    elif len(x) != len(y):
        raise ValueError("lengths must be equal")

    #Get dot product
    dot_prod = sum(abs(val1*val2) for val1, val2 in zip(x,y))

    #Calculate X and Y lengths
    x_len = (sum(el**2 for el in x))**(1/2)
    y_len = (sum(el**2 for el in y))**(1/2)

    #Calculate cos
    cos = dot_prod/(x_len * y_len)

    return cos

# Feel free to add more
