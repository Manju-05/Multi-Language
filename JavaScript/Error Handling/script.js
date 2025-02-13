let a = prompt("enter first  number")

let b = prompt("enter second  number")

// let sum= a + b   if we write like this then it will concatinate/append but doesnot add
// If the user enter the value in the form of text then it returns NaN  
//So whnever u want to throw the error explicitly when the user enters text then we have to use the throw keyword and throw the error


if(isNaN(a) || isNaN(b)){
    throw SyntaxError("please enter the valid numbers")
}
let sum=parseInt(a)+parseInt(b)
// console.log('The sum is ',sum);

//whenever u want to handle the error then u have to use the try catch block 
//here x is not defined therfore it throws error..
// try catch is a block that is used to wrte the ambigous code i.e that it might generate error then that lines of code is written in the try block..if the code dosenot genrate the error then it skips the catch block..
//when the code in the try block genreates the error then the control goes to the catch block catch block provides some eror message and handles the error..


let x=2
function main(){
    try {
        console.log('The sum is ',sum*x);
        return true
} catch (error) {

    // console.log("Hello user x is not defined....! please define the value of X")

    console.log(error.name,error.mesage,error.stack);//printing the values of error object 
    return false
}
finally{
    console.log('The program is ended..!');
}
}
main()


//finally is the code clause that is used whenvever a set of code should execute compulsory if errors are occur or errors are not occur..
//In some cases there will be a situation like we uses the function and in the fuction it returns some values NOTE: the code after the return statement doesnot execute after it returnoing some value.In this case we use the finally block to display something compulsory



