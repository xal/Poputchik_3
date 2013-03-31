
  function loadMap(containet_id) {
    var latlng = new google.maps.LatLng(50.4225, 30.50583);
    var myOptions = {
      zoom: 18,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById(containet_id),myOptions);
 
    var marker = new google.maps.Marker({
      position: latlng, 
      map: map, 
      title:"Ciklum"
    }); 
 
  }
