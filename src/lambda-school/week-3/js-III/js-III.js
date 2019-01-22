/*

Good morning! You have an array full of objects detailing information about pets: name, species and age. Let's write a function which iterates through each object, looks for all the pets of a particular species, converts each of those pets' ages into human years, then reduces the converted pets' ages into one sum.

INPUT three parameters
an array: arr,
a string: kind,
a number: multiply

Write a function that uses the JavaScript Array methods: .filter(), .map() and .reduce().

OUTPUT:
console.log(sumPetYears(pets, 'dog', 7)); // The combined dogs' ages: 154
console.log(sumPetYears(pets, 'cat', 4)); // The combined cats' ages: 132
console.log(sumPetYears(pets, 'parakeet', 5)); // The combined parakeets' ages: 65

Do not modify the original "pets" array. Write your function so that the "pets" array is not mutated as a result of invoking your function. To verify the input array is not mutated, you can console.log it after your function:

console.log(pets); // ---> remains the same? Yes!

*/

function sumPetYears(arr, kind, multiply) {
  const filterMapReduce = arr
    .filter(animal => animal.species === kind.toLowerCase())
    .map(animal => animal.age * multiply)
    .reduce((total, accumulator) => {
      return (total += accumulator);
    }, 0);
  return `The combined ${kind.toLowerCase()}s' ages: ${filterMapReduce}`;
}

module.exports = sumPetYears;
