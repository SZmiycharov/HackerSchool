<!DOCTYPE html >
  <head>
    	<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    	<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    	<title>Ekatte places</title>
	<script src="http://code.jquery.com/jquery-latest.js"
            type="text/javascript"></script>
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  	<script src="//code.jquery.com/jquery-1.10.2.js"></script>
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>

<script type="text/javascript">

function getParameterByName(name, url) 
{
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)", "i"),
    results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function downloadUrl(url, callgetParameterByNameback) 
{
	var request = window.ActiveXObject ?
	new ActiveXObject('Microsoft.XMLHTTP') :
	new XMLHttpRequest;
	request.onreadystatechange = function() 
	{
        	if (request.readyState == 4) 
		{
          		callgetParameterByNameback(request, request.status);
  		}
	};
	request.open('GET', url, true);
	request.send(null);
}

function myFunction() 
{
	console.log("Start of myfunction");
	var input = document.getElementById('mySearch').value;
	var url = "http://10.20.1.151/helper.php?entry=" + document.getElementById('mySearch').value;
	$.ajax({
		type: "GET",
		crossDomain: true,
		url: "http://10.20.1.151/helper.php?entry=" + document.getElementById('mySearch').value,
		dataType: "xml",
		success: function(xml) 
		{		
			console.log("start of ajax success");	
			downloadUrl(url, function(data) 
			{		
      				var xml = data.responseXML;
        			var helper = xml.documentElement.getElementsByTagName("place");
				//ASSERT(helper !== null); // slavi
				
				var ul = document.getElementById("list");
  				
				$(list).empty();
        			for (var i = 0; i < helper.length; i++) 
				{   //TRACE("Option", i, option);
					//option to be displayed properly
					console.log("in for cycle");

					var li = document.createElement("li");
 					li.appendChild(document.createTextNode(helper[i].getAttribute("oblast") + " "));
					li.appendChild(document.createTextNode(helper[i].getAttribute("name") + " "));
					li.appendChild(document.createTextNode(helper[i].getAttribute("region") + " "));
					li.appendChild(document.createTextNode(helper[i].getAttribute("document") + " "));
  					ul.appendChild(li);

					console.log("index at current iteration: " + i);
					console.log("second attribute at current iteration: " + helper[i].getAttribute("name"));
       				}
				
     			 });
		},
    		error: function (jqXHR, textStatus, error) 
		{
        		console.log('Error: ' + error.message);
       			alert("ERROR" + error.message);
       		}
	});
}


</script>
</head>

<body onload="load()">
<p>Enter:</p>
<input type="search" id="mySearch" placeholder="Search for place..">

<button onclick="myFunction()">Search</button>

<p id="places"></p>

<ul id = "list"></ul> 



</body>
</html>