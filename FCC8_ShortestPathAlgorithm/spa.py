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

def shortest_path(graph, start):
    unvisited = []                          # list to store the nodes that have not been visited
    distances = {}                          # dictionary to store the distance of each node from the start node
    for node in graph:
        unvisited.append(node)              # add all nodes to the unvisited list
        if node == start:                   # set the distance of the starting node to 0
            distances[node] = 0
        else:
            distances[node] = float('inf')  # set the distance of all other nodes to infinity
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

# step 40 on freeCodeCamp
shortest_path(my_graph,'A')