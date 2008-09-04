"""
This is the screenscraper for Westminster City Council.

I have just noticed that there is a PublicAccess underneath all this, but
it only has the apps in for which they are accepting comments, so I think
we may as well use this url and get the lot...

This is the PublicAccess url:
http://publicaccess.westminster.gov.uk/publicaccess/
"""

import urllib
import urlparse

import pycurl
import StringIO

import datetime, time
import cgi

import sys

from BeautifulSoup import BeautifulSoup

from PlanningUtils import PlanningApplication, \
    PlanningAuthorityResults, \
    getPostcodeFromText

date_format = "%d%%2F%m%%2F%Y"

class WestminsterParser:
    def __init__(self, *args):

        self.authority_name = "City of Westminster"
        self.authority_short_name = "Westminster"
        self.base_url = "http://www3.westminster.gov.uk/planningapplications/currentsearch-results.cfm"

        self._results = PlanningAuthorityResults(self.authority_name, self.authority_short_name)


    def getResultsByDayMonthYear(self, day, month, year):
        search_day = datetime.date(year, month, day)

#         post_data = [
#             ("EFNO", ""),
#             ("STName", ""),
#             ("STNUMB", ""),
#             ("ADRSNO", ""),
#             ("WARD", "AllWards"),
#             ("AGT", ""),
#             ("ATCDE", "AllApps"),
#             ("DECDE", "AllDecs"),
#             ("DTErec", search_day.strftime(date_format)),
#             ("DTErecTo", search_day.strftime(date_format)),
#             ("DTEvalid", ""),
#             ("DTEvalidTo", ""),
#             ("APDECDE", "AllAppDecs"),
#             ("submit", "Start+Search"),
#             ]
        post_data = "REFNO=&STName=&STNUMB=&ADRSNO=&WARD=AllWards&AGT=&ATCDE=AllApps&DECDE=AllDecs&DTErec=%(date)s&DTErecTo=%(date)s&DTEvalid=&DTEvalidTo=&APDECDE=AllAppDecs&submit=Start+Search" %{"date": search_day.strftime(date_format)}

        while post_data:
            

            # Now get the search page

            sys.stderr.write("Fetching: %s\n" %self.base_url)
            sys.stderr.write("post data: %s\n" %post_data) 
            

            # This gives us something to use as the callback
            fakefile = StringIO.StringIO()

            curlobj = pycurl.Curl()
            curlobj.setopt(pycurl.URL, self.base_url)
            curlobj.setopt(pycurl.POST, True)
            curlobj.setopt(pycurl.POSTFIELDS, post_data)
            curlobj.setopt(pycurl.WRITEFUNCTION, fakefile.write)
            curlobj.setopt(pycurl.FOLLOWLOCATION, True)
            curlobj.setopt(pycurl.MAXREDIRS, 10)

            curlobj.perform()

            sys.stderr.write("Got it\n")
            soup = BeautifulSoup(fakefile.getvalue())

            # We may as well free up the memory used by fakefile
            fakefile.close()

            sys.stderr.write("Created soup\n")

            results_form = soup.find("form", {"name": "currentsearchresultsNext"})

            # Sort out the post_data for the next page, if there is one
            # If there is no next page then there will be no inputs in the form.
            # In this case, post_data will be '', which is false.

            sys.stderr.write("Found form containing results\n")

            post_data = urllib.urlencode([(x['name'], x['value']) for x in results_form.findAll("input")])

            sys.stderr.write("Got post data\n")

            # Each result has one link, and they are the only links in the form

            links = results_form.findAll("a")

            sys.stderr.write("Got list of links\n")

            for link in links:

                sys.stderr.write("Working on link: %s\n" %link['href'])

                application = PlanningApplication()

                application.date_received = search_day
                application.info_url = urlparse.urljoin(self.base_url, link['href'])
                application.council_reference = link.string.strip()

                application.address = link.findNext("td").string.strip()
                application.postcode = getPostcodeFromText(application.address)

                application.description = link.findNext("tr").findAll("td")[-1].string.strip()

                # To get the comment url, we're going to have to go to each info url :-(

                sys.stderr.write("Fetching: %s\n" %application.info_url)


                fakefile = StringIO.StringIO()


                curlobj.setopt(pycurl.HTTPGET, True)
                curlobj.setopt(pycurl.WRITEFUNCTION, fakefile.write)

                # We have to convert the info url to ascii for curl
                curlobj.setopt(pycurl.URL, application.info_url.encode("ascii"))

                curlobj.perform()

                sys.stderr.write("Got it\n")

                info_soup = BeautifulSoup(fakefile.getvalue())

                fakefile.close()

                comment_nav_string = info_soup.find(text="Comment on this case")
                if comment_nav_string:
                    application.comment_url = comment_nav_string.parent['href']
                else:
                    application.comment_url = "No Comments"

    #http://publicaccess.westminster.gov.uk/publicaccess/tdc/dcapplication/application_comments_entryform.aspx?caseno=K586GHRP03500

                self._results.addApplication(application)

                sys.stderr.write("Finished that link\n")


        sys.stderr.write("Finished while loop, returning stuff.\n")

        return self._results

    def getResults(self, day, month, year):
        return self.getResultsByDayMonthYear(int(day), int(month), int(year)).displayXML()

if __name__ == '__main__':
    parser = WestminsterParser()
    print parser.getResults(1,8,2008)

