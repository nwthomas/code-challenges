const { diameterOfBinaryTree, TreeNode } = require('./binaryTreeDiameter');

describe('diameterOfBinaryTree', () => {
    it('should return the diameter of the binary tree through the root', () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.left.right = new TreeNode(5);
        expect(diameterOfBinaryTree(root)).toBe(4);
    });

    it('should return the diameter of the binary tree not through the root', () => {
        const root = new TreeNode(100);
        root.left = new TreeNode(20);
        root.left.left = new TreeNode(10);
        root.left.left.left = new TreeNode(9);
        root.left.right = new TreeNode(21);
        root.left.right.right = new TreeNode(22);
        root.left.right.right.right = new TreeNode(30);
        expect(diameterOfBinaryTree(root)).toBe(5);
    });

    it('should return the diameter of the binary tree with a single node', () => {
        const root = new TreeNode(1);
        expect(diameterOfBinaryTree(root)).toBe(0);
    });
});