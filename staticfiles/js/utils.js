$(function(){
  function extractId(s) {
    var m = /(\d+)$/.exec(s);
    return m ? m[1] : null;
  }
  
    $(".slidetabs").tabs(".images > div", {
        //effect: 'fade',
        rotate: true
    }).slideshow({interval:5000, autoplay:true});

  $('#id_products a').lightBox();
});

