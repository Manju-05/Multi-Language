alert("Welcome to the Js Introduction"); //This is the alert message
console.log("Hey I am console")  //This mesages wil be diplayed on console on the webpage
console.log("code is running")

var a = prompt("HI Welocme to the Intro of Js-- Enter any Number");   //This is the example of Variable declaration    -- The enterd number will bwe stord in a variable

console.log("enterd number is "+ a);  // the enterd number will be dipslayed on the console

var b = confirm("are u sure u want to blast")  //This is the confirm message that when u click OK then true block will be executed else false block will be executed
if(b){
    console.log("We r going to Blast");
}
else{
    console.log("Oops We r not going to blast");
}

console.warn("hey this is a warning message");//this is a warning message that displays in the console
console.error("this is the error message");//this is used for error message
console.info("hi welocome to web devolepment course") //used to display any message on the console same as console.log