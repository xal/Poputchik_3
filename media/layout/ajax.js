function retrieveRoutes(map, handler) {
	
  ($.ajax({
      url: 'data.json',
      dataType: "json",
      success : function(data) {
            


      	    handler(data);

            return data;
        },
      error: function(xhr, status, error) {
		  var err = eval("(" + xhr.responseText + ")");
		  alert(err.Message);
		}
}));


	 
}
