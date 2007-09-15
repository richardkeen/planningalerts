#!/usr/local/bin/python

# This is the parser for South Lakeland District Council.
# it is generated from the file CGITemplate

import cgi
import cgitb
#cgitb.enable(display=0, logdir="/tmp")


form = cgi.FieldStorage()
day = form.getfirst('day')
month = form.getfirst('month')
year = form.getfirst('year')


authority_name = "South Lakeland District Council"
authority_short_name = "South Lakeland"
base_url = "http://www.southlakeland.gov.uk/fastweb/"

#print "Content-Type: text/html"     # HTML is following
#print

import FastWeb

parser = FastWeb.FastWeb(authority_name, authority_short_name, base_url)

xml = parser.getResults(day, month, year)


print "Content-Type: text/xml"     # XML is following
print
print xml                          # print the xml
