function drawRoutes(map, data) {

    routes = data['routes'];

    $.each( routes, function( i, item ) {
       map.drawRoute({
        origin: [item.coordinate_start.latitude, item.coordinate_start.longtitude],
        destination: [item.coordinate_finish.latitude, item.coordinate_finish.longtitude],
        travelMode: 'driving',
        strokeColor: '#131540',
        strokeOpacity: 0.6,
        strokeWeight: 6
      });
    });
    
}
