#
# CSS / JS file merger and minifier
#
# (c) by Marian Steinbach (marian@sendung.de)
#
# LICENSE: Feel free to use and redistribute in any way you like.
#
# INSTALL: 
#
# This script relies on cssmin and jsmin for Python. If you have Paython
# setuptools, you can easily install these modules using
# $> easy_install cssmin
# $> easy_install jsmin
#
# USAGE:
# 
# 1. Edit build_cssjs.conf to match the files you want to compress
# 2. Run this script
#
# As a result, you should have up to 2 output file in the 
# folder containg this script.

import os
import re
import datetime
import jsmin
import cssmin

CONFIGFILE = 'build_cssjs.conf'

def getPathsFromConfig(ext):
	global CONFIGFILE
	arr = []
	if os.path.exists(CONFIGFILE):
		f = file(CONFIGFILE);
		text = f.read();
		text = re.sub("\r", "\n", text)
		text = re.sub("\n\n", "\n", text)
		text = re.sub("\n\n", "\n", text)
		lines = text.split("\n")
		for line in lines:
			line = line.strip();
			#print "'" + line[-len(ext):] + "'"
			if line[0:1] != '#' and line != '' and (line[-len(ext):].lower() == ext.lower()):
				#print line
				arr.append(line)
		return arr
	else:
		print "ERROR: build_cssjs.conf file not available."


cssfiles = getPathsFromConfig('.css')
jsfiles = getPathsFromConfig('.js')

now = datetime.datetime.now()

outfilename = 'compact_' + now.strftime("%Y%m%d%H%M") + '.css'
outfile = open(outfilename, 'w')
css = ''
for infilepath in cssfiles:
	print infilepath
	if os.path.exists(infilepath):
		#print "Gefunden " + infilepath
		css += file(infilepath).read() + "\n\n"
	else:
		print "ERROR: File '%s' not found." % infilepath
#print outfilename
outfile.write(cssmin.cssmin(css))
outfile.close()



outfilename = 'compact_' + now.strftime("%Y%m%d%H%M") + '.js'
outfile = open(outfilename, 'w')
js = ''
for infilepath in jsfiles:
	print infilepath
	if os.path.exists(infilepath):
		#print "Gefunden " + infilepath
		js += file(infilepath).read() + "\n\n"
	else:
		print "ERROR: File '%s' not found." % infilepath
#print outfilename
outfile.write(jsmin.jsmin(js))
outfile.close()