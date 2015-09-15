/**
 * Created by Chelsea on 8/27/15.
 */
setInterval(function(){ changebg(); }, 20000);

var bgImg = document.getElementById("jumbotron");
var i = 1;

function changebg() {
    if (i<=9){
        console.log(i);
        bgImg.style.backgroundImage = "url('static/images/pdxcg_0" + i + ".jpg')";
    }
    else {
        bgImg.style.backgroundImage = "url('static/images/pdxcg_" + i + ".jpg')";
    }
    if (i===10) {
        i=0;
    }
    i++;
}

//loops through function every 20 seconds
//looping through the images and either adding a 0 or not adding a 0
//Then looping through all the images and if the image equals 60 goes back to 0