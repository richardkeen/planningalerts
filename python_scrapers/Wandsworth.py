import urllib2
import urllib
import re

import datetime
import cgi

from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup, SoupStrainer

from PlanningUtils import PlanningApplication, \
    PlanningAuthorityResults, \
    getPostcodeFromText

class WandsworthParser:

    def __init__(self, *args):

        self.authority_name = "London Borough of Wandsworth"
        self.authority_short_name = "Wandsworth"
        self.base_url = "http://www.wandsworth.gov.uk/gis/search/Search.aspx"

        self._results = PlanningAuthorityResults(self.authority_name, self.authority_short_name)

    def getResultsByDayMonthYear(self, day, month, year):
        search_day = datetime.date(year, month, day)
        formatted_search_day = search_day.strftime("%d-%m-%Y")

        post_data = urllib.urlencode([
            ("__EVENTTARGET", ""),
            ("__EVENTARGUMENT", ""),
            ("cboRecordType", "DC"),
            ("cboNumRecs", "99999"),
            ("cmdSearch", "Search"),
            ("drReceived:txtStart", formatted_search_day),
            ("drReceived:txtEnd", formatted_search_day)
        ])

        response = urllib2.urlopen(self.base_url, post_data)

        # Modify the redirect response URL to remove the XSL template param
        # so we get more detailed XML embedded in HTML instead
        redirect_url = response.geturl()
        redirect_url = re.sub("&XSLTemplate=xslt/Results.xslt", "", redirect_url)

        results_response = urllib2.urlopen(redirect_url)

        try:
            soup = BeautifulSoup(results_response.read())

            # Get the XML content contained in the HTML doc
            td = soup.find("td", colspan="3")
            xml = str(td.contents[2])
            xml_soup = BeautifulStoneSoup(xml)
        except:
            return self._results

        for entry in xml_soup.findAll('internet_web_search'):
            application = PlanningApplication()

            primary_key = entry.find('primary_key').renderContents()

            application.council_reference = entry.find('application_number').renderContents()

            application.info_url = "http://www.wandsworth.gov.uk/apply/showCaseFile.do?appNumber=%s" \
                % urllib.quote(application.council_reference)

            application.comment_url = "http://www.wandsworth.gov.uk/apply/createComment.do?action=CreateApplicationComment&appNumber=%s" \
                % urllib.quote(application.council_reference)

            str_date_received = entry.find('received_date').renderContents()[0:10]
            date_received = datetime.datetime.strptime(str_date_received, "%Y-%m-%d")

            application.date_received = date_received

            application.address = entry.find('site_address').renderContents()

            application.description = entry.find('development_description').renderContents()

            # We need to make another request to get postcode details
            details_url = "http://www.wandsworth.gov.uk/gis/search/StdDetails.aspx?"
            details_url = details_url + urllib.urlencode([
                ("PT", "Planning Application Details"),
                ("TYPE", "WBCPLANNINGREF"),
                ("PARAM0", primary_key),
                ("XSLT", "xslt/planningdetails.xslt"),
                ("DAURI", "PLANNING")
            ])

            details_response = urllib2.urlopen(details_url)
            details_soup = BeautifulSoup(details_response.read())
            postcode_row = details_soup.find('table', "bodytextsmall").findAll('tr')[5]
            postcode_cell = postcode_row.find('td', "searchinput")
            application.postcode = getPostcodeFromText(postcode_cell.string.strip())

            self._results.addApplication(application)

        return self._results

    def getResults(self, day, month, year):
        return self.getResultsByDayMonthYear(int(day), int(month), int(year)).displayXML()

if __name__ == '__main__':
    parser = WandsworthParser()
    print parser.getResults(11,2,2010)