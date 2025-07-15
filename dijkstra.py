import heapq

def dijkstra(graph, start):
   
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    
    priority_queue = [(0, start)]

    while priority_queue:
        curr_distance, curr_vertex = heapq.heappop(priority_queue)

        # Пропускаємо, якщо поточна відстань більша за вже знайдену
        if curr_distance > distances[curr_vertex]:
            continue

       
        for neighbor, weight in graph[curr_vertex].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3},
    'E': {'C': 8, 'D': 3}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)


print(f"Найкоротші шляхи від вершини '{start_vertex}':")
for vertex, distance in shortest_paths.items():
    print(f"  ➤ До '{vertex}': {distance}")