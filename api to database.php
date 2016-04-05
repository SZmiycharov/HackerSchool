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
    	
	$page = $_SERVER['http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'];
	$sec = "10";
	header("Refresh: $sec; url=$page");
	
    //convert json object to php associative array
    $data = json_decode($jsondata, true);

    foreach ($data['features'] as &$feature) {
        $longitude = $feature['geometry']['coordinates'][0];
        $latitude = $feature['geometry']['coordinates'][1];
        
		
		$query = "INSERT INTO Coordinates(longitude, latitude) VALUES ($longitude,$latitude)";
		$result = mysql_query($query);
		if (!$result) {
		  die('Invalid query: ' . mysql_error());
		}
    }
?>