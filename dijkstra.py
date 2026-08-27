import tkinter as tk
from tkinter import ttk, messagebox
import sys
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

# 📍 Bangalore Locations
locations = [
    "Hebbal","Yelahanka","Yeshwanthpur","Malleshwaram","Majestic",
    "MG Road","Brigade Road","Shivajinagar","Indiranagar","Domlur",
    "Marathahalli","Whitefield","Koramangala","HSR Layout","BTM Layout",
    "Jayanagar","Banashankari","Vijayanagar","Rajajinagar","Electronic City"
]

# 🚧 Base Graph (distance)
graph = [
[0,6,7,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[6,0,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[7,5,0,4,5,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0],
[5,6,4,0,3,0,0,5,0,0,0,0,0,0,0,0,0,5,6,0],
[0,0,5,3,0,4,5,5,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,4,0,2,3,4,3,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,2,0,2,3,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,5,5,3,2,0,4,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,4,3,4,0,2,4,6,0,0,0,0,0,0,0,0],
[0,0,0,0,0,3,0,0,2,0,3,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,4,3,0,3,5,6,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,6,0,3,0,4,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,5,4,0,3,4,5,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,6,0,3,0,2,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,4,2,0,3,0,0,0,6],
[0,0,0,0,0,0,0,0,0,0,0,0,5,0,3,0,4,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,5,0,0],
[0,0,6,5,0,0,0,0,0,0,0,0,0,0,0,0,5,0,3,0],
[0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,4,0]
]

# 🚦 Traffic Generator
def generate_traffic():
    n = len(locations)
    t = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                t[i][j] = random.choice([1,1,2,2,3])
    return t

# 🚀 Dijkstra Algorithm
def dijkstra(src, dest, traffic):
    n = len(graph)
    dist = [sys.maxsize]*n
    vis = [False]*n
    parent = [-1]*n

    dist[src] = 0

    for _ in range(n):
        u = -1
        mn = sys.maxsize

        for i in range(n):
            if not vis[i] and dist[i] < mn:
                mn = dist[i]
                u = i

        vis[u] = True

        for v in range(n):
            if graph[u][v]:
                cost = graph[u][v] * traffic[u][v]
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parent[v] = u

    path = []
    cur = dest
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[dest], path

# 🗺️ MAP DISPLAY
def show_map(path, src, dest, traffic):
    G = nx.Graph()

    for i in range(len(locations)):
        G.add_node(i)

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]:
                G.add_edge(i, j)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(12,8))

    plt.title(f"{locations[src]} → {locations[dest]}", fontsize=14, fontweight="bold")

    nx.draw(
        G, pos,
        labels={i: locations[i] for i in range(len(locations))},
        node_color="lightblue",
        node_size=1500,
        font_size=8
    )

    # 🚦 traffic edges
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]:
                color = "green" if traffic[i][j]==1 else "orange" if traffic[i][j]==2 else "red"
                nx.draw_networkx_edges(G, pos, edgelist=[(i,j)], edge_color=color)

    # 🔵 shortest path
    edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="blue", width=4)

    # 📌 LEGEND
    plt.legend(handles=[
        mpatches.Patch(color="green", label="Low Traffic"),
        mpatches.Patch(color="orange", label="Medium Traffic"),
        mpatches.Patch(color="red", label="Heavy Traffic"),
        mpatches.Patch(color="blue", label="Shortest Path")
    ], loc="lower left")

    plt.show()

# 🖥️ MAIN FUNCTION
def find_route():
    if combo_src.get()=="" or combo_dest.get()=="":
        messagebox.showerror("Error","Select Source & Destination")
        return

    s = locations.index(combo_src.get())
    d = locations.index(combo_dest.get())

    traffic = generate_traffic()

    dist, path = dijkstra(s, d, traffic)

    result_label.config(text=
    f"📍 Source: {combo_src.get()}\n"
    f"🎯 Destination: {combo_dest.get()}\n\n"
    f"🚦 Shortest Distance: {dist} km\n\n"
    f"🛣️ Optimized Route:\n"
    f"{' → '.join([locations[i] for i in path])}"
)

    show_map(path, s, d, traffic)

# 🎨 UI (FINAL DASHBOARD)
root = tk.Tk()
root.title("🚦 Shortest Route Finder")
root.geometry("750x600")
root.configure(bg="#1e1e2f")

# HEADER
header = tk.Frame(root, bg="#2c2f4a", height=60)
header.pack(fill="x")

tk.Label(header,
         text="🚦 Shortest Route Finder",
         bg="#2c2f4a",
         fg="white",
         font=("Arial",16,"bold")).pack(pady=15)

# CARD
card = tk.Frame(root, bg="white")
card.place(x=50, y=100, width=650, height=450)

# SOURCE
tk.Label(card,
         text="📍 Enter Source Location",
         bg="white",
         font=("Arial",11,"bold")).pack(pady=(20,5))

combo_src = ttk.Combobox(card, values=locations, width=50)
combo_src.pack()

# DESTINATION
tk.Label(card,
         text="🎯 Enter Destination Location",
         bg="white",
         font=("Arial",11,"bold")).pack(pady=(20,5))

combo_dest = ttk.Combobox(card, values=locations, width=50)
combo_dest.pack()

# BUTTON
tk.Button(card,
          text="🚀 Find Best Route",
          bg="#4CAF50",
          fg="white",
          font=("Arial",12,"bold"),
          command=find_route).pack(pady=20)

# RESULT
result_label = tk.Label(card,
                        text="",
                        bg="white",
                        justify="left",
                        font=("Arial",11))
result_label.pack()

root.mainloop()