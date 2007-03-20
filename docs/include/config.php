<?php

/* Includes for all pages*/
require_once ("smarty/Smarty.class.php");
require_once ("scraper_support.php");

/*  Config vars */
//Database
define ("DB_CONNECTION_STRING", 'mysql://root:@localhost/planning');

//Smarty
define ("SMARTY_COMPILE_DIRECTORY", '/data/vhost/planning/data/');
define ("SMARTY_TEMPLATE_DIRECTORY", '/data/vhost/planning/docs/templates/');
define ("SMARTY_PATH", '');

//PEAR
define ("PEAR_LOCATION", 'PEAR');

//URL Stuff
define ("BASE_URL", 'http://localhost.planning');
define ("DOMAIN", 'planningalerts.com');

//Scrape method (Curl vs PEAR HTTP)
define ("SCRAPE_METHOD", 'PEAR');

//Size of alert areas
define ("SMALL_ZONE_SIZE", '200');
define ("MEDIUM_ZONE_SIZE", '800');
define ("LARGE_ZONE_SIZE", '2000');
define ("ZONE_BUFFER_PERCENTAGE", '5');

//Email setup
define ("EMAIL_FROM_ADDRESS", 'planningbot@planningalerts.com');
define ("EMAIL_FROM_NAME", 'PlanningAlerts.com');

//Scraper params
define ("SCRAPE_DELAY", '5');
define ("LOG_EMAIL", 'richard@memespring.co.uk');

//Google maps key
define ("GOOGLE_MAPS_KEY", 'ABQIAAAA74qlSxRXDySLggVC9lWIbBQeWac_qjVnPmH5iTpTixX1E2xfnBR9X0On0aXuFhRdSPx42Pz0LmJzhQ');

?>