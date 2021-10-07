from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    if len(points) == 0:
        return []

    num_points = len(points)
    num_entries = len(points[0])

    avg = [0]*num_entries

    for idx, el in enumerate(points):
        for i in range(len(el)):
            avg[i] += el[i]
    
    for idx, element in enumerate(avg):
        avg[idx] = element/num_points

    return avg


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = len(set(assignments))

    dim = len(dataset[0])

    #Allocated List for return
    centroids = []

    #Iterate through the samples in each cluster and take cluster mean
    for label in range(k):
        cluster_indices = [idx for idx, el in enumerate(assignments) if el == label ]
        avg_array = [0 for i in range(dim)]
        for index in cluster_indices:
            element = dataset[index]
            avg_array = [a +b for a, b in list(zip(avg_array, element))]
        
        cluster_avg = [feature/len(cluster_indices) for feature in avg_array]


        # cluster_avg = sum([dataset[idx] for idx in cluster_indices])/len(cluster_indices)
        centroids.append(cluster_avg)

    return centroids

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)


def distance_squared(a, b):

    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    import random
    #Extract a list of K random elements from dataset
    centroids = random.sample(list(dataset), k)

    return centroids

def cost_function(clustering):
    cost = 0
    for cluster_id in clustering.keys():
        cluster = clustering.get(cluster_id)
        centroid = point_avg(cluster)
        for entry in cluster:
            cost += distance_squared(entry, centroid)
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """

    centroids = random.sample(list(dataset), 1)

    while(len(centroids) < k):
        max_d = 0
        max_item = []
        for item in dataset:
            distance = sum([distance_squared(item, centroid) for centroid in centroids])
            if distance > max_d:
                max_d = distance
                max_item = item
        centroids.append(max_item)
    
    return centroids


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
