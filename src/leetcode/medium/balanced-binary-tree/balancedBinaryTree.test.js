const { isBalanced, TreeNode } = require("./balancedBinaryTree");

describe("isBalanced", () => {
    it("should return true if the tree is balanced", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        expect(isBalanced(root)).toBe(true);
    });

    it("should return false if the tree is not balanced", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.left.left = new TreeNode(5);
        expect(isBalanced(root)).toBe(false);
    });

    it("should return true if the tree is empty", () => {
        const root = null;
        expect(isBalanced(root)).toBe(true);
    });
});
