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
$stmt = $db->prepare("SELECT DISTINCT maker FROM (
            SELECT maker, 1 as ordering FROM store_product WHERE maker LIKE ?
            UNION 
            SELECT maker, 2 as ordering FROM store_product WHERE maker LIKE ?)
            ORDER BY ordering
            LIMIT 5");

$stmt->bindValue(1, "{$q}%");
$stmt->bindValue(2, "%{$q}%");


$results = $stmt->execute();

$hint = '';


while ($row = $results->fetchArray()) {
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