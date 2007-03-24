<?php

//Includes
require_once('config.php');
require_once('application.php');

//build date url
$request_time = get_time_from_get();

//search url
$search_url = "http://idox.hackney.gov.uk/WAM/weeklyApplications.do?action=showWeeklyList&areaCode=%25&sortOrder=1&endDate=#enddate&applicationType=%25&Button=Search";
$search_url = str_replace("#enddate", $request_time * 1000, $search_url);

//comment and info urls
$info_url_base = "http://idox.hackney.gov.uk/WAM/showCaseFile.do?action=show&appType=Planning&appNumber=";
$comment_url_base = "http://idox.hackney.gov.uk/WAM/createComment.do?action=CreateApplicationComment&&applicationType=Planning&appNumber=";

//grab urls
$applications = scrape_applications_wam($search_url, $info_url_base, $comment_url_base, 2);

display_applications($applications, "London Borough of Hackney", "Hackney");

?>
