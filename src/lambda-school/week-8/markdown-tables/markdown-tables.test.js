const markdownTables = require("./markdown-tables");

const data1 = [
  "name,email",
  "emily,emily@email.com",
  "mary,maryberry@gbbs.co.uk"
];

const data2 = ["number", "1", "2", "3", "4", "5", "6"];

test("Takes in an array of data and converts it into syntax for a markdown table", () => {
  expect(markdownTables(data1)).toBe(`|name|email|
|----|-----|
|emily|emily@email.com|
|mary|maryberry@gbbs.co.uk|`);
  expect(markdownTables(data2)).toBe(`|number|
|------|
|1|
|2|
|3|
|4|
|5|
|6|`);
});
