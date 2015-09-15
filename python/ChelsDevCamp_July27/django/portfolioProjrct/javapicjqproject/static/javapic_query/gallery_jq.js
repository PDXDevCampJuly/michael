/**
* Created by Chelsea on 9/1/15.
*/

var $position=("#gallery");
var $displayImage=("#image_show");
var $imageChild=("div img:first-child");
var $images = [];
//Getting elements
//Making an array

( function () {
    for (var i=1; i<=60; i ++) {
        if (i<=9){
            $images.push("images/pdxcg_0" + i + ".jpg");

        } else {
            $images.push("images/pdxcg_" + i + ".jpg");
        }
    }
    //Loops thru 1-60 and appends imgs to $images
    // If i is less then 10 add a 0
    //Else don't add 0
}());

var items = [];
jQuery.each($images, function(i, item) {
  items.push('<li><img src=' + item + '></li>')
});
$("#gallery").append(items);
//making li's and img with the images in $images

changeName();
//calls function
function changeName() {   // if the will support it continue
    var name = sessionStorage.getItem('name');  //Getting the item from sessionStorage
    document.body.innerHTML = document.body.innerHTML.replace(/tiffany/g, name);
}
//Takes the name from join and swaps the word tiffany for it

$($position).on( "click", function(event) {
    $("li").addClass('display_none');
    $($displayImage).attr('class', 'display_img');
    $($imageChild).attr('src', event.target.src);
});
//Changes the class

$($imageChild).on( "click", function(event) {
    event.stopPropagation()
});
//Makes it do nothing

$($displayImage).on("click", function(event){
        $($displayImage).attr('class', 'display_none');
    }
);
//Changes class