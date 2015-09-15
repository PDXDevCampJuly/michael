/**
 * Created by Chelsea on 9/1/15.
 */

$(document).ready(function(){
    setInterval(function(){ changebg(); }, 20000);

    var $bgImg =("#jumbotron");
    var i = 1;

    function changebg() {
        if (i<=9){
            console.log(i);
            $($bgImg).css('background-image','url(images/pdxcg_0' + i + '.jpg)');
        }
        else {
            console.log(i);
            $($bgImg).css('background-image','url(images/pdxcg_' + i + '.jpg)');
        }
        if (i===60) {
            i=0;
        }
        i++;
    }
});
//Loops thru i and changes the background img every 20 seconds