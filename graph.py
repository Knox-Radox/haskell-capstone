import networkx as nx
import matplotlib.pyplot as plt

def draw_file_sharing_graphs():
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # Centralized File-Sharing System
    G_centralized = nx.DiGraph()
    server = "Central Server"
    clients = [f"Client {i}" for i in range(1, 6)]

    G_centralized.add_node(server, color='red')
    for client in clients:
        G_centralized.add_node(client, color='blue')
        G_centralized.add_edge(client, server)
        G_centralized.add_edge(server, client)

    pos_centralized = nx.spring_layout(G_centralized)
    colors_centralized = [G_centralized.nodes[node]['color'] for node in G_centralized.nodes]
    nx.draw(G_centralized, pos_centralized, with_labels=True, node_color=colors_centralized, ax=axs[0], edge_color='gray')
    axs[0].set_title("Centralized File-Sharing System")

    # Peer-to-Peer (P2P) File-Sharing System
    G_p2p = nx.Graph()
    peers = [f"Peer {i}" for i in range(1, 6)]

    G_p2p.add_nodes_from(peers, color='blue')
    edges = [("Peer 1", "Peer 2"), ("Peer 1", "Peer 3"), ("Peer 2", "Peer 4"),
             ("Peer 3", "Peer 4"), ("Peer 4", "Peer 5"), ("Peer 2", "Peer 5")]

    G_p2p.add_edges_from(edges)

    pos_p2p = nx.circular_layout(G_p2p)
    colors_p2p = [G_p2p.nodes[node]['color'] for node in G_p2p.nodes]
    nx.draw(G_p2p, pos_p2p, with_labels=True, node_color=colors_p2p, ax=axs[1], edge_color='gray')
    axs[1].set_title("Peer-to-Peer (P2P) File-Sharing System")

    plt.show()

draw_file_sharing_graphs()
