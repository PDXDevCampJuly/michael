/**
 * Created by Chelsea on 9/1/15.
 */

var $name=$('[name=name]'); //Setting $name to the input with the name name

var alert = [];
alert.push('<p>'+ "That email isn't valid. Please try again");
$( "main" ).append(alert);
$( "p" ).hide().css({'text-align': 'center', 'color': '#94BA65'});
//Making/appending a paragraph to main that will be hidden

function checkIfValid(event) {
    event.preventDefault(); //preventing default
    var inputEmail=$('input[name=email]').val(); //Setting inputEmail to the input with the name email

        var validInput = /[^@]+@[^@.].+/.test(inputEmail); //making a very simple regex amake making it test against inputEmail

        if (!validInput) {
            $( "p" ).slideDown(600).show();
            event.preventDefault();
            //If email is not valid display alert and preventDefault
        } else {
            sessionStorage.setItem('name', $name.val());
            document.location.href = '../html/gallery.html';
            // Else save the users name they imputed and go to the gallery
        }
}

$("#signup").submit(checkIfValid);
//Event listener for when they try to submit the form