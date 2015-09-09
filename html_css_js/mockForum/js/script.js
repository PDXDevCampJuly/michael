// mock forum by michael
// Utilizing Google Spreadsheets API

var $forumWrapper = $('#forumWrapper');
var $msgSuccess = $('.text-success');
var $msgDanger = $('.text-danger');

  // hide helper messages
$('input').on('focus', function() {
  $msgSuccess.removeClass("show").addClass("hidden");
  $msgDanger.removeClass("show").addClass("hidden");
});
$('textarea').on('focus', function() {
  $msgSuccess.removeClass("show").addClass("hidden");
  $msgDanger.removeClass("show").addClass("hidden");
});

// submits a post to the Google spreadsheet
$('[type=button]').on('click', function() {
  var title = $('#title').val();
  var body = $('#body').val();
  if ((title !== "") && (body !== "")) {
    $.ajax({
      url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
      type: "POST",
      dataType: "xml",
      data: { "entry_434124687": title, "entry_1823097801": body },
      statusCode: {
        0: function() {
          $('#title').val("");
          $('#body').val("");
          $msgSuccess.removeClass("hidden").addClass("show");
        },
        200: function() {
          $('#title').val("");
          $('#body').val("");
          $msgSuccess.removeClass("hidden").addClass("show");
        }
      }
    });
  } else {
    $msgDanger.removeClass("hidden").addClass("show");
  }
});

// AJAX Get - grabs the data from the Google spreadsheet
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
});

// populates the posts to the webpage for the user to see
function createForumPost(title, body) {
  $forumWrapper.append('<div class="alert alert-warning" role="alert"><h4>' + title + '</h4><p>' + body + '</p></div>').hide().fadeIn('slow');
}


