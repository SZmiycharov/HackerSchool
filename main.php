<?php
/**
 * Template Name: main
 *
 * This template is used to integrate main.php file in wordpress
 *
 * @since          Twenty Fifteen 1.0
 *
 * @package        Acme_Project
 * @subpackage     Twenty_Fifteen
 */
?>



<!DOCTYPE html >
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>PHP/MySQL & Google Maps Example</title>
    <script src="https://maps.googleapis.com/maps/api/js?sensor=false"
            type="text/javascript"></script>
<script src="http://code.jquery.com/jquery-latest.js"
            type="text/javascript"></script>

    <script type="text/javascript">

    //<![CDATA[
	
    $(document).ready(function() {
	$('#search-btn').click(function() {
		var value = $('#search-input').val();
		
		window.location.href = window.location.href.split('?')[0] + '?longitude=' + value;
	});
    });	
	
    var customIcons = {
      restaurant: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_blue.png'
      },
      bar: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_red.png'
      }
    };

    function load() {
      var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(30.102261, -81.711777),
        zoom: 5
      });
      var infoWindow = new google.maps.InfoWindow;

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

	var longitude = getParameterByName('longitude')

      // Change this depending on the name of your PHP file
      downloadUrl("http://localhost/halo.php?longitude=" + longitude, function(data) {
        var xml = data.responseXML;
        var markers = xml.documentElement.getElementsByTagName("coord");
        for (var i = 0; i < markers.length; i++) {
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("latitude")),
              parseFloat(markers[i].getAttribute("longitude")));
          var html = "latitude: " + markers[i].getAttribute("latitude") + " longitude: " + markers[i].getAttribute("longitude");
          var marker = new google.maps.Marker({
            map: map,
            position: point
          });

          bindInfoWindow(marker, map, infoWindow, html);
        }
      });
    }

    function bindInfoWindow(marker, map, infoWindow, html) {
      google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
      });
    }

    function downloadUrl(url, callback) {
      var request = window.ActiveXObject ?
          new ActiveXObject('Microsoft.XMLHTTP') :
          new XMLHttpRequest;

      request.onreadystatechange = function() {
        if (request.readyState == 4) {
          
          callback(request, request.status);
        }
      };

      request.open('GET', url, true);
      request.send(null);
    }

   

    //]]>

  </script>

  </head>

  <body onload="load()">
	<input type="text" id="search-input" />

<input type="button" value="Search" id="search-btn" />


    <div id="map" style="width: 1000px; height: 600px"></div>
  </body>

</html>
