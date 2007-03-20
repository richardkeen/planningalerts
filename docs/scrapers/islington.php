<?php

//Includes
require_once('config.php');
require_once('application.php');

//build date url
$current_date = getdate();
$day = $current_date['mday'] -5;
$month = $current_date['mon'];
$year = $current_date['year'];

//if any get params were passed, overwrite the default date
if (isset($_GET['day'])){
    $day = $_GET['day'];
}
if (isset($_GET['month'])){
    $month = $_GET['month'];
}
if (isset($_GET['year'])){
    $year = $_GET['year'];
}

	//search url
	$search_url = "https://www.islington.gov.uk/onlineplanning/apas/run/Wphappcriteria.showApplications?decfromdate=#daterange&dectodate=#daterange";
    $date_range = "{$day}-{$month}-{$year}";
	$search_url = str_replace("#daterange", $date_range, $search_url);

	//comment and info urls
	$info_url_base = "https://www.islington.gov.uk/onlineplanning/apas/run/WPHAPPDETAIL.DisplayUrl?theApnID=";
	$comment_url_base = "http://www.blaby.gov.uk/publicaccess/dc/DcApplication/application_comments_entryform.aspx?caseno=";
		
	//grab urls
	$applications = scrape_applications_islington($search_url, $info_url_base, $comment_url_base);
	
	//comment and info urls
	$info_url_base = "http://www.blaby.gov.uk/publicaccess/dc/DcApplication/application_detailview.aspx?caseno=";
	$comment_url_base = "http://www.blaby.gov.uk/publicaccess/dc/DcApplication/application_comments_entryform.aspx?caseno=";

print_r($applications);


    //Display applications
//    display_applications($applications, "Balby District Council", "Balby");

?>
