console.log("Js is running");

let boxes = document.querySelector(".container").children
// console.log(box)


// formula: a+ Math.random()*0
            // if generated random number is 1 then a value returned else 0 value is returned
// To generate a random number to select the color betwen the rgb value(0,255)


function getRandomColor() {
    let r = Math.ceil(0 + Math.random()* 255);  //generates a value b/w 0-255
    let g = Math.ceil(0 + Math.random()* 255);  //generates a value b/w 0-255
    let b = Math.ceil(0 + Math.random()* 255);  //generates a value b/w 0-255
    return `rgb(${r},${g},${b})` //combines 3 values and generate a rgb(r,g,b) value
}
console.log(getRandomColor()) 

Array.from(boxes).forEach(e => {
    e.style.backgroundColor = getRandomColor() //function-call() to generate a  rgb value
   e.style.color  = getRandomColor()
})