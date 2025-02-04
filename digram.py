import matplotlib.pyplot as plt
import networkx as nx

# Create a new directed graph for the circuit
G = nx.DiGraph()

# Add nodes (components)
components = [
    "Power Supply (5V/3.3V)", "Raspberry Pi", 
    "PIR Sensor", "Ultrasonic Sensor", "Thermal Camera", 
    "LoRa Module", "LED", "Buzzer"
]

for component in components:
    G.add_node(component)

# Add edges (connections)
connections = [
    ("Power Supply (5V/3.3V)", "Raspberry Pi"),
    ("Power Supply (5V/3.3V)", "PIR Sensor"),
    ("Power Supply (5V/3.3V)", "Ultrasonic Sensor"),
    ("Power Supply (5V/3.3V)", "Thermal Camera"),
    ("Power Supply (5V/3.3V)", "LoRa Module"),
    ("Raspberry Pi", "PIR Sensor"),
    ("Raspberry Pi", "Ultrasonic Sensor"),
    ("Raspberry Pi", "Thermal Camera"),
    ("Raspberry Pi", "LoRa Module"),
    ("Raspberry Pi", "LED"),
    ("Raspberry Pi", "Buzzer")
]

for conn in connections:
    G.add_edge(*conn)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for nodes

# Draw nodes and edges with labels
nx.draw(
    G, pos, with_labels=True, node_color="lightblue", node_size=3000,
    font_size=10, font_weight="bold", edge_color="gray", width=1.5,
    arrowsize=20, connectionstyle="arc3,rad=0.2"
)

# Show the diagram
plt.title("Circuit Diagram for Smart Wildlife Detection and Alert System", fontsize=14)
plt.show()
