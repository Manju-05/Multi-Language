// Creating the random names
let rand = Math.random()  //math.random generates a random  number b/w 0-1 
let w1, w2, w3;

//Here it generates any of the rand word

if (rand < 0.33) {
    w1 = "Crazy"
}
else if (rand < 0.66 && rand >= 0.33) {
    w1 = "Amazing"
}
else {
    w1 = "Fire"
}

//Here it generates any of the second word

rand = Math.random()

if (rand < 0.33) {
    w2 = "Engine"
}
else if (rand < 0.66 && rand >= 0.33) {
    w2 = "Foods"
}
else {
    w2 = "Garments"
}

//Here it generates any of the third word

rand = Math.random()

if (rand < 0.33) {
    w3 = "Bros"
}
else if (rand < 0.66 && rand >= 0.33) {
    w3 = "limited"
}
else {
    w3 = "hub"
}
console.log( ` ${w1} ${w2} ${w3} `)

