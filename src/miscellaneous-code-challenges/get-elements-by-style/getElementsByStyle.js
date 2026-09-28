/*

*/

/**
 * @param {Element} element
 * @param {string} property
 * @param {string} value
 * @return {Array<Element>}
 */
function getElementsByStyle(node, styleName, styleValue, isInitialNode = true) {
    let matches = [];

    if (node.nodeType === 1 && !isInitialNode) {
        if (node.style[styleName] === styleValue) {
            matches.push(node);
        }
    }

    let child = node.firstChild;
    while (child) {
        matches = matches.concat(
            getElementsByStyle(child, styleName, styleValue, false),
        );
        child = child.nextSibling;
    }

    return matches;
}

module.exports = {
    getElementsByStyle,
};
