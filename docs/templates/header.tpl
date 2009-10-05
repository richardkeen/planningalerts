<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

	<title>PlanningAlerts.com | {$page_title}</title>
	<link rel="stylesheet" media="all" type="text/css" href="./css/memespring.css" />		
	<link rel="stylesheet" media="all" type="text/css" href="./css/main.css" />
    <script src="./javascript/main.js" type="text/javascript"></script>      	
	
</head>

<body>

    <div class="hide">
        <a href="#divContent">Skip navigation</a>
    </div>
    <div id="divAppeal">
        <strong>PlanningAlerts.com is currently experiencing technical difficulties because of ongoing legal action by Royal Mail</strong>.<br/> 
        Our provider of postcode data, ErnestMarples.com, has been taken offline because of legal action. Until we find an alternative source, PlanningAlerts.com will be unable to send out any email alerts, or publish data via it's API.
        We apologise for the inconvenience. For more information, visit the <a href="http://www.ernestmarples.com/blog/">Ernest Marples Blog</a>
    </div>
    <div id="divMenu">
        <ul class="collapse">
            <li {if $menu_item =="about"}class="selected"{/if}><a href="about.php">About</a></li>                                     
			<li {if $menu_item == "api"}class="selected"{/if}><a href="apihowto.php">API</a></li>

            <li {if $menu_item =="getinvolved"}class="selected"{/if}><a href="getinvolved.php">Get involved</a></li>                                       
            <li {if $menu_item =="faq"}class="selected"{/if}><a href="faq.php"><acronym title="Frequently asked questions">FAQ</acronym>s</a></li>                
            <li {if $menu_item =="signup"}class="selected"{/if}><a href="/">Signup</a></li>            
        </ul>
    </div>
    <div id="divPage">
        <div id="divHeader">
            <h1><a href="/">PlanningAlerts<span>.</span>com</a><small>beta</small></h1>
            <h2>Email alerts of planning applications <em>near you</em></h2>
            <p id="pStats">{$stats.alert_count} alerts sent for {$stats.authority_count} local authorities</p>
            <img alt="logo" title="logo" src="./images/logo.png" />
        </div>
        <div id="divContent">
            <div id="divWarning" {if $warnings == ""}class="hide"{/if}>
                {$warnings}
            </div>
            
