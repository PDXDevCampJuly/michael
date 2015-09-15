# HTML Portfolio Code Review

### Reviewed by: [Max Resnick](https://github.com/PDXDevCampJuly/max-resnick)
August 12, 2015

```
Overall
-------

* Project Structure is good.
* Consider renaming the app `about` to something slightly more generic.

html__portfolio/urls.py
----------------------
* If you want to use `about` as an app that handles some basic pages of content like an Index or About Me, that’s good but are you going to add another another url pattern for the next page in the “global” urls file? I might suggest a defining pattern for the about app, it could be a catch all as well... Meaning if you moved it to the bottom of the tuple, it will be the last url checked against, and your `about` app could catch everything else using the pattern `r’^’`, then the `about/urls.py` could handle that.
* The way you’ve structure L11 & L12 makes `about/urls.py` a bit pointless, your bypassing `about/urls.py` and going directly to the views function. You should use a catch all method mention in the previous comment, or pass the about patterns to the `about/urls.py` via `include()`, or remove the `about/urls.py`.


javapic/urls.py
---------------

* Your gallery URL has a structure of `javapic/join/gallery/` but `gallery` is not really a “child” of join nor does it have any relationship to join. In my opinion the structure should be `javapic/gallery`

Loading jQuery
--------------

* Currently you have jquery in two apps, it’s debatable if your app should carry it’s dependencies.
* If you want each app to carry the dependency jquery it might be wise to name them uniquely, with your current setup only of the jquery files is utilized, not both. Meaning the first app listed in your INSTALLED_APPS list’s JQuery version is loaded, which could cause issues.
* You could switch to a CDN to avoid this, or you can make a `static/js` directory structure as a sibling to all of your django apps. This is where you could place common assets like jQuery
```

### Response
14 September 2015

