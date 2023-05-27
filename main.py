import networkx as nx
import itertools
import random

#connectivity_making
bank_addresses = [
    'City_Bank_Uttara_Branch', 
    'City_Bank_Airport', 
    'City_Bank_Nikunjo', 
    'City_Bank_Beside_Uttara_Diagonostic',
    'City_Bank_Mirpur_12',
    'City_Bank_Le_Meredien',
    'City_Bank_Shaheed_Sharani',
    'City_Bank_Narayanganj',
    'City_Bank_Pallabi',
    'City_Bank_JFP'
]

# Create a graph representing the cities and distances between them
G = nx.Graph()

for item in range(1,5000):

    starting = random.choice(bank_addresses)
    ending = random.choice(bank_addresses)
    distance = random.randint(1,50)

    if starting != ending:
        G.add_edge(starting, ending, weight=distance)

# Define the function to calculate the total distance of a given path
def calculate_path_distance(graph, path):
    total_distance = 0
    
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]['weight']

    return total_distance

# Generate all possible permutations of cities
cities = list(G.nodes)
all_permutations = itertools.permutations(cities)

# Find the shortest path among all permutations
shortest_distance = float('inf')
shortest_path = None
for permutation in all_permutations:
    distance = calculate_path_distance(G, permutation)
    if distance < shortest_distance and permutation[0] == bank_addresses[0]:
        shortest_distance = distance
        shortest_path = permutation
        
route = ''

for item in shortest_path:
    route += f'{item} -> '

route = route[:-3]

print("Best Route:", route)