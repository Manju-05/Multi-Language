let Username=prompt("enter your username")
document.write(`hello ${Username} Welcome to the Intro`)


let name2;
document.getElementById("btn").onclick =function(){
    name2=document.getElementById("txtbox").value;
    document.getElementById("myh2").textContent=`HELLO  ${name2} WELCOME `
}