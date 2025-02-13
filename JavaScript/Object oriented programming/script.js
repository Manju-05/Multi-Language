 console.log('Testing the js');


let obj = {
    "name": "manju",
    "course": "diploma",
    "year": "3"

}
console.log(obj)
let details = {
    "college": "engg clg",
    "course": "dipoma",
    'year': "3",
}

let student_2 = {
    "name":"ram",
    "roll":"074"
}
console.log(student_2)
student_3={
    "name":"hanu",
    "roll":"099"
}
console.log(student_3)

student_2.__proto__ = details; //prototyping
student_3.__proto__ = details; //prototyping


class Animal{
    constructor(name){
        this.name=name
        console.log("object is created..! for animal class");
    }

    eats(){
        console.log("eatting veg ...");
    }

    jumps(){
        console.log("jumping...");
    }
}
let obj1=new Animal("jaggu"); // Animal calling the contructor we give the value name 
console.log(obj1)

//creating the class (Animal) and creating the constructor with name as a parameter and creating the functions... and created an object 

class Lion extends Animal{
    constructor(name){
        super(name)
        console.log('object is created..! for lion class'); //method Overriding..//overriding the method that is declared in the animal class..
    }
    eats(){
        super.eats()// super keyword is used to call the method in the parent class..
        console.log('lion eats non-veg...');
    }
    display(){
        console.log(' this is the example of inheritance like this we can add mutiple functions');
    }
    inherit(){
        console.log('lion is inherited by animal lion has the features of the animal and the lion also ');
    }

}
let obj2=new Lion("Puli_Raja");
console.log(obj2);



//this the example of satic method
class Sample{
    static run(){
        console.log('this is the example of the static method we are calling the method without creating the object... by using the static method | by using the calss name we have to call the method ');
    }
}

Sample.run() //calling the method by using the class name 
console.log('Ending the js in the script.js');
