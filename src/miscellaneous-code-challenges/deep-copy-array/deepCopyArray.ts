type NestedArray<T> = (T | NestedArray<T>)[];

/*

Give an array with a variable amount of indexes and nested arrays inside it (of any sort of data), write a custom copy function capable of deep-copying an array.

*/

function copy<T>(arr: NestedArray<T>): NestedArray<T> {
    const final: NestedArray<T> = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            final[i] = copy(arr[i] as NestedArray<T>);
        } else {
            final[i] = arr[i];
        }
    }
    return final;
}

export default copy;
