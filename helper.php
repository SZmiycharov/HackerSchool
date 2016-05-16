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

$query1 = "SELECT oblast AS a, ekatte AS b, name AS c, region AS d FROM ek_obl WHERE name = '{$entry}'";
$query2 = "SELECT obstina AS e, ekatte AS f, name AS g, document AS h FROM ek_obst WHERE name = '{$entry}'";
$query3 = "SELECT raion AS j, name AS k category AS l, document AS m FROM ek_raion WHERE name = '{$entry}'";
$query4 = "SELECT kmetstvo AS n, name AS o, center AS p, document AS q FROM ek_kmet WHERE name = '{$entry}'";


$result1 = pg_query($query1);
$result2 = pg_query($query2);
$result1 = pg_query($query3);
$result1 = pg_query($query4);

header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Places>'; 

// Iterate through the rows, printing XML nodes for each
while ($row1 = @pg_fetch_assoc($result1)){
  echo '<Oblast ';

  echo 'oblast="' . $row1['a'] . '" ';
  echo 'ekatte="' . $row1['b'] . '" ';
  echo 'name="' . $row1['c'] . '" ';
  echo 'region="' . $row1['d'] . '" ';
  
  echo '/>';
}
while ($row2 = @pg_fetch_assoc($result2)){
  echo '<Obstina ';

  echo 'obstina="' . $row2['e'] . '" ';
  echo 'ekatte="' . $row2['f'] . '" ';
  echo 'name="' . $row2['g'] . '" ';
  echo 'document="' . $row2['h'] . '" ';
  
  echo '/>';
}
while ($row3 = @pg_fetch_assoc($result3)){
  echo '<Raion ';

  echo 'raion="' . $row3['e'] . '" ';
  echo 'name="' . $row3['f'] . '" ';
  echo 'category="' . $row3['g'] . '" ';
  echo 'document="' . $row3['h'] . '" ';
  
  echo '/>';
}
while ($row4 = @pg_fetch_assoc($result4)){
  echo '<Kmetstvo ';

  echo 'kmetstvo="' . $row4['i'] . '" ';
  echo 'name="' . $row4['j'] . '" ';
  echo 'center="' . $row4['k'] . '" ';
  echo 'document="' . $row4['l'] . '" ';
  
  echo '/>';
}

echo '</Places>';




?>
