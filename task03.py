import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                if distance < distances.get(neighbor, float('infinity')):
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    
    start_vertex = 'A'
    shortest_paths = graph.dijkstra(start_vertex)
    
    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Вершина {vertex}: {distance}")