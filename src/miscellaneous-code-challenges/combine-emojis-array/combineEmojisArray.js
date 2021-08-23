/*
Write a function called mergeLists that takes in two sorted lists of the following data structure
and combines them up to the hard limit passed in as the third argument.

EXAMPLE
const paulius = [
    { t: 1, emoji: 'smiley' }, 
    { t: 1, emoji: 'lovingIt' }, 
    { t: 3, emoji: 'laugh' }
]
const helen = [
    { t: 2, emoji: 'wow' }, 
    { t: 3, emoji: 'laugh' }, 
    { t: 10, emoji: 'wow' }
]

---> input
mergeLists(paulius, helen, 5)

---> output
[
    { t: 1, emoji: 'smiley' },
    { t: 1, emoji: 'lovingIt' },
    { t: 2, emoji: 'wow' }, 
    { t: 3, emoji: 'laugh' },
    { t: 3, emoji: 'laugh' },
]
*/

function mergeLists(list1, list2, limit) {
    const finalEmojisArray = [];
    let list1Index = 0;
    let list2Index = 0;

    while (
        finalEmojisArray.length < limit &&
        (list1Index < list1.length || list2Index < list2.length)
    ) {
        const list1Item = list1[list1Index];
        const list2Item = list2[list2Index];

        if (list1Item && list2Item && list1Item.t < list2Item.t) {
            finalEmojisArray.push(list1Item);
            list1Index++;
        } else if (list1Item && list2Item && list1Item.t >= list2Item.t) {
            finalEmojisArray.push(list2Item);
            list2Index++;
        } else if (list1Item) {
            finalEmojisArray.push(list1Item);
            list1Index++;
        } else {
            finalEmojisArray.push(list2Item);
            list2Index++;
        }
    }

    return finalEmojisArray;
}

module.exports = mergeLists;
