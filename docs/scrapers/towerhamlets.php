<?php

//Includes
require_once('config.php');
require_once('application.php');

//build date url
$request_time = get_time_from_get();

//search url
$search_url = "http://194.201.98.213/WAM/weeklyApplications.do?endDate=#enddate&action=showWeeklyList&sortOrder=1&areaCode=%25&applicationType=%25";
$search_url = str_replace("#enddate", $request_time * 1000, $search_url);

//comment and info urls
$info_url_base = "http://194.201.98.213/WAM/showCaseFile.do?action=show&appType=Planning&appNumber=";
$comment_url_base = "http://194.201.98.213/WAM/createComment.do?action=CreateApplicationComment&&applicationType=PLANNING&appNumber=";
	
//grab urls
$applications = scrape_applications_wam($search_url, $info_url_base, $comment_url_base);

display_applications($applications, "Tower Hamlets Council", "Tower Hamlets");

?>
