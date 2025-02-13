console.log("Testing the js in the getter and setter js ")

class User{
    constructor(name){
        this.name=name
    }
    get name(){
        return this._name; //we used the _ to avoid the name collosion..
    }
    set name(value){
        if(value.length<18){
            console.log('name is tooo short');
            return;
        }
        this._name=value;
    }
}
let object= new User("bosidike");
console.log(object.name);
object.name="";

