<!DOCTYPE html >
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>PHP/MySQL & Google Maps Example</title>
    <script src="https://maps.googleapis.com/maps/api/js?sensor=false"
            type="text/javascript"></script>
<script src="http://code.jquery.com/jquery-latest.js"
            type="text/javascript"></script>
<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>

    <script type="text/javascript">

    //<![CDATA[

	function load() {
      var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(30.102261, -81.711777),
        zoom: 3
      });
      var infoWindow = new google.maps.InfoWindow;	

	
    $(document).ready(function() {
	$('#search-btn').click(function() {
		var value = $('#search-input').val();
		var value1 = $('#from').val();
		var value2 = $('#to').val();
	
	var url = "http://localhost/halo.php?longitude=" + value + "&fromtime=" + value1 + "&totime=" + value2;
	
      downloadUrl(url, function(data) 
{
        var xml = data.responseXML;
	
        var markers = xml.documentElement.getElementsByTagName("coord");
	
        for (var i = 0; i < markers.length; i++) 
	{
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("latitude")),
              parseFloat(markers[i].getAttribute("longitude")));
          var html = markers[i].getAttribute("place");
          var marker = new google.maps.Marker({
            map: map,
            position: point
          });

          bindInfoWindow(marker, map, infoWindow, html);
        }
      });
	});
    });		

  $(function() {
    $( "#from" ).datepicker({
      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 1,
      onClose: function( selectedDate ) {
        $( "#to" ).datepicker( "option", "minDate", selectedDate );
      }
    });
    $( "#to" ).datepicker({
      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 1,
      onClose: function( selectedDate ) {
        $( "#from" ).datepicker( "option", "maxDate", selectedDate );
	var fromtime = $( "#from" ).val();
	var totime = $( "#to" ).val();
	var url = "http://localhost/halo.php?fromtime=" + fromtime + "&totime=" + totime;
	$.ajax({
	type: "GET",
	url: "http://localhost/halo.php?fromtime=" + $( "#from" ).val() + "&totime=" + $( "#to" ).val(),
	dataType: "xml",
	success: function(xml) 
	  {
		
		var select = $('#search-input');	
		// dostupvane na xml elementite korektno tuk		
		 downloadUrl(url, function(data) 
{
        var xml = data.responseXML;
        var helper = xml.documentElement.getElementsByTagName("coord");
        for (var i = 0; i < helper.length; i++) 
	{
	var dropdown = document.getElementById("search-input");
        var option = document.createElement("option");
        option.text = helper[i].getAttribute("longitude");
        dropdown.add(option);
              
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
  });

    

	//function to get the jquery string
	function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)", "i"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

	var fromtime = getParameterByName('fromtime');
	var totime = getParameterByName('totime');
	var longitude = getParameterByName('longitude');
    
 	

      // Change this depending on the name of your PHP file
      
}

    function bindInfoWindow(marker, map, infoWindow, html) {
      google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
      });
    }


    function downloadUrl(url, callgetParameterByNameback) {
      var request = window.ActiveXObject ?
          new ActiveXObject('Microsoft.XMLHTTP') :
          new XMLHttpRequest;

      request.onreadystatechange = function() {
        if (request.readyState == 4) {
          
          callgetParameterByNameback(request, request.status);
        }
      };

      request.open('GET', url, true);
      request.send(null);
    }

   

    //]]>

  </script>

  </head>

  <body onload="load()">

<label for="from">Date: from</label>
<input type="text" id="from" name="from">
<label for="to">to</label>
<input type="text" id="to" name="to">
	

<p>Longitude: <select id="search-input">
<option selected="selected">

</option>
</select>



<input type="button" value="Search" id="search-btn" />

    <div id="map" style="width: 1000px; height: 600px"></div>
  </body>

</html>
