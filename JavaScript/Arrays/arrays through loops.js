// arrays through loops

//Arrays by using for loop

let a = [2, 3, 4, 5, 6, 15, 5];
console.log("array by using for loop");
for (let i = 0; i < a.length; i++) {
    console.log(a[i]);
}

//arrays by using foreach loop
console.log("for-each loop ");

a.forEach((value, index, arr) => {
    //console.log(value);  displays values of the array
    // console.log(index);  //displays index fo the arrays
    console.log(value, index, arr); // displays value index and array
});

//for-in loop
console.log("for in loop");

let obj = {
    a: 2,
    b: 3,
    c: 4
}
for (const key in obj) {
    if (Object.hasOwnProperty.call(obj, key)) {
        const element = obj[key];
        console.log(key, element);

    }
}

//for-of loop
console.log("for of loop");
for (const iterator of a) {
    console.log(iterator);

}

//map-filter-reduce functions

//map

//creating an empty array and pushing the elements through for loop
let arr2 = [2, 3, 4, 5, 6, 7]

// let newarr=[];
// for (let i = 0; i < arr2.length; i++) {
//     const element = arr2[i];
//     newarr.push(element**2) 
// }
// console.log(newarr);

// by using map function

console.log("map function")
let newarr = arr2.map((e) => {
    return e ** 2;
})
console.log(newarr)

//filter function
console.log("filter funciton");
let newarr3 = [43, 2, 21, 1, 3, 4, 5];
console.log(newarr3);
console.log("greter than Ten");

const greaterThanTen = (e) => {
    if (e > 10) {
        return true;
    }
    else {
        return false;
    }
}

console.log(newarr3.filter(greaterThanTen));


// reduce method
let arr3 = [1, 2, 3, 4, 5, 6]

const red = (a, b) => {
    return a * b
}
console.log("reduce function ", arr3.reduce(red));


//array from

console.log("array-from function");

Array.from("manju")//create an array from the given element;