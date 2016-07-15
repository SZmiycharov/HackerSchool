<?php
/**
 * Template Name: Google Maps API
 *
 * This template is used to demonstrate how to use Google Maps
 * in conjunction with a WordPress theme.
 *
 * @since          Twenty Fifteen 1.0
 *
 * @package        Acme_Project
 * @subpackage     Twenty_Fifteen
 */
?>

<?php get_header(); ?>

<style type="text/css">
#map-canvas {
	
	width:    100%;
	height:   500px;
	
}
</style>

<div id="map-canvas"></div><!-- #map-canvas -->


<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places&signed_in=true"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

<script>

      var map;



      function initialize() {

    var mapOptions = {

      zoom: 2,

      center: {lat: -33.865427, lng: 151.196123},

      mapTypeId: google.maps.MapTypeId.TERRAIN

    };



    map = new google.maps.Map(document.getElementById('map-canvas'),

        mapOptions);



    // Create a <script> tag and set the USGS URL as the source.

    var script = document.createElement('script');



    script.src = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp';

    document.getElementsByTagName('head')[0].appendChild(script);

      }



      function eqfeed_callback(results) {

        map.data.addGeoJson(results);

      }



      // Call the initialize function after the page has finished loading

      google.maps.event.addDomListener(window, 'load', initialize);



  </script>

<?php get_footer(); ?>
