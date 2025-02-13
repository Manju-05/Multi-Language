// console.log("hey user welcome to the JS")
// console.log("hey user welcome to the functions")
// console.log("hey user Example code of functions")


// these are the sentences that are used for other many users if u want to change the  of user then u have to rewrite all the sentences.
//therefore functions are introduced

//funcitons are mainly used for code reusablity

// syntax : 
//  function name(params) {

//                  }


function name(user) {
    console.log("hey " + user + " welcome to the JS")
    console.log("hey " + user + " welcome to the functions")
    console.log("hey " + user + " Exmaple of functions")
}
name("manju") //funciton call
             //without this the function won't execute

//Addition of two numbers usimg functions

function sum(a,b) {
    console.log(a+b);   
}
sum(2,3)
//---> Another function
function addition(a,b,c=20)  { //here c=20 is the default parameter whwn the user dosent give value of c then defalult value is passed
    console.log("numbers to be add" , a,b,c)
    return a+b+c
}
    result1=addition(10,20);//function call
    result2=addition(10);//function call
    result3=addition(10,20,40);//function call we can also intilize the value of "c"
    console.log("sum of result 1 is : ",result1 )
    console.log("sum of result 2 is : ",result2 )
    console.log("sum of result 3 is : ",result3 )

//Arrow function
console.log("hey iam a arrow function");

const fun1 = (x)=>{
    console.log("I am arrow function",x)

}
fun1(90);
    

    

