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

$query1 = "SELECT oblast, ekatte, name, document FROM ek_obl WHERE name = '{$entry}'";
$query2 = "SELECT obstina, ekatte, name, document FROM ek_obst WHERE name = '{$entry}'";
$query3 = "SELECT raion, category, name, document FROM ek_raion WHERE name = '{$entry}'";
$query4 = "SELECT kmetstvo, center, name, document FROM ek_kmet WHERE name = '{$entry}'";

$result1 = pg_query($query1);
$result2 = pg_query($query2);
$result3 = pg_query($query3);
$result4 = pg_query($query4);

header("Content-type: text/xml");

// Start XML file, echo parent node
echo '<Places>'; 

// Iterate through the rows, printing XML nodes for each
while ($row1 = @pg_fetch_assoc($result1)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'OBLoblast="' . $row1['oblast'] . '" ';
  echo 'OBLekatte="' . $row1['ekatte'] . '" ';
  echo 'OBLname="' . $row1['name'] . '" ';
  echo 'OBLregion="' . $row1['document'] . '" ';
  
  echo '/>';
}

while ($row2 = @pg_fetch_assoc($result2)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'OBSTobstina="' . $row2['obstina'] . '" ';
  echo 'OBSTekatte="' . $row2['ekatte'] . '" ';
  echo 'OBSTname="' . $row2['name'] . '" ';
  echo 'OBSTdocument="' . $row2['document'] . '" ';
  
  echo '/>';
}

while ($row3 = @pg_fetch_assoc($result3)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'RAIraion="' . $row3['raion'] . '" ';
  echo 'RAIname="' . $row3['name'] . '" ';
  echo 'RAIcategory="' . $row3['category'] . '" ';
  echo 'RAIdocument="' . $row3['document'] . '" ';
  
  echo '/>';
}

while ($row4 = @pg_fetch_assoc($result4)){
  // ADD TO XML DOCUMENT NODE
  echo '<place ';

  echo 'KMETkmetstvo="' . $row4['kmetstvo'] . '" ';
  echo 'KMETcenter="' . $row4['center'] . '" ';
  echo 'KMETname="' . $row4['name'] . '" ';
  echo 'KMETdocument="' . $row4['document'] . '" ';
  
  echo '/>';
}

// End XML file
echo '</Places>';





?>
