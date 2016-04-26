<?php
$host_name = "localhost";
$database = "wp_db"; 
$username = "monty";          
$password = "some_pass";         

try {
$dbo = new PDO('mysql:host='.$host_name.';dbname='.$database, $username, $password);
} catch (PDOException $e) {
print "Error!: " . $e->getMessage() . "<br/>";
die();
}
?
