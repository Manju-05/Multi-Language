// Function to calculate factorial using a for loop

function factorial() {
    // Prompt user for input
    let userInput = prompt("Enter a number:");

    // Convert user input to a number
    let number = parseInt(userInput);

    // Check if the input is a valid number
    if (isNaN(number)) {
        alert("Please enter a valid number");
        return;
    }

    // Check if the number is non-negative
    if (number < 0) {
        alert("Please enter a non-negative number");
        return;
    }

    // Initialize factorial to 1
    let factorial = 1;

    // Calculate factorial using a for loop
    for (let i = 1; i <= number; i++) {
        factorial =  factorial*i;
    }

    // Display the result
    alert(`The factorial of ${number} is: ${factorial}`);
}

// Call the function to calculate factorial
factorial();



