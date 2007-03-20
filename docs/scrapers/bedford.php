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
	$search_url = "http://www.publicaccess.bedford.gov.uk/publicaccess/dc/DcApplication/application_searchresults.aspx?searchtype=WEEKLY&selWeeklyListRange=#daterange&weektype=VAL";
    $date_range = "{$day}%2F{$month}%2F{$year}%7C{$day}%2F{$month}%2F{$year}";
	$search_url = str_replace("#daterange", $date_range, $search_url);

	//comment and info urls
	$info_url_base = "http://www.publicaccess.bedford.gov.uk/publicaccess/dc/DcApplication/application_detailview.aspx?caseno=";
	$comment_url_base = "http://uniformpublicaccess.oxford.gov.uk/publicaccess/tdc/DcApplication/application_comments_entryform.aspx?caseno=";
	
    //grab urls
	$applications = scrape_applications_publicaccess($search_url, $info_url_base, $comment_url_base);

    //smarty
	$smarty = new Smarty;
    $smarty->force_compile = true;
    $smarty->compile_dir = SMARTY_COMPILE_DIRECTORY;
    $smarty->template_dir = "../templates";
    $smarty->assign("authority_name", "Bedford Borough Council");
    $smarty->assign("authority_short_name", "Bedford");    
    
	if (sizeof($applications) > 0){
        $smarty->assign("applications", $applications);
	}
	
	$smarty->display("xml.tpl");

?>