<?php

$user = 'postgres';
$passwd = '3111';
$db = 'PCStore';
$port = 5432;
$host = '';
$strCnx = "port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);

$maker = $_GET['maker'];

$query = "SELECT name, id, country FROM Makers WHERE name LIKE '{$maker}%'";

$result = pg_query($query);
header("Content-type: text/xml");

echo "<Places>"; 
while ($row = @pg_fetch_assoc($result)){
  echo '<place ';
  echo 'name="' . $row['name'] . '" ';
  echo 'id="' . $row['id'] . '" ';
  echo 'country="' . $row['country'] . '" ';
  echo '/>';
}
echo '</Places>';

?>

