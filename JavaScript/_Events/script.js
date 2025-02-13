console.log("js is running")

let button=document.getElementById("btn") //whenever the button with id btn is clicked then certain actions are performed  -- here button is a variable name that the id of button(btn) is stored in button(variable)

let button2=document.getElementById("btn2")

// Syntax:
// ELement/variable-Name.addEventListener("event-name",()=>{
//     set of instructions to be performed
// })

button.addEventListener("click",()=>{
    alert("Button is clicked")
    document.querySelector(".box1").innerHTML="<b>Hey the button was clicked</b>"
    document.querySelector(".box1").style.color="red" 
})
button2.addEventListener("click",()=>{
    document.querySelector(".box2").style.backgroundColor="green"
})
button2.addEventListener("contextmenu",()=>{
    alert("Hi you rightclicked")
})

button2.addEventListener("dblclick",()=>{
    document.querySelector(".box2").style.color="yellow"
})

// like this we can perform many funcitons or events like:
// single click
// double click
// mouse events 
// keyboard events