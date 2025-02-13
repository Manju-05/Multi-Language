console.log("Hey Welocme to the variables , datatypes & Objects concept");
console.log(" variables");

// Addition of two numbers using Variables

var a = 10; // declared as var as a global scope
let b = 30;
let c = 10;
let d = "manju"
var _name = "manjunath"
var y = undefined;
let z = null;    //type of null is object

console.log(a + b + c); //  O/P in console
console.log(a, b, c, d, _name);
console.log(typeof a, typeof b, typeof c, typeof d, typeof _nam, typeof y, typeof z);
console.log(y)
console.log(z)

const x_1 = 100;//This is a constant value we cant change the value
//x = x+1; //poduces an error  bcoz it is an constant value


{
    let a = 47;  // declared as let as a local scope
    console.log(a); // here eventhough a is assigned as 10 in upside it will consider only the a within the block
}


//Data Types
console.log("Data Types");
console.log(typeof a, typeof b, typeof c, typeof d, typeof _nam, typeof y, typeof z);

//Objects
console.log("Objects")

let x = {
    "name": "manju",
    "college": "svr",
    "course": "diploma",
    "year": "4"
}
console.log(x);

x.bus_no ="2"; //adding another value to the x object
console.log(x);






