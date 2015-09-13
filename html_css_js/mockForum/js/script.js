// Responsive Mock Forum by michael
// Utilizing Google Spreadsheets API

var $forumWrapper = $('#forumWrapper');
var $msgSuccess = $('.text-success');
var $msgDanger = $('.text-danger');

  // hide helper message(s)
$('input, textarea').on('focus', function() {
  $msgSuccess, $msgDanger.removeClass("show").addClass("hidden");
});

// submits a post to the Google spreadsheet
$('button').on('click', function(event) {
  var $title = $('input').val();
  var $body = $('textarea').val();
  if (($title !== "") && ($body !== "")) {
    $.ajax({
      type: "POST",
      dataType: "xml",
      url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
      data: { "entry_434124687": $title, "entry_1823097801": $body },
      statusCode: {
        0: function() {
          //success msg (refer to index.HTML)
          $msgSuccess.removeClass("hidden").addClass("show");
        },
        200: function() {
          $msgSuccess.removeClass("hidden").addClass("show");
        }
      }
    });

    //clear input fields
    $('input').val("");
    $('textarea').val("");

  } else {
    //error msg (refer to index.HTML)
    $msgDanger.removeClass("hidden").addClass("show");
  }
});

// AJAX Get - grabs the data from the Google spreadsheet
(function refreshPosts() {
  $.ajax({
    type: 'GET',
    dataType: 'jsonp',
    url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
    error: function() { console.log("fail.."); },
    success: function(data) {
      entries = data.feed.entry;
      entries.reverse(); // show the last forum post first
      for (var i = 0; i < entries.length; i++) {
        var title = entries[i].gsx$posttitle.$t;
        var body = entries[i].gsx$postbody.$t;
        createForumPost(title, body);
      }
    }
  }).then(function() {
    setTimeout(refreshPosts, 15000);
  });
}());

// creates elements for DOM manipulation
// populates the posts to the webpage for the user to see
function createForumPost(title, body) {
  $forumWrapper.append('<div class="alert alert-warning" role="alert"><h4>' + title + '</h4><p>' + body + '</p></div>');
}

// // media queries for bootstrap classes
if (window.matchMedia("(min-width: 992px)").matches) {
  /* the viewport is at least 992 pixels wide */
  $('input, textarea').removeClass('input-md').addClass('input-lg');
  $('button').removeClass('btn-md').addClass('btn-lg');
} else {
  /* the viewport is less than 992 pixels wide */
  $('input, textarea').removeClass('input-lg').addClass('input-md');
  $('button').removeClass('btn-lg').addClass('btn-md');
}
