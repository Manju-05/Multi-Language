async function getdata(){
return new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve(234)
    },3000)
})
}
async function main(){

    console.log('Task 1 loading data ✅');
    console.log('Task 1 processing data ✅');
    console.log("Task 1 completed ✅")
    
     //if we donot write the await keyword then automatically it ececutes the rest of the statements 
    //NOTE: await can onlybe used in the async functions we cant use it outside of the async functions

    let data=await getdata() 
    console.log(data);
    console.log("Task2 intiliaized")
    console.log('task 2 is loading the data');
}
main()
    
    
    // let data= getdata()

//this is the call for the asynchronous function the asynchronous functions donot wait  for the complete execution if they see the functioncall of the asynchronous function they simply jumps over them and executes the rest of the statements

//so if there is a condition to execute only after the asynchronous function execution is done this can be done by the using (then) 

//by using  (then) we can stop & make the rest of the statements wait until the execution of the sychronous functions.

// data.then((v)=>{
//     console.log(data);
//     console.log("Task2 intiliaized")
//     console.log('task 2 is loading the data');
    
// })

// In Simple words async and await are used instead of (then) and callback functions
// callback-hell inorder to make the code wait to execute the  asynchronous fuctions 
// instead of executing the rest of statements
