/*
Currying is mostly an interview exercise, but it usefully tests closures, arity, and this forwarding.

Clarification questions
- What value types will curry expect?
- Should the function expect values of different types?

Solution
The closure-based implementation is the recommended version to internalize first. It collects one argument from each call until the total count reaches the original function's arity (func.length), then invokes the original function with the accumulated arguments and current this value.

Two terms are useful here:
- Arity: The number of arguments or operands taken by a function.
- Closure: A closure is the combination of a function bundled together with references to its lexical environment (surrounding state).

A curried function therefore has two phases:
1. If it has enough arguments, call the original function and return its result.
2. Otherwise, return another function that remembers the arguments seen so far and accepts the next one.

That remembered state is what the closure provides. Each partial call produces a new function that still has access to the earlier arguments.

Every public collector is unary. It reads only its first parameter, even if the caller supplies additional arguments. It also checks arguments.length so an empty call can be ignored without mistaking an explicitly passed undefined for an empty call.

The key property is that each partial function owns its own accumulated argument prefix and the receiver from the chain that created it. Reusable partials only work if later calls create a new prefix instead of mutating shared state.

The other subtle part is this. The prompt asks for preserving the receiver from the first call in the chain, even if that call is empty. If the original function depends on this, the curried wrapper has to forward that receiver when eventually calling func, which is why the code uses apply and keeps the inner function aligned with the current call context.

The implementation saves the first call's receiver in the closure. Later collectors use regular functions so they can inspect their own arguments.length while still applying func with that saved receiver.

For obj.mul(3)()(2), the first call stores both 3 and obj as the receiver. The empty call keeps that same receiver, and the final (2) invokes the original function as if it were called with obj and [3, 2].
*/

type Curried<Args extends unknown[], Result> = Args extends [
    infer Arg,
    ...infer Rest,
]
    ? {
          (): Curried<Args, Result>;
          (
              arg: Arg,
              ...ignored: unknown[]
          ): Rest extends [] ? Result : Curried<Rest, Result>;
      }
    : (...args: unknown[]) => Result;

type Collector<Result> = (
    this: unknown,
    arg?: unknown,
) => Result | Collector<Result>;

export default function curry<Args extends unknown[], Result>(
    func: (...args: Args) => Result,
): Curried<Args, Result> {
    function curried(
        previousArgs: unknown[],
        context: unknown,
        hasContext = false,
    ): Collector<Result> {
        return function collector(this: unknown, arg?: unknown) {
            const currentContext = hasContext ? context : this;

            if (func.length === 0) {
                return func.apply(currentContext, [] as unknown as Args);
            }

            if (arguments.length === 0) {
                return curried(previousArgs, currentContext, true);
            }

            const nextArgs = [...previousArgs, arg];
            if (nextArgs.length >= func.length) {
                return func.apply(currentContext, nextArgs as Args);
            }

            return curried(nextArgs, currentContext, true);
        };
    }

    return curried([], undefined) as Curried<Args, Result>;
}
