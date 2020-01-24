const { findSumInBinaryTree, Node } = require("./binaryTreeAddition.js");

const utils = {
    smallNumberArray: [5, 8, 1, 4, 10, 9, 8, 3],
    createBinarySearchTree: function createBinarySearchTree(numberArray) {
        const rootNode = new Node(numberArray[0]);
        numberArray.forEach((num, i) => {
            i && rootNode.addValue(num);
        });
        return rootNode;
    }
};

describe("binaryTreeAddition", () => {
    describe("Node", () => {
        describe("instantiates", () => {
            test("instantiates without erroring out", () => {
                const result = new Node();
                expect(result instanceof Node).toBeTruthy();
            });

            test("instantiates with null as the default value", () => {
                const node = new Node();
                const result = node.value;
                expect(result).toBeNull();
            });

            test("instantiates with null as the default left and right value", () => {
                const node = new Node();
                const leftResult = node.left;
                const rightResult = node.right;
                expect(leftResult).toBeNull();
                expect(rightResult).toBeNull();
            });

            test("instantiates with a value if one is given as an argument", () => {
                const node = new Node("test");
                const result = node.value;
                expect(result).toBe("test");
            });

            test("instantiates with a left and right value if they are given", () => {
                const left = new Node();
                const right = new Node();
                const node = new Node(undefined, left, right);
                expect(node.left).toEqual(left);
                expect(node.right).toEqual(right);
            });
        });

        describe("addValue()", () => {
            test("adds a value to the Binary Search Tree", () => {
                const rootNode = new Node(5);
                rootNode.addValue(10);
                const result = rootNode.right.value;
                expect(result).toBe(10);
            });

            test("adds a value to the current Node if its value is null", () => {
                const node = new Node();
                node.addValue(10);
                const result = node.value;
                expect(result).toBe(10);
            });

            test("should add a larger number of integers to the Binary Search Tree", () => {
                const rootNode = utils.createBinarySearchTree(
                    utils.smallNumberArray
                );
                const result = rootNode.right.right.value;
                expect(result).toBe(10);
            });
        });
    });

    describe("findSumInBinaryTree()", () => {
        test("returns an empty array if the first argument is not a Node", () => {
            const result = findSumInBinaryTree("test", 10);
            expect(result).toEqual([]);
        });

        test("returns an empty array if the second argument is not a number", () => {
            const result = findSumInBinaryTree(new Node(), "test");
            expect(result).toEqual([]);
        });

        test("returns the two Nodes that add up to a number in a tiny Binary Search Tree", () => {
            const rootNode = new Node(5);
            rootNode.addValue(10);
            rootNode.addValue(7);
            rootNode.addValue(1);
            const result = findSumInBinaryTree(rootNode, 15);
            expect(result).toEqual([rootNode, rootNode.right]);
        });

        test("returns the two Nodes that add up to a number in a medium Binary Search Tree", () => {
            const rootNode = utils.createBinarySearchTree(
                utils.smallNumberArray
            );
            const result = findSumInBinaryTree(rootNode, 19);
            expect(result).toEqual([
                rootNode.right.right,
                rootNode.right.right.left
            ]);
        });
    });
});
