import networkx as nx
import matplotlib.pyplot as plt

def draw_hybrid_p2p_graph():
    G = nx.DiGraph()

    # Nodes
    server = "Metadata Server"
    peers = [f"Peer {i}" for i in range(1, 6)]
    files = [f"File {i}" for i in range(1, 6)]

    G.add_node(server, color='red')
    for peer in peers:
        G.add_node(peer, color='blue')

    for file in files:
        G.add_node(file, color='green')

    # Server to Peers (Metadata management)
    for peer in peers:
        G.add_edge(peer, server)  # Peers send metadata to server
        G.add_edge(server, peer)  # Server provides metadata lookup

    # Peer-to-Peer File Transfers
    G.add_edge("Peer 1", "Peer 3")
    G.add_edge("Peer 2", "Peer 4")
    G.add_edge("Peer 3", "Peer 5")
    G.add_edge("Peer 4", "Peer 1")
    G.add_edge("Peer 5", "Peer 2")

    # File ownership
    file_owners = {
        "Peer 1": ["File 1"],
        "Peer 2": ["File 2"],
        "Peer 3": ["File 3"],
        "Peer 4": ["File 4"],
        "Peer 5": ["File 5"]
    }

    for peer, files in file_owners.items():
        for file in files:
            G.add_edge(peer, file)

    # Layouts
    pos = nx.spring_layout(G)
    colors = [G.nodes[node]['color'] for node in G.nodes]

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color=colors, edge_color='gray', arrows=True)
    plt.title("Centralized Metadata Server with Decentralized File Transfers")
    plt.show()

draw_hybrid_p2p_graph()
