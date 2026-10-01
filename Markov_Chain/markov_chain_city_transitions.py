import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def find_city_sequence(start, t_matrix, cities, lenght):    # find sequence of cities based on transition matrix
    current_city_index = cities.index(start)
    sequence = [start]
    for _ in range(lenght - 1):
        next_index = np.random.choice(len(cities), p=t_matrix[current_city_index])  # more probability for selectiing cities with higher prob
        next = cities[next_index]
        sequence.append(next)
        current_city_index = next_index
    return sequence

def cal_probs_n_step(start, n, t_matrix, cities):   # probabilities after n steps start from 'start' city
    index = cities.index(start)
    t_matrix_n = np.linalg.matrix_power(t_matrix, n)
    probabilities = t_matrix_n[index]
    prob_dict = {city: probabilities[i] for i, city in enumerate(cities)}
    prob_dict = {city: prob for city, prob in prob_dict.items() if city != start}   # just showing prob of other cities except 'start' city
    # prob_dict = {city: prob for city, prob in prob_dict.items()}   # show all cities
    print(f"\nProbability of being in other cities after {n} steps starting from {start}:")
    return prob_dict

def display_markov_graph(cities, t_matrix):
    G = nx.DiGraph()
    G.add_nodes_from(cities)
    for i, city in enumerate(cities):
        for j, next in enumerate(cities):
            if t_matrix[i][j] > 0:
                G.add_edge(city, next, weight=t_matrix[i][j])
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2700, arrowsize=15, node_color='pink', font_weight='bold', font_size=10)
    nx.draw_networkx_edges(G, pos)
    plt.title('Markov Chain graph')
    plt.show()

# transition probabilities
probability_matrix = [
    [0.25, 0.25, 0.25, 0.25],
    [0, 0.25, 0.25, 0.5],
    [0.75, 0, 0.25, 0],
    [1, 0, 0, 0]
]

cities = ['Tehran', 'Esfahan', 'Mashhad', 'Shiraz']

# 1 show transition matrix
t_matrix = np.array(probability_matrix)

print("\nTransition matrix:")
print(t_matrix)
print("\n*===============================*")

# heat map
plt.imshow(t_matrix, cmap='Reds', interpolation='nearest')
plt.title('Transition matrix heat-map')
plt.colorbar()
plt.xticks(np.arange(4), ['Tehran', 'Esfahan', 'Mashhad', 'Shiraz'])
plt.yticks(np.arange(4), ['Tehran', 'Esfahan', 'Mashhad', 'Shiraz'])
plt.xlabel('To')
plt.ylabel('From')
plt.show()

# 2 transition matrix after 2 steps
print("\nTransition matrix after 2 steps:")
print(np.linalg.matrix_power(t_matrix, 2))
print("\n*===============================*")

# 3 sequence of cities starting from Tehran
print("\nSequence of cities (len=25):")
print(find_city_sequence('Tehran', t_matrix, cities, 25))
print("\n*===============================*")

# 4 probabilities in other cities after 2 steps starting from Tehran
print(cal_probs_n_step('Tehran', 2, t_matrix, cities))
print()

# 5 draw Markov-Chain graph
display_markov_graph(cities, t_matrix)