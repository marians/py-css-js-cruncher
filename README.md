JSS and CSS Minifier/Combiner
=============================

This script helps you to automate the generation of combined and minified
CSS and JavaScript files.

Why would you need that?
------------------------

You might have heard that, when it comes to web page/app load times, every
request counts. And by combining files, you can save requests. And once you
combine your files, you can as well minify them to make the download even faster.

If you want to find out more, read about the details here:

* [http://code.google.com/intl/de/speed/page-speed/docs/rtt.html](http://code.google.com/intl/de/speed/page-speed/docs/rtt.html)
* [http://developer.yahoo.com/performance/rules.html](http://developer.yahoo.com/performance/rules.html)

Prerequisites
-------------

* Python (tested with Python 2.6.1 on Mac OS and Windows)
* jsmin Python module from [http://pypi.python.org/pypi/jsmin/](http://pypi.python.org/pypi/jsmin/)
* cssmin Python module from [http://pypi.python.org/pypi/cssmin/](http://pypi.python.org/pypi/cssmin/)


How to use this script
----------------------

* Edit the file build_cssjs.conf to fit your needs. All you have to enter here 
  is the paths to all files you want to combine. The paths can either be
  relative to the location of the script or absolute. Use the / as seperator, no
  matter if you're on winows, Mac, Linux or elsewhere.

* Run the script

Output
------

You will get a maximum of two files as an output. One CSS and one JS file. They will
be named in the format of 

	compact_YYYYMMDDHHMM.css
	compact_YYYYMMDDHHMM.js


License
-------

None. No restrictions.
