const getCheapestItinerary = require("./connectingFlights.js");

const largeFlightList = [
    ["JFK", "ATL", 150],
    ["NYC", "JFK", 200],
    ["JFK", "NYC", 150],
    ["ATL", "NYC", 400],
    ["ATL", "ORD", 230],
    ["ORD", "NYC", 100],
    ["JFK", "ORD", 500],
    ["SFO", "JFK", 130],
    ["SFO", "SEA", 25],
    ["SEA", "JFK", 100],
];

const smallFlightList = [
    ["JFK", "ATL", 150],
    ["NYC", "JFK", 200],
    ["JFK", "NYC", 150],
    ["ATL", "NYC", 400],
    ["ATL", "ORD", 230],
    ["ORD", "NYC", 100],
];

describe("getCheapestItinerary", () => {
    test("throws new TypeError if the first argument is not an array", () => {
        const result = () => getCheapestItinerary("test", "test", "test");
        expect(result).toThrow(
            TypeError(
                "The first argument of getCheapestItinerary must be an array"
            )
        );
    });

    test("throws new TypeError if the second argument is not an array", () => {
        const result = () => getCheapestItinerary([], {}, "test");
        expect(result).toThrow(
            TypeError(
                "The second argument of getCheapestItinerary must be of type string"
            )
        );
    });

    test("throws new TypeError if the third argument is not an array", () => {
        const result = () => getCheapestItinerary([], "test", {});
        expect(result).toThrow(
            TypeError(
                "The third argument of getCheapestItinerary must be of type string"
            )
        );
    });

    test("returns an empty array if the first argument is an empty array", () => {
        const result = getCheapestItinerary([], "test", "test");
        expect(result).toEqual([]);
    });

    test("returns an empty array if there's no connecting flights from starting city", () => {
        const result = getCheapestItinerary(smallFlightList, "TEST", "NYC");
        expect(result).toEqual([]);
    });

    test("returns the correct cheapest itinerary for a small list", () => {
        const result = getCheapestItinerary(smallFlightList, "JFK", "NYC");
        expect(result).toEqual(["JFK -> ATL -> ORD -> NYC", 480]);
    });

    test("returns the correct cheapest itinerary for a large list", () => {
        const result = getCheapestItinerary(largeFlightList, "SFO", "NYC");
        expect(result).toEqual(["SFO -> SEA -> JFK -> NYC", 275]);
    });
});
