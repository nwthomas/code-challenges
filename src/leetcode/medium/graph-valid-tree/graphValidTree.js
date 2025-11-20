/*
https://leetcode.com/problems/graph-valid-tree/description

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
true

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output:
false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
*/


class Node {
    /**
     * 
     * @param {number} val
     */
    constructor(val) {
        this.val = val;
        this.neighbors = [];
    }

    /**
     * @param {Node} node
     */
    setNeighbor(node) {
        this.neighbors.push(node);
    }
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @returns {boolean}
 */
const validTree = (n, edges) => {
    const nodes = {};
    Array.from({ length: n }, (_, i) => nodes[i] = new Node(i));
    for (const [node1, node2] of edges) {
        nodes[node1].setNeighbor(nodes[node2]);
        nodes[node2].setNeighbor(nodes[node1]);
    }

    const stack = [[nodes[0], -Infinity]];
    const visited = {};
    while (stack.length) {
        const [node, prev] = stack.pop();
        
        if (visited[node.val]) {
            return false;
        }
        visited[node.val] = true;

        for (const neighbor of node.neighbors) {
            if (neighbor.val !== prev) {
                stack.push([neighbor, node.val]);
            }
        }
    }

    return Object.keys(nodes).length === Object.keys(visited).length;
}


module.exports = { validTree };