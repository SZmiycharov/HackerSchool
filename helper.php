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


$query = "SELECT ek_atte.t_v_m, ek_atte.name, ek_obl.name as oblast, ek_obst.name as obstina
	FROM ek_atte
	INNER JOIN ek_obst ON ek_atte.obstina = ek_obst.obstina
	INNER JOIN ek_obl ON ek_atte.oblast = ek_obl.oblast
	WHERE ek_atte.name LIKE '{$entry}%'";

$result = pg_query($query);

header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Places>'; 

// Iterate through the rows, printing XML nodes for each
while ($row = @pg_fetch_assoc($result)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'type="' . $row['t_v_m'] . '" ';
  echo 'name="' . $row['name'] . '" ';
  echo 'oblast="' . $row['oblast'] . '" ';
  echo 'obstina="' . $row['obstina'] . '" ';
  
  echo '/>';
}

// End XML file
echo '</Places>';





?>
