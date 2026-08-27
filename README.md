# Shortest Route Finder using Dijkstra's Algorithm

## 📌 Project Overview

The **Shortest Route Finder** is a DAA (Design and Analysis of Algorithms) mini project that finds the shortest path between two locations using **Dijkstra's Algorithm**.

The project represents locations as nodes in a weighted graph, where the edges represent the distances between locations. Dijkstra's Algorithm is used to calculate the shortest possible route from the selected source location to the destination.

## 🎯 Objectives

* Find the shortest route between two locations.
* Understand and implement **Dijkstra's Shortest Path Algorithm**.
* Represent real-world locations using a weighted graph.
* Display the shortest distance and route between selected locations.
* Provide a simple visualization of the calculated path.

## 🛠️ Technologies Used

* **Python**
* **Dijkstra's Algorithm**
* **NetworkX** – Graph creation and path analysis
* **Matplotlib** – Graph visualization

## ⚙️ Algorithm

### Dijkstra's Algorithm

Dijkstra's Algorithm is a greedy algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.

### Steps

1. Select the source location.
2. Assign a distance of `0` to the source and infinity to all other locations.
3. Select the unvisited location with the smallest known distance.
4. Update the distances of its neighboring locations.
5. Mark the current location as visited.
6. Repeat until the destination is reached or all reachable locations are processed.
7. Reconstruct and display the shortest route.

## 🗺️ Project Features

* 📍 Multiple location nodes
* 🛣️ Distance-based weighted graph
* 🔍 Source and destination selection
* ⚡ Shortest route calculation
* 📏 Shortest distance calculation
* 📊 Graph visualization
* 🟢 Highlighting of the shortest path

## 📂 Project Structure

```text
Shortest-Route-Finder/
│
├── shortest_route.py
├── README.md
└── requirements.txt
```

## 📦 Requirements

Install the required Python libraries using:

```bash
pip install networkx matplotlib
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/Shortest-Route-Finder.git
```

2. Open the project folder:

```bash
cd Shortest-Route-Finder
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Python program:

```bash
python shortest_route.py
```

5. Select the source and destination locations when prompted.

6. The program will display the shortest route, total distance, and graph visualization.

## 📊 Example

```text
Source      : Bangalore
Destination : Mysore

Shortest Route:
Bangalore → Ramanagara → Mandya → Mysore

Shortest Distance:
XXX km
```

*The actual route and distance depend on the locations and edge weights defined in the project.*

## ⏱️ Time Complexity

For Dijkstra's Algorithm using a priority queue:

**Time Complexity:** `O((V + E) log V)`

Where:

* `V` = Number of vertices (locations)
* `E` = Number of edges (connections)

**Space Complexity:** `O(V + E)`

## 🚀 Future Enhancements

* Add more real-world locations.
* Integrate real-time map data.
* Add an interactive GUI.
* Add traffic-aware route calculation.
* Provide multiple route alternatives.
* Integrate Google Maps or OpenStreetMap data.

## 👩‍💻 Author

**Spandana**

B.E. Computer Science Engineering

## 📄 License

This project is created for educational and academic purposes.
