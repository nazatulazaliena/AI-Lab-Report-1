import streamlit as st

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Breadth First Search & Depth First Search Graph", use_container_width=True)

# --- Define graph ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# --- BFS function ---
def bfs(graph, start_node):
    visited = []
    queue = []
    traversal_order = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        traversal_order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return traversal_order

# --- DFS function ---
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = []
    visited.append(start_node)

    for neighbour in graph[start_node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

# --- Streamlit UI ---
st.title("Graph Traversal Visualizer (BFS & DFS)")
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))
algorithm = st.radio("Choose Algorithm:", ("Breadth First Search (BFS)", "Depth First Search (DFS)"))

if st.button("Run Traversal"):
    if algorithm == "Breadth First Search (BFS)":
        order = bfs(graph, start_node)
        st.subheader("BFS Traversal Order:")
        st.write(" → ".join(order))
    else:
        order = dfs(graph, start_node)
        st.subheader("DFS Traversal Order:")
        st.write(" → ".join(order))
