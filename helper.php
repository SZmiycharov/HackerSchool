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

$entry = $_GET['entry'];

$query = "SELECT oblast AS a, ekatte AS b, name AS c, region AS d FROM ek_obl WHERE name = '{$entry}'
UNION
SELECT obstina AS a, ekatte as b, name AS c, document AS d FROM ek_obst WHERE name ='{$entry}'
UNION
SELECT kmetstvo AS a, center as b, name AS c, document AS d FROM ek_kmet WHERE name ='{$entry}'
UNION
SELECT category AS a, raion as b, name AS c, document AS d FROM ek_raion WHERE name ='{$entry}'";


$result = pg_query($query);
header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Places>'; 

// Iterate through the rows, printing XML nodes for each
while ($row = @pg_fetch_assoc($result)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'oblast="' . $row['a'] . '" ';
  echo 'name="' . $row['b'] . '" ';
  echo 'region="' . $row['c'] . '" ';
  echo 'document="' . $row['d'] . '" ';
  
  echo '/>';
}

// End XML file
echo '</Places>';


?>
