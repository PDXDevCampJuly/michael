/**
 * Created by Chelsea on 9/8/15.
 */

$.ajax({
url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
type: "GET",
dataType: "jsonp",
complete: function(data) {
    console.log(data.responseJSON);
    var object = data.responseJSON.feed.entry;
    object.reverse();
    for (var i=0; i < object.length; i++) {

        var itemtitle = data.responseJSON.feed.entry[i].gsx$posttitle.$t;
        var itembody = data.responseJSON.feed.entry[i].gsx$postbody.$t;

        var string = '<li>'+itemtitle+'<br>'+itembody+'</li>';

        $( 'body' ).append(string);
    }
}
});


$('#post').on('submit', function (e){
    e.preventDefault();
    var title = $('input[name=posttitle]');
    var body = $('input[name=postbody]');
    var post = {'entry_434124687':title.val(), 'entry_1823097801': body.val()};
    $.post(
        'https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse', post);
    location.reload();
});

$(document).ready(function() {
var stickyNavTop = $('.nav').offset().top;

var stickyNav = function(){
var scrollTop = $(window).scrollTop();

    if (scrollTop > stickyNavTop) {
        $('.nav').addClass('sticky');
    } else {
        $('.nav').removeClass('sticky');
    }
};

stickyNav();

$(window).scroll(function() {
    stickyNav();
});
});