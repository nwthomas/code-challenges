/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their destination B. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.
*/

function getCheapestItinerary(flightArr, start, end) {
    if (!Array.isArray(flightArr)) {
        throw new TypeError(
            "The first argument of getCheapestItinerary must be an array"
        );
    }
    if (typeof start !== "string") {
        throw new TypeError(
            "The second argument of getCheapestItinerary must be of type string"
        );
    }
    if (typeof end !== "string") {
        throw new TypeError(
            "The third argument of getCheapestItinerary must be of type string"
        );
    }
    if (!flightArr.length) {
        return [];
    }

    const flightsData = flightArr.reduce((flights, newFlight) => {
        const [newFlightStart, newFlightEnd, newFlightCost] = newFlight;

        if (flights[newFlightStart]) {
            flights[newFlightStart][newFlightEnd] = newFlightCost;
        } else {
            flights[newFlightStart] = { [newFlightEnd]: newFlightCost };
        }

        return flights;
    }, {});

    if (!flightsData[start]) {
        return [];
    }

    const flightsTracker = Object.entries(flightsData[start]).reduce(
        (flights, newFlight) => {
            return [
                ...flights,
                { flights: [start, newFlight[0]], cost: newFlight[1] },
            ];
        },
        []
    );

    if (!flightsTracker.length) {
        return [];
    }

    const finishedFlights = [];

    while (flightsTracker.length) {
        const { flights, cost } = flightsTracker.pop();
        const nextFlightStart = flights[flights.length - 1];
        const nextFlightsList = flightsData[nextFlightStart];

        if (nextFlightsList) {
            const nextFlightsListArray = Object.entries(nextFlightsList);

            nextFlightsListArray.forEach((nextFlight) => {
                const [nextFlightCity, nextFlightCost] = nextFlight;
                const newFlightObject = {
                    flights: [...flights, nextFlightCity],
                    cost: cost + nextFlightCost,
                };

                if (nextFlightCity === end) {
                    finishedFlights.push(newFlightObject);
                } else if (!flights.includes(nextFlightCity)) {
                    flightsTracker.push(newFlightObject);
                }
            });
        }
    }

    const finalChoice = finishedFlights.reduce((final, accum) => {
        if (Object.keys(final).length) {
            return final.cost > accum.cost ? accum : final;
        } else {
            return accum;
        }
    }, {});

    const finalChoiceStringWithPrice = [
        finalChoice.flights.join(" -> "),
        finalChoice.cost,
    ];

    return finalChoiceStringWithPrice;
}

module.exports = getCheapestItinerary;
