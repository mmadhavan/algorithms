import sys


class UndirectedGraphCycle(object):
    """
    The difference between this dfs and the other
    dfs is, here we keep track of the prev vertex to
    avoid going back in the same direction in which we
    came from.

    We say the graph has a cycle if it reaches a node that's
    already in the visited dict, If we don't have the prev
    vertex then we might go back in the same direction form
    which we cam from and say cycle exists (since the prev
    vertex will be in visited dict already).

    The reason behind not going backward to the prev node is
    in the example below B has C in its neighbour, now after
    adding B to visited when the control goes to C it will
    check if C's children (in this case B) is in the visited
    set or not (which is the case here). The control will
    simply exit saying cycle exists even before exploring
    all of the other edges.
    """

    def dfs(self, vertex, graph, visited={}, prev=None):
        if vertex not in visited:
            visited[vertex] = prev
            for vertices in graph[vertex]:
                # Don't go back in the direction
                # you came from
                if vertices != prev:
                    self.dfs(vertices, graph, visited, prev=vertex)
        else:
            print '\nCycle exists at {0}'.format(vertex)
            sys.exit(0)


if __name__ == '__main__':
    u_graph = {
        'A': ['B', 'F'],
        'B': ['A', 'C', 'E'],
        'C': ['B', 'D'],
        'D': ['C', 'E'],
        'E': ['B', 'D'],
        'F': ['A']
    }
    ugc = UndirectedGraphCycle()
    ugc.dfs('A', u_graph)
