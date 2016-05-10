<!DOCTYPE html>
<html>
<body>

<script>
function myFunction() {
	var input = document.getElementById('mySearch').value;
	$.ajax({
	type: "GET",
	url: "http://localhost/helper.php?entry=" + input,
	dataType: "xml",
	success: function(xml) 
	  {
		
		var select = $('#search-input');			
		downloadUrl(url, function(data) 
		{
       		 var xml = data.responseXML;
       		 var helper = xml.documentElement.getElementsByTagName("coord");
      		  for (var i = 0; i < helper.length; i++) 
			{
				echo(helper[i].getAttribute("longitude"));
        		}
      		});
	  },
    	error: function (jqXHR, textStatus, error) {
        console.log('Error: ' + error.message);
        alert("ERROR" + error.message);
        }
});
      }
    });
	
}
</script>

<p>Enter:</p>
<input type="search" id="mySearch" placeholder="Search for town..">

<button onclick="myFunction()">Search</button>



</body>
</html>