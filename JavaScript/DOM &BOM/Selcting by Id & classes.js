console.log("Hey helloo")


document.getElementById("box").style.backgroundColor = "red";  
//giving color through id


let x = document.getElementsByClassName("boxes")
//all the nodes are stored into a variable  by using class name and giving colors.

//here we cant give the color directly like the id by giving the style 

x[2].style.backgroundColor = "yellow";


document.querySelector(".boxes").style.backgroundColor = "pink"  //it only selects the "first class" and apply the css

document.querySelectorAll(".boxes").forEach((e) => {
    e.style.backgroundColor = "green";  
    //Here we cannot directly apply the css to the html elements but to apply the style to all the elements then we have to use the for each loop/any other loops
});



console.log(document.getElementsByTagName("body"))//by tag name

e[1].matches("#box1")  //if it doesnot matches the  the css id it retrurs false
false

e[1].matches("#box")//if it  matches ths css the id it retruns true
true

e[3].matches("#box")  //anther ex..
false


e[3].closest("#box")  //it inintallyy  checks it self for the given tag if it prsent it returns or it check in thr next parent tag and next parents tags like that it continues search upto the n elements

null


e[3].closest(".boxes")
/* <div class=​"boxes" style=​"background-color:​ green;​">​Box 4​</div>​ */

e[3].closest("html")
/* <html lang=​"en">
 <head>​…​</head>
 <body>​…​</body>
 </html>​ .*/

let e = document.getElementsByClassName("boxes")
undefined

document.querySelector(".container").contains(e[0])
true  //if it contians the spcified element then it returns true


document.querySelector(".container").contains(e[4])
true
