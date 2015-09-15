/**
 * Created by Chelsea on 8/27/15.
 */


var position = document.getElementById("gallery");
var displayImage = document.getElementById("image_show");
var imageChild = displayImage.children[0];

var images = [];
function arrayOfImages() {
    for (var i=1; i<=60; i ++) {
        if (i<=9){
            images.push("images/pdxcg_0" + i + ".jpg");

        } else {
            images.push("images/pdxcg_" + i + ".jpg");
        }
    }
    //while the image is under 10 add a 0 if it's greater than 9 don't add a 0
}

arrayOfImages();
//calling the function

for (var i=0; i<images.length; i++) {

        var li = document.createElement("li");
        var img = document.createElement("img");
        img.src = images[i];

        li.appendChild(img);
        position.appendChild(li);
}
//Looping through the list of images and making a list with an image element with a picture in each one

position.addEventListener('click',function() {displayLargeImage(event); });
displayImage.addEventListener('click',function() {goBackToSmall();});
imageChild.addEventListener('click',function() {doNothing(event);});
// Event Listeners to enlarge images, shrink images, and to not do anything if the user presses on the image while it's
//large

function displayLargeImage(event){
    displayImage.className = "display_img";
    imageChild.src = event.target.src;
}
// changing the images class name to display_img

function goBackToSmall(){
    displayImage.className = "display_none";
}
// Changes the images class to display_none

function doNothing(event){
    event.stopPropagation()
}
// Stops it from bubbling

changeName();
function changeName(){   // if the will support it continue
    var str = document.getElementsByClassName("tagline");   //Making a var for the string on the HTML
    var name = sessionStorage.getItem('name');  //Getting the item from sessionStorage
    console.log(name);
    document.body.innerHTML = document.body.innerHTML.replace(/tiffany/g, name);
}
//Changing the name on the string in the HTML





