#.NET MVC Unused View Finder
=============================

Simple python script to find view references.

##Usage

```sh
python finder.py [your application path]
```

If you want to save the output, you can always...

```sh
python finder.py [your application path] > log.txt
```

##Output

The output will be something like this:

```
Locating view files...

View files found:
['_unusedPartial', '_usedPartial', 'UnusedView', 'UsedView']

Locating references...
----------------------

_unusedPartial

UNUSED VIEW:  _unusedPartial
----------------------

_usedPartial

line number:  2
line text:  @Html.Partial("_usedPartial")

----------------------

UnusedView

UNUSED VIEW:  UnusedView
----------------------

UsedView

line number:  3
line text:  	public ActionView UsedView()


line number:  10
line text:  		return View("UsedView");


----------------------

```

