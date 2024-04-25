from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):

  visited = {source: (0, 0)}
  queue = deque([(source)])
  while queue:
    current = queue.popleft()

    distance, edges = visited[current]

    for neighbor, weight in graph[current]:
      new_distance = distance + weight
      new_edges = edges + 1
      if neighbor not in visited:
        visited[neighbor] = (new_distance, new_edges)
        queue.append(neighbor)
      else:
        if new_distance < visited[neighbor][0]:
          visited[neighbor] = (new_distance, new_edges)
        elif new_distance == visited[neighbor][0] and new_edges < visited[
            neighbor][1]:
          visited[neighbor] = (new_distance, new_edges)
        else:
          continue
  return visited


def bfs_path(graph, source):

  queue = deque([source])
  visited = {source: " "}

  while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
      if neighbor not in visited:
        visited[neighbor] = current
        queue.append(neighbor)

  return visited


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):

  path = []
  current = destination
  while not current == " ":
    path.append(current)
    current = parents[current]

  path = path[1:]
  path = reversed(path)
  return ''.join(path)


graph = {
            's': {('a', 1), ('c', 4)},
            'a': {('b', 2)}, # 'a': {'b'},
            'b': {('c', 1), ('d', 4)}, 
            'c': {('d', 3)},
            'd': {},
            'e': {('d', 0)}
        }
