// console.log("welocome")
document.title = "js"

// this is the  async function that fetches the data over the network and returns the data in the background
// The fetch() method is used to send the requests to the server without refreshing the page. It is an alternative to the XMLHttpRequest object.
// A fetch() method can be used with many type of requests such as POST, GET, PUT and DELETE.

async function getdata() {
    //simulate getting data from the server
    let x = await fetch('https://jsonplaceholder.typicode.com/todos/1')//fetches the data from the server and returns the raw data 
    // returns the promise 

    let data = await x.json() //parses the raw data into desired format like json text etc..
    console.log(data)
    console.log(x);
    return 324
}
async function main() {

    console.log('Task 1 loading data ✅');
    console.log('Task 1 processing data ✅');
    console.log("Task 1 completed ✅")

    let data = await getdata()  //waiting for the data to fetch and return after  returning the data the further statements are executed
    //if we dont wait for the get data it only returns the promise
    console.log(data);
    console.log("Task2 intiliaized")
    console.log('task 2 is loading the data');
}
main()

// Example of FETCH  POST method implementation:

// async function postData(url = "", data = {}) {
//     // Default options are marked with *
//     const response = await fetch(url, {
//       method: "POST", // *GET, POST, PUT, DELETE, etc.
//       mode: "cors", // no-cors, *cors, same-origin
//       cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
//       credentials: "same-origin", // include, *same-origin, omit
//       headers: {
//         "Content-Type": "application/json",
//         // 'Content-Type': 'application/x-www-form-urlencoded',
//       },
//       redirect: "follow", // manual, *follow, error
//       referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//       body: JSON.stringify(data), // body data type must match "Content-Type" header
//     });
//     return response.json(); // parses JSON response into native JavaScript objects
//   }

//   postData("https://example.com/answer", { answer: 42 }).then((data) => {
//     console.log(data); // JSON data parsed by `data.json()` call
//   });



