<?php

if (isset($_SERVER['HTTP_ORIGIN'])) {
    //header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
    header("Access-Control-Allow-Origin: *");
    header('Access-Control-Allow-Credentials: true');    
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS"); 
}   
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD']))
        header("Access-Control-Allow-Methods: GET, POST, OPTIONS");         
    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
        header("Access-Control-Allow-Headers:{$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");

    exit(0);
} 


$q=$_GET["q"];

$db = new SQLite3('/home/slavi/Desktop/HackerSchool/website/db.sqlite3');
$results = $db->query("SELECT DISTINCT model FROM (
						SELECT model,  1 as ordering FROM store_product WHERE model LIKE '{$q}%'
						UNION 
						SELECT model, 2 as ordering FROM store_product WHERE model LIKE '%{$q}%')
						ORDER BY ordering
						LIMIT 5");

while ($row = $results->fetchArray()) {
	if ($hint=="")
	{
		  $hint="<a href='" .
          "http://svzmobile.com'" .
          "' target='_blank'>" .
          $row['model'] . "</a>";
	}
	else 
	{
          $hint=$hint . "<br /><a href='" .
          "http://svzmobile.com'" .
          "' target='_blank'>" .
          $row['model'] . "</a>";
    }  
}

if ($hint=="") {
  $response="no suggestion";
} else {
  $response=$hint;
}

echo $response;
?> 