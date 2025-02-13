const incbtn = document.getElementById("inc")
const decbtn = document.getElementById("dec")
const resetbtn = document.getElementById("reset")
const countlabel = document.getElementById("countlabel")

let count = 0;
inc.onclick = function () {
    count++;
    countlabel.textContent = count;
}
decbtn.onclick = function () {
    count--;
    countlabel.textContent = count;
}
resetbtn.onclick = function () {
    count=0;
    countlabel.textContent = count;
}