const sumPetYears = require("./js-III");

const pets = [
  {
    name: "Tinkerbell",
    species: "cat",
    age: 2
  },
  {
    name: "Lucy",
    species: "dog",
    age: 12
  },
  {
    name: "Chloe",
    species: "cat",
    age: 18
  },
  {
    name: "Mojo",
    species: "dog",
    age: 6
  },
  {
    name: "Olivia",
    species: "parakeet",
    age: 4
  },
  {
    name: "Shadow",
    species: "cat",
    age: 8
  },
  {
    name: "Oreo",
    species: "cat",
    age: 5
  },
  {
    name: "Molly",
    species: "dog",
    age: 4
  },
  {
    name: "Freddie Prinze Jr.",
    species: "parakeet",
    age: 9
  }
];

test("Takes in a database of pets, the type of pet searched for, and number of years to multiply, and returns total number", () => {
  expect(sumPetYears(pets, "parakeet", 5)).toBe(
    "The combined parakeets' ages: 65"
  );
  expect(sumPetYears(pets, "dog", 7)).toBe("The combined dogs' ages: 154");
  expect(sumPetYears(pets, "cat", 4)).toBe("The combined cats' ages: 132");
});
