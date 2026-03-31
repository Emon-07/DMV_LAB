import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (greater than 3): "))

if n <= 3:
    print("Please enter a number greater than 3.")
else:
   
    G = nx.complete_graph(n)

    # 3. Draw the graph
    plt.title(f"Complete Graph with {n} Vertices (K{n})")
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray')
    
    plt.show()