<?php
$servername = "localhost";
$username = "monty";
$password = "some_pass";
$database="wp_db";

function parseToXML($htmlStr)
{
$xmlStr=str_replace('<','&lt;',$htmlStr);
$xmlStr=str_replace('>','&gt;',$xmlStr);
$xmlStr=str_replace('"','&quot;',$xmlStr);
$xmlStr=str_replace("'",'&#39;',$xmlStr);
$xmlStr=str_replace("&",'&amp;',$xmlStr);
return $xmlStr;
}

// Opens a connection to a MySQL server
$connection=mysql_connect ($servername, $username, $password);
if (!$connection) {
  die('Not connected : ' . mysql_error());
}

// Set the active MySQL database
$db_selected = mysql_select_db($database, $connection);
if (!$db_selected) {
  die ('Can\'t use db : ' . mysql_error());
}

// Select all the rows in the markers table
$longitude = addslashes($_GET['longitude']);
$fromtime = $_GET['fromtime'];
$date = DateTime::createFromFormat('m/d/Y',$fromtime);
$fromtime = $date->format("Y-m-d");
$totime = $_GET['totime'];
$date1 = DateTime::createFromFormat('m/d/Y',$totime);
$totime = $date1->format("Y-m-d");

	$query = "SELECT * FROM `Coordinates` WHERE `time` BETWEEN '$fromtime' AND '{$totime}' AND `longitude` = '{$longitude}'";

$result = mysql_query($query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}

header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Coordinates>';

// Iterate through the rows, printing XML nodes for each
while ($row = @mysql_fetch_assoc($result)){
  // ADD TO XML DOCUMENT NODE
  echo '<coord ';

  echo 'latitude="' . $row['latitude'] . '" ';
  echo 'longitude="' . $row['longitude'] . '" ';
  echo 'time="' . $row['time'] . '" ';
  echo 'place="' . $row['place'] . '" ';
  
  echo '/>';
}

// End XML file
echo '</Coordinates>';

?>
