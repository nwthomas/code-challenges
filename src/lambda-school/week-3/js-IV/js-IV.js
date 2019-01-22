/*

Wow, I really messed this up! My implementation of these attributes and prototypes isn't working the way I want it to. Can you help me to debug my code, please? Thanks!

*/

function Parent(attributes) {
  this.gender = attributes.gender;
  this.age = attributes.age;
  this.name = attributes.name;
  this.homeTown = attributes.homeTown;
}

Parent.prototype.yabbaDabba = function() {
  console.log("Yabba dabba doo!");
};

Parent.prototype.speak = function() {
  return `Hello, my name is ${this.name}`;
};

const fred = new Parent({
  gender: "Male",
  age: 35,
  name: "Fred",
  homeTown: "Bedrock"
});

const wilma = new Parent({
  gender: "Female",
  age: 37,
  name: "Wilma",
  homeTown: "Bedrock"
});

console.log("***** Parents *****");
console.log("1.", fred);
console.log("2.", fred.speak());
console.log("3.", wilma);
console.log("4.", wilma.speak());

function Child(childAttributes) {
  Parent.call(this, childAttributes);
  this.isChild = childAttributes.isChild;
}

Child.prototype = Object.create(Parent.prototype);

Child.prototype.checkIfChild = function() {
  if (this instanceof Parent) {
    return `My name is ${this.name}.\nAm I a Child?  ${pebbles instanceof
      Child}.\nAm I a Parent? ${pebbles instanceof Parent}.`;
  }
};

const pebbles = new Child({
  gender: "Female",
  age: 3,
  name: "Pebbles",
  homeTown: "Bedrock"
});

console.log("***** Child *****");
console.log("5.", pebbles);
console.log("6.", pebbles.speak());
console.log("7.", pebbles.checkIfChild());
console.log("8.", pebbles.yabbaDabba());
