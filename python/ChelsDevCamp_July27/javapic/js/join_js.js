 /**
 * Created by Chelsea on 8/27/15.
 */

var form = document.getElementById("signup");
var inputs = document.getElementsByTagName("input");
var name = document.querySelector('[name=name]');

function checkIfValid(event) {
    event.preventDefault();
    for (var i = 0; i < inputs.length; i++) {
// Looping through the array of inputs
        if (inputs[i].type == 'email') {
            // If while looping it finds a type called 'email'
            var validInput = /[^@]+@[^@.].+/.test(inputs[i].value);
            //Making a var that tests to see if the email is what we want and returns true of false
            if (!validInput) {
                invalidInput(event);


                // If validinput returns a false
                //calling the function invalidInput
            } else {
                sessionStorage.setItem('name', inputs[0].value);
                // Saving the name the user put in for later
                document.location.href = '../html/gallery.html';
                // Directing to gallery
            }
        }
    }
}

function invalidInput(event) {
    event.preventDefault(alert("That is not a valid input. Please try again."));}
    //Alerts user that their input was invalid
    // TODO: get rid of alert and make it more user friendly

form.addEventListener('submit', checkIfValid, false);
 //Event listener to check if the users input is valid when they press submit