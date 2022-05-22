class Queue:
    def __init__(self, data):
        self.queue_data = data

    def add(self, element):
        self.queue_data.append(element)

    def get (self):
        return self.queue_data.pop(0)

queue = Queue([])

graph = {
    "A": ["B", "E"],
    "B": ["A", "D", "C"],
    "C": ["B", "D", "K"],
    "D": ["C", "B"],
    "E": ["A", "K"],
    "K": ["E", "C"]
}
def width_search(graph, start, find):
    visited = []
    visited.append(start)
    queue.add(start)
    while queue.queue_data:
        top = queue.get()
        tops = graph[top]
        for i in tops:
            if i == find:
                break
            if i not in visited:
                visited.append(i)
                queue.add(i)

    for i in visited:
        if find in graph[i] and start in graph[i]:
            path = i

    return path

print(width_search(graph, "A", "D"))