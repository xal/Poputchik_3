function loadMap(containet_id) {
   
    
    var map = new GMaps({
      div: containet_id,
      lat: 50.4225,
      lng: 30.50583,
      click: function(e) {
          alert('click on' + e.latLng);
        },      
    });

    return map;
 
  }
