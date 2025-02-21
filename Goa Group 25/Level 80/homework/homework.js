
let password = 'Group 41 is best';

function Password() {
    let attempts = 0;
    let input;

    while (attempts < 3) {
        input = prompt("შეიყვანოთ პაროლი:");
        attempts++;

        if (input === password) {
            console.log("შეყვანილი პაროლი სწორია");
        }

        else{
            console.log("პაროლი არასწორია")
        }
    }

    alert("ამოიწურა ცდების რაოდენობა");
}

Password();