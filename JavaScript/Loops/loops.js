console.log("hey Welocme to the loops concept");

//for loop
let a = 1;

for (let i = 0; i < 10; i++) {
    console.log(a + i);
}

//for-loop 
let i = 0;

for (let i = 0; i < 10; i++) {
    console.log(i);
}

//for in loop --> mainly used for objects
let obj = {
    "name": "manju",
    "course": "diploma",
    "college": "svr"
}

//printing key & element values
for (const key in obj) {
    const element = obj[key];
    console.log(key, element)
}
//printing only keys
for (const key in obj) {
    console.log(key);
}


//for-of loop--used in arrays for iterating the values
for (const i of "manju") {
    console.log(i);
}

let arr=["manju",11,23,32]
console.log("for of array")
for (const i of arr) {
    console.log(i);
}


//while loop
i = 0;
console.log("while loop")
while (i < 10) {
    console.log(i);
    i++;
}

//do-while loop
let j = 0;
console.log(" Do -while loop")

do {
    console.log(j);
    j++;
}
while (j < 5);
