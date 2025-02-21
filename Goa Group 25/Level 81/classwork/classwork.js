

let result = 1;

for (let i = 1; i <= 10000; i++) {
    result *= i;

    if (result > 10000) {
        console.log("Loop stopped");
        break;
    }
}

console.log(result);