# HTML Portfolio Code Review

### Reviewed by: [Max Resnick](https://github.com/PDXDevCampJuly/max-resnick)
September 12, 2015

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
14 Sep 2015

##### html__portfolio/urls.py >>>

This was a good idea. Thanks for discussing this with me today to better understand how Django works and helping to implementing a 'catch all' in the html_portfolio/urls.py.

Added static directory.

Renamed the 'about' app to act as a global, more generic app; 'home'

##### javapic | javapic_jquery >>>

The URL structure for both apps are now {app}/join and {app}/gallery; no longer {app}/join/gallery.

##### javapic_jquery >>>

Removed the css directory and images directory. The css and images now reference the javapic app.

Converted the template reference to the jQuery to cdn.

##### forum >>>

Converted the template reference to the jQuery to cdn.

---
Let me know, if I may clarify any changes or if you have some suggestions on where to go from here… Thanks again.


### Reviewed by: [Max Resnick](https://github.com/PDXDevCampJuly/max-resnick)
August 16, 2015

```

`home/urls.py`
--------------

* L2 can be 86’d

`html_portfolio/urls.py`
-----------------------

* L2 can be 86’d

`home/templates`
----------------

* L1 of about.html && index.html should be killed, your base should include that.
* L16 - L21, L49 - L62 rather than using an HTML comment, use a django template comment. This will prevent it from render so the browser will never see it.
* L6 - L23 - ideally you should go ahead and put this as a template block called `header`, or better yet multiple blocks named, `meta`, `css`, `javasript` this way you can overide via completly blocking them or adding to them based on the needs of a template that’s extending base.html
* L23, there’s no need for this if L6 - L23 become new blocks
* If you plan on taking this further, i.e. making this public, consider breaking your templates down further. Consider how could all of your apps extend from base, and add their needed JS and CSS
```

### Response
22 Sep 2015

Changes annotated below. Thanks for the heads-up about using Django comments instead of html comments. 

##### home/urls.py:
no action taken as we discussed, the import is needed

##### html_portfolio/urls.py:
L2 — commented-out “from django.contrib import admin” for potential use later

##### home/base.html:
L49-62 — removed old commented-out html

##### home/about.html:
L1 — removed “<!DOCTYPE html>”
L16 — removed old commented-out html
L21 — removed old commented-out html

Many changes have been implemented since the last review. New additions include:

##### html_portfolio/urls.py:
‘namespace’ defined to distinguish the javapic app versus javapic jQuery

##### home/base:
There are now several base html templates: metadata, css_links, and js_scripts. As suggested in the previous review, this provides the flexibility for each app to utilize these base templates when extending the base.html. 

Within base.html there are now additional django block tags providing inheritance options for the metadata, css_links, title, navbar_subtext, and the js_scripts on top of the base html templates listed above. 

The project now has a consistent navbar and footer throughout each app.  

---
Let me know, if I can help with anything. Thanks again for the help.

### Reviewed by: [Max Resnick](https://github.com/PDXDevCampJuly/max-resnick)
September 22, 2015

```

## "Go ahead a turn in!"

```

### Response
22 September 2015

Thanks Max for your help.
