console.log('Testing js');

async function sleep() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(47)
            // console.log('hi');
        }, 2000);
    });
}

// sleep()
// sleep()


/* IIEF function....

(async function main() {
    let a = await sleep();
    console.log(a);
    let b = await sleep();
    console.log(b);
})()*/


// Destructuring
// Destructuring in arrays 


let [x, y, z] = [10, 20, 150]
console.log(x, y, z)

let [p, q, ...manju] = [100, 200, 300, 400, 500, 650, 550, 250] // p= 100 ,q= 200 and the rest of the elements are  assigned to the ...variable
console.log(p, q);
console.log(...manju);


// Destructuring in objects

let obj = {
    a: 1,
    b: 2,
    c: 3
}
let { a, b } = obj
console.log(obj);
console.log(a, b);  // returns 1,2
// console.log(c); // returns an error bcoz c is not destructed to the obj



// spread operator
const arr = [1, 2, 3, 4]
console.log(arr[0] + arr[1] + arr[2] + arr[3])
// console.log(sum(arr[0], arr[1], arr[2], arr[3]))
console.log(sum(...arr)) //   ...arr    this is the spread operator that retrives all the elements from the arr



// Local ,Global , Block level scopes  

// The variables that are declared withtin a function or a block that have block or local scope

// 1.Block scope: provides the block level scope which means if a variable declared inside a block or a fuction that variable cannot be accessed from the outside of the fucntion /block

// 2.local scope: this is also same as the block scope provides the block level scope which means if a variable declared inside a block or a fuction that variable cannot be accessed from the outside of the fucntion /block


// 3.global scope: Gobal variables are the variables that are declared outside of the function / block that can be accesed by throughout of the function 


// Hoisting:

//Hoisting is nothing but the varibles/functions/anything that are declared with the var keyword that are moved to the top of the function/ block  topof the code before execution ...


function sum() {
    
    console.log(a) //here we are accesing the value of the a before intializing it prints undefined

    c = a + b + d

    var a = 55  //when we declare a here the compiler will throw /move the variable to top of the code /function.. only the variable but not the value therefore it returns the value undefined

    let b = 12 //when we use let it directly throws error 

    const d = 78   //when we use const it directly throws error 
} 