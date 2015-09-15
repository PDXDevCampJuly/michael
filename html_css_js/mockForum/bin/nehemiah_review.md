# Mock Forum Code Review

### Reviewed by: [Nehemiah Newell](https://github.com/nehemiahnewell)
10 September 2015
```
css

Nothing stands out as bad. Only note I would make is that everything except font size is in px,
which is completely unresponsive. You import bootstrap for a lot of your css behaviour though, so
that's less of an issue.

html

I like your page design, though I would make the left column smaller and the right bigger, as the
focus should be on the messages.

Javascript

Line 8-16: I'm unclear as to the point of this. You might want to comment this more. I think it's
suppose to let a message appear to inform me of success sending a post or failure, but if so it
disappears so fast I never see it.

Line 28-33: It's clearly suppose to reload the page so you catch your new posts, but it seems to
happen so fast that doesn't always happen. You could put a delay on it of three or four seconds,
or you could just periodically reload the page automatically to catch all new entries.
```

### Response
11 September 2015

Hey Nehemiah, thanks for the review. I made several changes to include media queries in the CSS and the JS (the JS media queries only change once the page is refreshed)(e.g. the form becomes smaller for mobile devices), set timeout of 15sec., removed the reload function that made the success message disappear, and added additional comments to the success message on the HTML. Let me know if you get a chance to look at it again.

### Update 
14 September 2015

Removed the setTimeout of 15 seconds and the success message. The page will reload on a successful POST. 

### Reviewed by: [Nehemiah Newell](https://github.com/nehemiahnewell)
14 September 2014

```
CSS 

Looks good

JS

Comments cleaned up, code cleaned up. No auto refresh, but that isn't a requirement, so it looks good.

html

looks ok.
```
## "This looks good enough to turn in."

### Response
14 September 2015

Thanks Nehemiah for taking the time to review the code.
