__author__ = 'wolfram'

dest = [0]
next = [0]
weight = [0]
head = [0]
priorities = [0]
from_list = [0]
en = 0
begin_vertex = 0

def giving_priorities(u):
    global dest, next, head, priorities, from_list, begin_vertex
    j = head[u]
    while j != 0:
        if ((priorities[dest[j]] == 0) | (priorities[dest[j]] > weight[j] + priorities[u])) & (dest[j] != begin_vertex):
            priorities[dest[j]] = weight[j] + priorities[u]
            from_list[dest[j]] = u
            giving_priorities(dest[j])
        j = next[j]

def dijkstra(u, v):
    global dest, next, head, priorities, from_list, begin_vertex
    begin_vertex = u
    giving_priorities(u)
    if u == v:
        return [u]
    if priorities[v] == 0:
        return []
    answer = [v]
    j = v
    while j != u:
        answer.append(from_list[j])
        j = from_list[j]
    answer = [i for i in reversed(answer)]
    return answer

class WeightedGraph:

    def add_vertex(self, v):
        global head, priorities, from_list
        if v > len(head) - 1:
            for i in range(v - len(head) + 1):
                head.append(0)
                priorities.append(0)
                from_list.append(0)

    def add_direct_link(self, v1, v2, w):
        global dest, next, head, en, weight
        if len(dest) < len(head) * (len(head) - 1):
            for i in range(len(head) * (len(head) - 1) - len(dest) + 1):
                dest.append(0)
                weight.append(0)
                next.append(0)
        en += 1
        weight[en] = w
        dest[en] = v2
        next[en] = head[v1]
        head[v1] = en

    def paths(self, w):
        all_paths_from_w = []
        for i in range(len(head)):
            all_paths_from_w.append(dijkstra(w, i))
        return all_paths_from_w

if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_direct_link(2, 1, 6)
    graph.add_direct_link(2, 3, 4)
    print(graph.paths(2))