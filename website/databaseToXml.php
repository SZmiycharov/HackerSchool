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

$user = 'postgres';
$passwd = '3111';
$db = 'pcstore';
$port = 5432;
$host = '';
$strCnx = "port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);

$query = "SELECT DISTINCT maker, ordering FROM (
            SELECT maker, 1 as ordering FROM store_product WHERE LOWER(maker) LIKE LOWER('{$q}%') 
            UNION 
            SELECT maker, 2 as ordering FROM store_product WHERE LOWER(maker) LIKE LOWER('%{$q}%')) as a 
          ORDER BY ordering 
          LIMIT 5";

$result = pg_query($query);

$hint = '';

while ($row = @pg_fetch_assoc($result)){
  if ($hint=="")
  {
      $hint="<a href='" .
          "http://localhost:8000/store/searchdetails?q=" . $row['maker'] .
          "' target=''>" .
          $row['maker'] . "</a>";
  }
  else 
  {
          $hint=$hint . "<br /><a href='" .
          "http://localhost:8000/store/searchdetails?q=" . $row['maker'] .
          "' target=''>" .
          $row['maker'] . "</a>";
    }  
}

if ($hint=="") {
  $response="no suggestion";
} else {
  $response=$hint;
}

echo $response;

?> 