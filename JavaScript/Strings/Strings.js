console.log("hey this is strings tutorial");
let user = "manju"
console.log(user);
console.log(user[0]);
console.log(user[1]);
console.log(user[2]);
console.log(user[3]);
console.log(user[4]);
console.log(user[5]);

//Finding the length of striing
console.log("length of the string =" + user.length);
let name_1 = "manjunath"
console.log("length of the string =" + name_1.length);

//concatinating of strings by using "+"

let user_1 = "ramu"
let friend = "hanu"
console.log("his name is " + user_1 + " his friend name is " + friend);

//concatinating the strings using --> (``)  backTick

console.log(`His name is ${user_1} and his friend name is ${friend}`);

// like this we can add the double qoutes in the middle of the sentence 
let sentence = `hey welcome to the "js" tutorial`;
console.log(sentence);


//string functions

console.log("String funcitons")
let x = "sample";
let user_47 = "user_5";
console.log(x.toUpperCase());
console.log(x.toLowerCase());
console.log(x.concat(user_47));
console.log(x.indexOf("e"));
console.log(x.charAt(4));
console.log(x.length);
console.log(x.endsWith("le"));
console.log(x.endsWith("nth"));
console.log(x.startsWith("sa"));
console.log(x.startsWith("ma"));
console.log(x.replace("sam", "ap"));
console.log(x.slice(1, 4));
console.log(x.slice(3));
console.log("manju\"".length + " the \  new line character will also counts")
console.log(x.includes("sam"))

