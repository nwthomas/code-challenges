/*

Give an object with a variable amount of keys and values (of any sort of data), write a custom copy function capable of deep-copying an object.

*/

function copy<T extends object>(obj: T): T {
    const final = {} as T;
    for (let key in obj) {
        if (typeof obj[key] === "object") {
            final[key] = copy(obj[key] as object) as T[Extract<
                keyof T,
                string
            >];
        } else {
            final[key] = obj[key];
        }
    }
    return final;
}

export default copy;
