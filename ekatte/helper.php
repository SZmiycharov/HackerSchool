<?php

$user = 'postgres';
$passwd = '3111';
$db = 'ekatte';
$port = 5432;
$host = '';
$strCnx = "port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);

$entry = $_GET['entry'];

$query = "SELECT selishte.t_v_m, selishte.name, oblast.name as oblast, obstina.name as obstina
  FROM selishte
  INNER JOIN obstina ON selishte.obstina = obstina.obstina
  INNER JOIN oblast ON selishte.oblast = oblast.oblast
  WHERE selishte.name LIKE '{$entry}%'";
$result = pg_query($query);
header("Content-type: text/xml");

echo "<Places>"; 
while ($row = @pg_fetch_assoc($result)){
  echo '<place ';
  echo 'type="' . $row['t_v_m'] . '" ';
  echo 'name="' . $row['name'] . '" ';
  echo 'oblast="' . $row['oblast'] . '" ';
  echo 'obstina="' . $row['obstina'] . '" ';
  echo '/>';
}
echo '</Places>';

?>

