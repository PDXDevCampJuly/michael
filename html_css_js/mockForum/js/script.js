// mock forum by michael
// Utilizing Google Spreadsheets API

var $forumWrapper = $('#forumWrapper');

// AJAX Get - grabs the data from the spreadsheet
$.ajax({
  type: 'GET',
  dataType: 'jsonp',
  crossDomain: true,
  url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
  error: function() { console.log("fail.."); },
  success: function(data) {
    entries = data.feed.entry;
    for (var i = 0; i < entries.length; i++) {
      var title = entries[i].gsx$posttitle.$t;
      var body = entries[i].gsx$postbody.$t;
      // console.log(entries[i].gsx$postbody.$t);
      // console.log(entries[i].gsx$posttitle.$t);
      createForumPost(title, body);
    };
    console.log(entries[3].gsx$postbody.$t);
  }
});

// populates the posts to the webpage
function createForumPost(title, body) {

  // console.log(title, body);
  $forumWrapper.append('<div><p>' + title + '</p><p>' + body + '</p></div>');
}

// submits a post to the spreadsheet
$('form').on('submit', function(e) {
  e.preventDefault();
  var title = $('#title').val();
  var body = $('#body').val();
  if ((title !== "") && (body !== "")) {
    $.ajax({
      type: 'POST',
      dataType: 'xml',
      url: 'https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse',
      data: { "entry_434124687": title, "entry_1823097801": body },
      statusCode: {
        0: function (){
          $('#title').val("");
          $('#body').val("");
          alert('successful #1');
        },
        200: function (){
          $('#title').val("");
          $('#body').val("");
          alert('successful #2');
        }
      }
    })
  } else {
    alert("could be blank.. could be an error..");
  }
})


