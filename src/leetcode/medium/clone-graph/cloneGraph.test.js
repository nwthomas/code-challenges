const { cloneGraph, Node } = require("./cloneGraph.js");

describe("Clone Graph", () => {
    let node;
    let second;
    let third;
    let fourth;

    beforeEach(() => {
        node = new Node(1, []);

        second = new Node(2, []);
        third = new Node(3, []);
        fourth = new Node(4, []);
        node.neighbors.push(second, fourth);
        second.neighbors.push(node, third);
        third.neighbors.push(second, fourth);
        fourth.neighbors.push(node, third);
    });

    it("returns undefined if no node is given as input", () => {
        const result = cloneGraph();
        expect(result).toBe(undefined);
    });

    it("returns a singular node if only one node with no neighbors is given", () => {
        const newNode = new Node(1, []);
        const result = cloneGraph(newNode);
        expect(result.val).toEqual(newNode.val);
        expect(result.neighbors).toEqual(newNode.neighbors);
    });

    it("returns a deeploy cloned graph", () => {
        const result = cloneGraph(node);
        expect(result === node).toBe(false);

        const clonedSecondNode = result.neighbors.find(
            (node) => node.val === 2,
        );
        const clonedThirdNode = clonedSecondNode.neighbors.find(
            (node) => node.val === 3,
        );
        const clonedFourthNode = result.neighbors.find(
            (node) => node.val === 4,
        );
        expect(clonedSecondNode === second).toBe(false);
        expect(clonedThirdNode === third).toBe(false);
        expect(clonedFourthNode === fourth).toBe(false);
    });
});
