import {
    TreeNode,
    deserialize,
    serialize,
} from "./serializeAndDeserializeBinaryTree.ts";
import { describe, expect, it } from "bun:test";

function buildTree(values: (number | null)[]): TreeNode | null {
    if (values.length === 0 || values[0] === null) {
        return null;
    }

    const root = new TreeNode(values[0]);
    const queue: TreeNode[] = [root];
    let head = 0;
    let i = 1;

    while (head < queue.length && i < values.length) {
        const node = queue[head++];

        if (i < values.length && values[i] !== null) {
            node.left = new TreeNode(values[i]!);
            queue.push(node.left);
        }
        i++;

        if (i < values.length && values[i] !== null) {
            node.right = new TreeNode(values[i]!);
            queue.push(node.right);
        }
        i++;
    }

    return root;
}

describe("Serialize and Deserialize Binary Tree", () => {
    describe(serialize.name, () => {
        it("handles an empty tree", () => {
            expect(serialize(null)).toEqual('{"val":null}');
        });

        it("handles a full tree", () => {
            const tree = buildTree([1, 2, 3, null, null, 4, 5]);
            expect(serialize(tree)).toEqual(
                '{"val":1,"left":{"val":2,"left":null,"right":null},"right":{"val":3,"left":{"val":4,"left":null,"right":null},"right":{"val":5,"left":null,"right":null}}}',
            );
        });
    });

    describe(deserialize.name, () => {
        it("handles an empty tree", () => {
            expect(deserialize('{"val":null}')).toEqual(null);
        });

        it("handles a valid tree", () => {
            expect(
                deserialize(
                    '{"val":1,"left":{"val":2,"left":null,"right":null},"right":{"val":3,"left":{"val":4,"left":null,"right":null},"right":{"val":5,"left":null,"right":null}}}',
                ),
            ).toEqual(buildTree([1, 2, 3, null, null, 4, 5]));
        });
    });
});
