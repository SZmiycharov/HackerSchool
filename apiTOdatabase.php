<?php
	$servername = "localhost";
	$username = "monty";
	$password = "some_pass";
	$database="wp_db";

	$connection=mysql_connect ($servername, $username, $password);
	if (!$connection) {
	  die('Not connected : ' . mysql_error());
	}

	// Set the active MySQL database
	$db_selected = mysql_select_db($database, $connection);
	if (!$db_selected) {
	  die ('Can\'t use db : ' . mysql_error());
	}

	$jsondata = file_get_contents('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson');
    	
	
	
    //convert json object to php associative array
    $data = json_decode($jsondata, true);

    foreach ($data['features'] as &$feature) {
        $longitude = $feature['geometry']['coordinates'][0];
        $latitude = $feature['geometry']['coordinates'][1];
	$time = $feature['properties']['time'];
	$place = $feature['properties']['place'];
	$place = mysql_real_escape_string($place);
	
       
		$query ="INSERT INTO `Coordinates` (`longitude`, `latitude`,`time`,`place`)
			SELECT * FROM (SELECT $longitude,$latitude,$time,'$place') AS tmp
			WHERE NOT EXISTS (
    			SELECT * FROM `Coordinates` WHERE longitude = $longitude AND latitude = $latitude
			) LIMIT 1;";
		$result = mysql_query($query);
		if (!$result) {
		  die('Invalid query: ' . mysql_error());
		}
    }
?>
