#!/usr/local/bin/python

# This is the parser for East Dorset District Council.
# it is generated from the file CGITemplate

import cgi
import cgitb
#cgitb.enable(display=0, logdir="/tmp")


form = cgi.FieldStorage()
day = form.getfirst('day')
month = form.getfirst('month')
year = form.getfirst('year')


authority_name = "East Dorset District Council"
authority_short_name = "East Dorset"
base_url = "http://193.243.228.16/PublicAccess/dc/"

import PublicAccess

parser = PublicAccess.PublicAccessParser(authority_name, authority_short_name, base_url)

xml = parser.getResults(day, month, year)

print "Content-Type: text/xml"     # XML is following
print
print xml                          # print the xml
