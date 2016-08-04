<?php

$user = 'postgres';
$passwd = '3111';
$db = 'ekatte';
$port = 5432;
$host = '';
$strCnx = "port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);

$entry = $_GET['entry'];

$query = "SELECT selishta.t_v_m, selishta.name, oblasti.name as oblast, obstini.name as obstina
  FROM selishta
  INNER JOIN obstini ON selishta.obstina_kod = obstini.obstina_kod
  INNER JOIN oblasti ON selishta.oblast_kod = oblasti.oblast_kod
  WHERE selishta.name LIKE '{$entry}%'";

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

