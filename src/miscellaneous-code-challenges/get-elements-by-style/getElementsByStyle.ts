/*
Implement a method getElementsByStyle() that finds DOM elements that are rendered by the browser using the specified style. It is similar to Element.getElementsByClassName() but with some differences:

- It is a pure function that takes an element, a property string, and a value string representing the style property/value pair to match on the element's descendants. For example, getElementsByStyle(document.body, 'font-size', '12px').
- Similar to Element.getElementsByClassName(), only descendants of the element argument are searched, not the element itself.
- Returns an array of Elements instead of an HTMLCollection of Elements.

Do not use document.querySelectorAll(), which would make the problem trivial. You will not be allowed to use it during real interviews.

Examples:

```javascript
const doc = new DOMParser().parseFromString(
  `<div>
    <span style="font-size: 12px">Span</span>
    <p style="font-size: 12px">Paragraph</p>
    <blockquote style="font-size: 14px">Blockquote</blockquote>
  </div>`,
  'text/html',
);

getElementsByStyle(doc.body, 'font-size', '12px'); // [span, p] <-- This is an array of elements.
```
*/

/**
 * @param {Element} element
 * @param {string} property
 * @param {string} value
 * @return {Array<Element>}
 */
function getElementsByStyle(
    startingNode: Element,
    styleName: string,
    styleValue: string,
) {
    function dfs(
        node: globalThis.Node,
        isInitialNode: boolean = true,
    ): Element[] {
        let matches: Element[] = [];

        if (node instanceof HTMLElement && !isInitialNode) {
            if (node.style.getPropertyValue(styleName) === styleValue) {
                matches.push(node);
            }
        }

        let child = node.firstChild;
        while (child) {
            matches = matches.concat(dfs(child, false));
            child = child.nextSibling;
        }

        return matches;
    }

    return dfs(startingNode);
}

export { getElementsByStyle };
