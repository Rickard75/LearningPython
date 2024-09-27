"""Shortest path algorithm"""
# A dictionary representing a graph, where the key is the node and the value is a list of tuples
# where the first element of the tuple is the node and the second element is the weight of the edge
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)                                                     # list of nodes
    distances = {node: 0 if node == start else float('inf') for node in graph}  # dictionary of distances
    paths = {node: [] for node in graph}                                        # dictionary of paths
    paths[start].append(start)                                                  # add the starting node to the path
    
    while unvisited:
        current = min(unvisited, key=distances.get)                             # get the node with the minimum distance
        for node, distance in graph[current]:                                   # iterate over the neighbors of the current node
            if distance + distances[current] < distances[node]:                 # if the distance is less than the current distance update the distance and the path
                distances[node] = distance + distances[current]                 # update the distance
                if paths[node] and paths[node][-1] == node:                     # if the last element of the path is the node itself, create a new path
                    paths[node] = paths[current][:]                             # copy the path of the current node
                else:                                                           # otherwise, update the path
                    paths[node].extend(paths[current])                          # extend the path of the current node
                paths[node].append(node)                                        # append the node to the path
        unvisited.remove(current)                                               # remove the current node from the unvisited list
    #print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')    # print the results
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    # end of while loop
    
    return distances, paths
    # end of function
    
print('Shortest path algorithm')
print('*********************')
print('Graph with target = A')
shortest_path(my_graph, 'A')
print('*********************')
print('Graph with start = A and target = F')
shortest_path(my_graph,'A','F')
