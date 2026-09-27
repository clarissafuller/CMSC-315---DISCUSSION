"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph and return the visit order.

    Why a queue: a queue is first-in, first-out (FIFO). Nodes discovered
    first are processed first, so every node at distance 1 from the start
    is visited before any node at distance 2, and so on. That FIFO order
    is what makes BFS move level by level.

    Why neighbors are added to the queue: when a node is visited, its
    unvisited neighbors are the next layer outward. Adding them to the
    back of the queue schedules them after everything already waiting,
    which keeps the layers in order.

    How BFS differs from DFS: depth-first search uses a stack (or
    recursion), so it follows one path as deep as possible before
    backtracking. BFS spreads out evenly from the start instead, which is
    why BFS finds the shortest path (fewest edges) in an unweighted graph
    and DFS does not guarantee that.
    """
    # Handle a missing start node safely instead of raising a KeyError.
    if start not in graph:
        return []

    visited = {start}         # Nodes already discovered, so none is queued twice
    queue = deque([start])    # deque gives O(1) removal from the front
    order = []                # The order nodes are visited in

    while queue:
        # Take the node that has been waiting the longest.
        current = queue.popleft()
        order.append(current)

        # Queue each neighbor we haven't seen yet. Marking it visited now,
        # when it's queued rather than when it's removed, prevents the same
        # node from being added again by another neighbor.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_levels(graph, start):
    """
    Return BFS results grouped by level (distance from the start),
    to make the level-by-level behavior visible.
    """
    if start not in graph:
        return []

    visited = {start}
    current_level = [start]
    levels = []

    while current_level:
        levels.append(current_level)
        next_level = []
        # Every unvisited neighbor of this level belongs to the next level.
        for node in current_level:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)
        current_level = next_level

    return levels


def display_graph(graph):
    """Print each node and its neighbors."""
    if not graph:
        print("  (empty graph)")
        return
    for node, neighbors in graph.items():
        print(f"  {node:<12} -> {', '.join(neighbors) if neighbors else '(none)'}")


def display_levels(graph, start):
    """Print each BFS level on its own line."""
    for distance, nodes in enumerate(bfs_levels(graph, start)):
        print(f"  Level {distance}: {', '.join(nodes)}")


def add_edge(graph, a, b):
    """Add an undirected edge, creating either node if needed."""
    graph.setdefault(a, [])
    graph.setdefault(b, [])
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    # This graph models a small office computer network.
    # Nodes are network devices, and edges are direct connections
    # (cables or wireless links) that data can travel across.
    # The graph is undirected, since data can travel both ways on a link.
    print("\n=== GRAPH STRUCTURE ===")
    network = {
        "Router":    ["Switch A", "Switch B"],
        "Switch A":  ["Router", "Laptop", "Printer"],
        "Switch B":  ["Router", "WebServer", "Database"],
        "Laptop":    ["Switch A"],
        "Printer":   ["Switch A"],
        "WebServer": ["Switch B", "Database"],
        "Database":  ["Switch B", "WebServer"],
    }
    display_graph(network)

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    # Starting from the Router, BFS first visits everything one hop away
    # (the switches), then everything two hops away (the devices behind
    # them). This mirrors how a network broadcast spreads outward.
    print("\n=== BFS TRAVERSAL ===")
    print("Start: Router")
    print(f"  Visit order: {bfs(network, 'Router')}")
    display_levels(network, "Router")

    # Add a new node and edge: a backup server plugged into the Database.
    # Work on a copy so the original network stays available for comparison.
    updated = {node: list(neighbors) for node, neighbors in network.items()}
    add_edge(updated, "Database", "Backup")

    print("\nAfter adding Backup (connected to Database):")
    print(f"  Visit order: {bfs(updated, 'Router')}")
    display_levels(updated, "Router")
    print("  Backup appears at Level 3 because the shortest route to it is")
    print("  Router -> Switch B -> Database -> Backup, three hops away.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # 1. Different starting node
    print("\n1. Starting from Laptop instead of Router:")
    print(f"  Visit order: {bfs(network, 'Laptop')}")
    display_levels(network, "Laptop")
    print("  Same nodes are reached, but the levels change because distance")
    print("  is measured from the new start. The Router is now two hops away.")

    # 2. Disconnected graph
    disconnected = {node: list(neighbors) for node, neighbors in network.items()}
    disconnected["Guest Laptop"] = ["Guest Phone"]
    disconnected["Guest Phone"] = ["Guest Laptop"]
    print("\n2. Disconnected graph (separate guest network added):")
    print(f"  From Router: {bfs(disconnected, 'Router')}")
    print(f"  From Guest Laptop: {bfs(disconnected, 'Guest Laptop')}")
    print("  BFS only reaches nodes connected to the start. The guest devices")
    print("  never appear from the Router, and vice versa, so BFS can be used")
    print("  to check whether two devices can reach each other.")

    # 3. Missing start node
    print("\n3. Missing start node ('Tablet'):")
    print(f"  Visit order: {bfs(network, 'Tablet')}")
    print("  The start check returns an empty list instead of crashing.")

    # 4. Single-node graph
    single = {"Router": []}
    print("\n4. Single-node graph:")
    print(f"  Visit order: {bfs(single, 'Router')}")
    print("  The start is visited, it has no neighbors, and the queue empties.")

    # 5. Empty graph
    print("\n5. Empty graph:")
    print(f"  Visit order: {bfs({}, 'Router')}")
    print("  There are no nodes, so the start can't exist. BFS returns [].")


if __name__ == "__main__":
    main()