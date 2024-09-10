"""Example of a dictionary"""

student = {
    'name'      : 'Riccardo',
    'age'       : 0,
    'university': 'University of Padova',
    'email'     : 'riccardo.carroccio@studenti.unipd',
    'food'      : 'pizza'
}

student['course'] = 'physics'   # adding a new key-value pair
student['age']    = '25'        # changing the value of a key
del student['age']              # deleting a key-value pair

print("Printing using items():")
for i in student.items():
    print(i)
print("\nPrinting using items() with double index:")
for i,j in student.items():
    print(i,j)
print("\nPrinting using values():")
for i in student.values():
    print(i)

print('*****************************************************************************************')
    
"""Shortest path algorithm"""
# A dictionary representing a graph, where the key is the node and the value is a list of tuples
# where the first element of the tuple is the node and the second element is the weight of the edge
my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B',4), ('D',7)],
    'D': [('A',1), ('C',7)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')
    
shortest_path(my_graph, 'A')