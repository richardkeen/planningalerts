#!/usr/local/bin/python

# This is the parser for Carlisle City Council.
# it is generated from the file CGITemplate

import cgi
import cgitb
#cgitb.enable(display=0, logdir="/tmp")


form = cgi.FieldStorage()
day = form.getfirst('day')
month = form.getfirst('month')
year = form.getfirst('year')


authority_name = "Carlisle City Council"
authority_short_name = "Carlisle"
base_url = "http://planning.carlisle.gov.uk/acolnet/acolnetcgi.gov?ACTION=UNWRAP&RIPNAME=Root.pgesearch"

import AcolnetParser

parser = AcolnetParser.CarlisleParser(authority_name, authority_short_name, base_url)

xml = parser.getResults(day, month, year)

print "Content-Type: text/xml"     # XML is following
print
print xml                          # print the xml
