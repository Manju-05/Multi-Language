console.log("welocme to tutorial of Arrays");

// ARRAYS:
// Arrays are the variables which can hold more than one value.
//Arrays are mutable whereas strings are immutable.

let fruits = ["mango", "apple", "banana", "kiwi", "pomegranate"]; //of same datatype
console.log(fruits);
console.log("array=", fruits);


//the datatype of arrays are object
console.log("data type of arrays= ", typeof (fruits));


let cars = ["toyata", "mauruti", "vks", "benz", "breeza", 1, 32, 99];
console.log("cars=", cars)
console.log(cars[0]);
console.log(cars[2]);
console.log(cars[3]);
console.log(cars[4]);
console.log(cars[5]);
console.log(cars[6]);

//finding the length of array

console.log("length of the Array = ", cars.length);
cars[2] = "suzuki";

console.log("Array is mutable");
console.log(cars[2]);

//Arrays methods

let x = ["ss", "ntr", "tarak", "aa"];

console.log(x.toString()); //converts the array into string

console.log(x.join(" & "));//joins in the middle of the elements

console.log(x.pop());//delete's and returns the element at  the end of the array

console.log(x.push(100, 1, 29, 4, 43, 546, 2345, 23, 432, 12, 3, 1,));//pushes the elemenst into the array
console.log(x.push("cv"));//pushes at the element end of the array
console.log("After pushing into the array = ", x);

console.log(x.shift());//delete's & returns the first element of the array

console.log(x.unshift("box")); //pushes the element at the beggining and the returns the size of the array
console.log(x);

delete x[1]; //delete operator
console.log("after deleting ", x);
console.log(x.length);

//concatinating of arrays

let x1 = [1, 2, 3]
let x2 = [4, 5, 6]
let x3 = [7, 8, 9]

console.log(x1.concat(x2, x3)); //combines the three arrays into a single array

//sorting arranging the elements in an order
let z = [354, 23543, 5, 2, 34, 54, 65, 234, 2, 3432]
console.log("ater sorting ", z.sort());

//splice method :used to add the elements in the array.

let numbers = [1, 2, 3, 4, 5, 6]
numbers.splice(1, 3)//only deleting 
console.log(numbers)
numbers.splice(1, 3, 44, 55, 66) // deletng and adding ---> 1 is the starting number and from thrn it has to delete 3 elements ad 44 55 66 are the elements to be added in the array
console.log("numbers after splicing =", numbers)


//slice method : used to create a new array from the already existing array.

bikes = ["tvs", "bajaj", "ns", "jupiter", "zx"]
console.log(bikes.slice(1, 4)); // 4'th element is not countable
console.log(bikes.slice(0));
console.log(bikes.slice(3));

//reverse method

let m = ["rahul", "ankush", "ankith"]
console.log("reversed arrya", m.reverse());















