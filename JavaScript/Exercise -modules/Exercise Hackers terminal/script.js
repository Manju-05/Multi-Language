console.log('Testing ');

async function GenLine1() {
    return new Promise((reslove, reject) => {
        setTimeout(() => {
            document.querySelector(".fir").innerHTML = `>>>Initializing Hacking...`;
        }, 2000)
    })
}

async function GenLine2() {
    return new Promise((reslove, reject) => {
        setTimeout(() => {
            document.querySelector(".sec").innerHTML = ">>>Reading your files...";
        }, 4000)
    })
}
async function GenLine3() {
    return new Promise((reslove, reject) => {
        setTimeout(() => {
            document.querySelector(".thir").innerHTML = ">>>Reading the passwords...";
        }, 5900)
    })
}

async function GenLine4() {
    return new Promise((reslove, reject) => {
        setTimeout(() => {
            document.querySelector(".fou").innerHTML = ">>>Cleaning Up...";
        }, 7500)
    })
}

async function GenLine5() {
    return new Promise((reslove, reject) => {
        setTimeout(() => {
            document.querySelector(".fiv").innerHTML = ">>>Sucessfully Completed...";
        }, 9000)
    })
}
// GenLine1()
// GenLine2()
// GenLine3()
// GenLine4()
// GenLine5()

GenLine1().then()
GenLine2().then()
GenLine3().then()
GenLine4().then()
GenLine5()
let t = setInterval(() => {
        let last = document.body.getElementsByTagName("p");
        last = last[last.length - 1]
        if(last.innerHTML.endsWith(".....")){
            last.innerHTML = last.innerHTML.slice(0, last.innerHTML.length-4)
        }
        else{
            last.innerHTML = last.innerHTML + ".."
        }
        ``
    }, 100);
