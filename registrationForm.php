<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$nameErr = $passwordErr =  "";
$name = $password = "";



if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
  }
  if (empty($_POST["password"])) {
    $nameErr = "Name is required";
  } else {
    $password = test_input($_POST["password"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name" value="<?php echo $name;?>">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>

  Password: <input type="text" name="password" value="<?php echo $password;?>">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  
  <input type="submit" name="submit" value="Submit">  
</form>

<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $password;
echo "<br>";


$user = 'slavi';
$passwd = '3111';
$db = 'httpAuth';
$port = 5432;
$host = '10.20.1.151';

$strCnx = "host=$host port=$port dbname=$db user=$user password=$passwd";
$cn = pg_connect($strCnx);
$result = pg_query($cn, "INSERT INTO users(username, password) VALUES('{$name}', '{$password}');");

?>

</body>
</html>