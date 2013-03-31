function loadMap(containet_id, click_handler) {
   
    
    var map = new GMaps({
      div: containet_id,
      lat: 50.4225,
      lng: 30.50583,
      click: function(e) {
          click_handler(e);
        },      
    });

    map.route_state = "starting";

    return map;
 
  }

function addRouteOnMap(route) {
  map.drawRoute({
        origin: [route.coordinate_start.latitude, route.coordinate_start.longtitude],
        destination: [route.coordinate_finish.latitude, route.coordinate_finish.longtitude],
        travelMode: 'driving',
        strokeColor: '#131540',
        strokeOpacity: 0.6,
        strokeWeight: 6
      });
}

function drawRoutes(map, data) {

    routes = data['routes'];

    $.each( routes, function( i, route ) {
      addRouteOnMap(route);
       
    });
    
}
