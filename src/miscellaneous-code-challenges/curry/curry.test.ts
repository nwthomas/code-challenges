import { describe, expect, test, vi } from "vitest";

import curry from "./curry.ts";

describe("curry", () => {
    test("collects arguments in order, one call at a time", () => {
        const curried = curry((a: string, b: string, c: string) => a + b + c);

        expect(curried("a")("b")("c")).toBe("abc");
    });

    test("invokes the original function only after collecting enough arguments", () => {
        const add = vi.fn((a: number, b: number, c: number) => a + b + c);
        const curried = curry(add);
        const partial = curried(1)(2);

        expect(add).not.toHaveBeenCalled();
        expect(partial(3)).toBe(6);
        expect(add).toHaveBeenCalledExactlyOnceWith(1, 2, 3);
    });

    test("handles a function with one parameter", () => {
        const double = curry((value: number) => value * 2);

        expect(double(4)).toBe(8);
    });

    test("invokes a zero-parameter function on each call, not during setup", () => {
        const original = vi.fn(() => "ready");
        const curried = curry(original);

        expect(original).not.toHaveBeenCalled();
        expect(curried()).toBe("ready");
        expect(curried("ignored")).toBe("ready");
        expect(original.mock.calls).toEqual([[], []]);
    });

    test("ignores empty calls before and between arguments", () => {
        const add = vi.fn((a: number, b: number) => a + b);
        const partial = curry(add)()()(2)()();

        expect(add).not.toHaveBeenCalled();
        expect(partial(3)).toBe(5);
        expect(add).toHaveBeenCalledExactlyOnceWith(2, 3);
    });

    test("counts an explicitly passed undefined as an argument", () => {
        const curried = curry((a: undefined, b: string) => [a, b]);

        expect(curried(undefined)("value")).toEqual([undefined, "value"]);
    });

    test("preserves mixed types and falsy argument values", () => {
        const curried = curry((a: number, b: boolean, c: string, d: null) => [
            a,
            b,
            c,
            d,
        ]);

        expect(curried(0)(false)("")(null)).toEqual([0, false, "", null]);
    });

    test("ignores additional arguments at every stage", () => {
        const original = vi.fn((a: number, b: number, c: number) => a + b + c);
        const curried = curry(original);

        expect(curried(1, 99)(2, 98)(3, 97)).toBe(6);
        expect(original).toHaveBeenCalledExactlyOnceWith(1, 2, 3);
    });

    test("allows partial functions to be reused without sharing later arguments", () => {
        const curried = curry((a: string, b: string, c: string) => a + b + c);
        const first = curried("a");
        const second = first("b");

        expect(second("c")).toBe("abc");
        expect(first("d")("e")).toBe("ade");
        expect(second("f")).toBe("abf");
        expect(curried("x")("y")("z")).toBe("xyz");
    });

    test("returns the original result without copying it", () => {
        const result = { value: 42 };
        const curried = curry((value: typeof result) => value);

        expect(curried(result)).toBe(result);
    });

    test("forwards the first receiver despite later calls on another receiver", () => {
        const receiver = {
            factor: 10,
            multiply: curry(function (
                this: { factor: number },
                a: number,
                b: number,
            ) {
                return this.factor * a * b;
            }),
        };
        const other = { factor: 100, partial: receiver.multiply(2) };

        expect(other.partial(3)).toBe(60);
    });

    test("preserves the receiver when the first call is empty", () => {
        const receiver = {
            factor: 10,
            multiply: curry(function (
                this: { factor: number },
                a: number,
                b: number,
            ) {
                return this.factor * a * b;
            }),
        };
        const other = { factor: 100, partial: receiver.multiply() };

        expect(other.partial(2)()(3)).toBe(60);
    });

    test("keeps receivers independent across calls to the same curried function", () => {
        const add = curry(function (
            this: { base: number },
            a: number,
            b: number,
        ) {
            return this.base + a + b;
        });
        const first = { base: 10, add };
        const second = { base: 100, add };
        const firstPartial = first.add(1);
        const secondPartial = second.add(2);

        expect(firstPartial(3)).toBe(14);
        expect(secondPartial(4)).toBe(106);
        expect(firstPartial(5)).toBe(16);
    });

    test("forwards the receiver to a zero-parameter function", () => {
        const receiver = {
            value: 42,
            read: curry(function (this: { value: number }) {
                return this.value;
            }),
        };

        expect(receiver.read()).toBe(42);
    });

    test.each([null, undefined])(
        "preserves a first receiver of %s even if a later call has a receiver",
        (receiver) => {
            const curried = curry(function (
                this: unknown,
                a: number,
                b: number,
            ) {
                return { receiver: this, sum: a + b };
            });
            const other = { partial: curried.call(receiver, 1) };

            expect(other.partial(2)).toEqual({ receiver, sum: 3 });
        },
    );

    test("propagates errors thrown by the original function", () => {
        const error = new Error("Unable to add");
        const original = vi.fn((_a: number, _b: number) => {
            throw error;
        });
        const partial = curry(original)(1);

        expect(original).not.toHaveBeenCalled();
        expect(() => partial(2)).toThrow(error);
    });
});
