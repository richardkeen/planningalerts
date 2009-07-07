<?php

    require_once('tools_ini.php'); 
    require_once('application.php'); 
    require_once('DB.php');

    //initialise
    $news_mailer = new news_mailer();
    $news_mailer->run();

//class
class news_mailer {

    //Run
     function run (){

        $db = DB::connect(DB_CONNECTION_STRING);

         //Grab all the users
         $sql = "select distinct email            
             from user
             where confirmed = 1";

         $user_results = $db->getAll($sql);
         
         print "Found " . sizeof($user_results) . " to email ";

         if(sizeof($user_results) > 0){
             
             //Loop though users
             for ($i=0; $i < sizeof($user_results); $i++){ 

                    //Smarty template
                    $smarty = new Smarty;
                    $smarty->force_compile = true;
                    $smarty->compile_dir = SMARTY_COMPILE_DIRECTORY;                            
                    
                    //Get the email text
                    $email_text = $smarty->fetch(SMARTY_TEMPLATE_DIRECTORY . 'news_mail.tpl');
                    
                    //Send the email
                    if($email_text !=""){
                        //send_text_email($user_results[$i][0], EMAIL_FROM_NAME, EMAIL_FROM_ADDRESS, "PlanningAlerts needs your help",  $email_text);
send_text_email("testing@memespring.co.uk", EMAIL_FROM_NAME, EMAIL_FROM_ADDRESS, "PlanningAlerts needs your help",  $email_text);                        
                    }
                    exit;
                }

             }

         }
     
    }

?>