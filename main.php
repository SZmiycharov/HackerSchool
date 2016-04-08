<!DOCTYPE html >
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>PHP/MySQL & Google Maps Example</title>
    <script src="https://maps.googleapis.com/maps/api/js?sensor=false"
            type="text/javascript"></script>
    <script type="text/javascript">
    //<![CDATA[

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

      // Change this depending on the name of your PHP file
      downloadUrl("http://localhost/halo.php?longitude=-116.8613333", function(data) {
        var xml = data.responseXML;
        var markers = xml.documentElement.getElementsByTagName("coord");
        for (var i = 0; i < markers.length; i++) {
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("latitude")),
              parseFloat(markers[i].getAttribute("longitude")));
          var html = "<b> test </b>";
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
    <div id="map" style="width: 1000px; height: 600px"></div>
  </body>

</html>
