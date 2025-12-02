const { goodNodes, TreeNode } = require("./countGoodNodesInBinaryTree");

describe("goodNodes", () => {
    it("returns the number of good nodes in the binary tree", () => {
        const root = new TreeNode(3);
        root.left = new TreeNode(1);
        root.right = new TreeNode(4);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(1);
        root.right.right = new TreeNode(5);
        expect(goodNodes(root)).toBe(4);
    });

    it("returns the number of good nodes in the binary tree with a single node", () => {
        const root = new TreeNode(1);
        expect(goodNodes(root)).toBe(1);
    });

    it("returns 0 if the binary tree is empty", () => {
        const root = null;
        expect(goodNodes(root)).toBe(0);
    });

    it("returns 1 for just the root if all child nodes are bad", () => {
        const root = new TreeNode(10);
        root.left = new TreeNode(4);
        root.right = new TreeNode(2);
        expect(goodNodes(root)).toBe(1);
    });
});
