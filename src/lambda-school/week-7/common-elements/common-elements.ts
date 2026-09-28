/*

Good morning! Write a function called commonElements that has parameters for two arrays.  Return an array of all items that are present in both arrays.  Do not modify the arrays that are passed in.

## Input Example:  
[1, 2, 3, 4] [3, 4, 5, 6]
['a', 'b', 'c'] ['x', 'y', 'z', 'a']
[1, 2, 3] [4, 5, 6]

## Input Example:  
[1, 2, 3, 4] [3, 4, 5, 6]
['a', 'b', 'c'] ['x', 'y', 'z', 'a']
[1, 2, 3] [4, 5, 6]

*/

function commonElements<T>(arr1: T[], arr2: T[]): T[] {
    let common: T[] = [];
    arr1.forEach((item1) => {
        arr2.forEach((item2) => {
            if (item1 === item2) return common.push(item1);
        });
    });
    return common;
}

export default commonElements;
