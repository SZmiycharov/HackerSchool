<?php
$servername = "10.20.1.151";
$username = "slavi";
$password = "3111";
$database="ekatte";


$user = 'slavi';
$passwd = '3111';
$db = 'ekatte';
$port = 5432;
$host = '10.20.1.151';

$strCnx = "host=$host port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);

function parseToXML($htmlStr)
{
$xmlStr=str_replace('<','&lt;',$htmlStr);
$xmlStr=str_replace('>','&gt;',$xmlStr);
$xmlStr=str_replace('"','&quot;',$xmlStr);
$xmlStr=str_replace("'",'&#39;',$xmlStr);
$xmlStr=str_replace("&",'&amp;',$xmlStr);
return $xmlStr;
}


$entry = $_GET['entry'];


$query = "SELECT * FROM ek_obl WHERE name ='{$entry}'";
$result = pg_query($query);
header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Coordinates>'; 

// Iterate through the rows, printing XML nodes for each
while ($row = @pg_fetch_assoc($result)){
  // ADD TO XML DOCUMENT NODE
  echo '<coord ';

  echo 'oblast="' . $row['oblast'] . '" ';
  echo 'name="' . $row['name'] . '" ';
  echo 'region="' . $row['region'] . '" ';
  echo 'document="' . $row['document'] . '" ';
  
  echo '/>';
}

// End XML file
echo '</Coordinates>';


?>
