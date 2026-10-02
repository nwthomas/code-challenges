import { describe, expect, it } from "vitest";

import { Node } from "./nextBiggerElementNode.ts";

describe("Node", () => {
    it("initializes an empty tree and rejects missing values", () => {
        const root = new Node();
        expect(root.addValue()).toBe(false);
        expect(root.addValue(10)).toBe(true);
        expect(root.value).toBe(10);
    });

    it("inserts values with parent pointers", () => {
        const root = new Node(10);
        for (const value of [5, 30, 22, 35]) {
            expect(root.addValue(value)).toBe(true);
        }
        expect(root.left?.value).toBe(5);
        expect(root.left?.parent).toBe(root);
        expect(root.right?.parent).toBe(root);
        expect(root.right?.left?.value).toBe(22);
        expect(root.right?.left?.parent).toBe(root.right);
        expect(root.right?.right?.value).toBe(35);
        expect(root.right?.right?.parent).toBe(root.right);
        expect(root.findNextBigger(root.right!.left)).toBe(root.right);
    });

    it("finds the leftmost successor in the right subtree", () => {
        const root = new Node(10);
        for (const value of [30, 22, 15]) {
            root.addValue(value);
        }
        expect(root.findNextBigger(root)).toBe(root.right!.left!.left);
    });

    it("climbs past smaller ancestors to find the successor", () => {
        const root = new Node(30);
        for (const value of [10, 22, 25]) {
            root.addValue(value);
        }
        expect(root.findNextBigger(root.left!.right!.right)).toBe(root);
    });

    it("returns an empty object when there is no successor", () => {
        const root = new Node(10);
        root.addValue(30);
        expect(root.findNextBigger()).toEqual({});
        expect(root.findNextBigger(new Node())).toEqual({});
        expect(root.findNextBigger(root.right)).toEqual({});
        expect(root.findNextBigger(new Node(1))).toEqual({});
    });

    it("keeps duplicate values in inorder sequence", () => {
        const root = new Node(10);
        root.addValue(10);
        expect(root.findNextBigger(root)).toBe(root.right);
        expect(root.findNextBigger(root.right)).toEqual({});
    });
});
