const { isSubtree, TreeNode } = require("./subtreeOfAnotherTree");

describe("isSubtree", () => {
    it("should return true if the subtree is found in the main tree", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        const subRoot = new TreeNode(2);
        subRoot.left = new TreeNode(4);
        subRoot.right = new TreeNode(5);
        expect(isSubtree(root, subRoot)).toBe(true);
    });

    it("should return false if the subtree is not found in the main tree", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        const subRoot = new TreeNode(2);
        subRoot.left = new TreeNode(4);
        subRoot.right = new TreeNode(6);
        expect(isSubtree(root, subRoot)).toBe(false);
    });

    it("should return false if the root tree is present but the subtree is not", () => {
        const root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        expect(isSubtree(root, undefined)).toBe(false);
    });

    it("should return false if the subtree is present but the root tree is not", () => {
        const subRoot = new TreeNode(1);
        subRoot.left = new TreeNode(2);
        subRoot.right = new TreeNode(3);
        expect(isSubtree(undefined, subRoot)).toBe(false);
    });

    it("should return true if both the root and subtree are empty", () => {
        expect(isSubtree(undefined, undefined)).toBe(true);
    });
});
