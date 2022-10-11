const Spreadsheet = require("./spreadsheet.js");

describe("Spreadsheet", () => {
    let s;

    beforeEach(() => {
        s = new Spreadsheet();
    });

    test("can write basic values successfully", () => {
        s.put("A1", "1");
        s.put("A2", "2");
        s.put("A3", "3");
        expect(s.cells).toEqual({ A1: "1", A2: "2", A3: "3" });
    });

    test("can write equations successfully", () => {
        s.put("B1", "=A1+A2");
        s.put("B2", "=B1+2");
        s.put("B3", "=B1+B2+5");
        expect(s.cells).toEqual({
            B1: "=A1+A2",
            B2: "=B1+2",
            B3: "=B1+B2+5",
        });
    });

    test("fetches correct value for numbers", () => {
        s.put("A1", "1");
        expect(s.get("A1")).toBe(1);
    });

    test("fetches correct value for equations", () => {
        s.put("A1", "1");
        s.put("A2", "2");
        s.put("B1", "=A1+A2");
        expect(s.get("B1")).toBe(3);
    });

    test("will overwrite cache with updates values", () => {
        s.put("A1", "1");
        s.put("A2", "2");
        s.put("A3", "3");
        s.put("B1", "=A1+A2");
        s.put("B2", "=B1+2");
        s.put("B3", "=B1+B2+5");
        expect(s.get("B3")).toEqual(13);
        s.put("B2", "=4+5+A1");
        expect(s.get("B3")).toBe(18);
    });
});
