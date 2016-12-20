$(function(){

  $("#try-now-button").click(function(ev) {

    ev.preventDefault();
    ev.stopPropagation();
    $('#demo-modal').modal();
    $('head').append('<link rel="manifest" href="/CW598XLRMJ3YUBTZI/manifest.json">');
    $("head").append('<script src="/sdk/config-CW598XLRMJ3YUBTZI.js"></script>');
  })   
});

