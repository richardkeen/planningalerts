#!/usr/local/bin/python

# This is the parser for Fylde Borough Council.
# it is generated from the file CGITemplate

import cgi
import cgitb
#cgitb.enable(display=0, logdir="/tmp")


form = cgi.FieldStorage()
day = form.getfirst('day')
month = form.getfirst('month')
year = form.getfirst('year')


authority_name = "Fylde Borough Council"
authority_short_name = "Fylde"
base_url = "http://www2.fylde.gov.uk/planning/acolnetcgi.gov?ACTION=UNWRAP&RIPNAME=Root.pgesearch"

import AcolnetParser

parser = AcolnetParser.FyldeParser(authority_name, authority_short_name, base_url)

xml = parser.getResults(day, month, year)

print "Content-Type: text/xml"     # XML is following
print
print xml                          # print the xml
