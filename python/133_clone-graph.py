# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        mapping = {}

        def clone(node):
            if node in mapping:
                return mapping[node]

            copy = Node(node.val)
            mapping[node] = copy

            for neighbour in node.neighbors:
                copy.neighbors.append(clone(neighbour))

            return copy

        clone(node)

        return mapping[node]

# Time:  O(n)
# Space: O(n)
