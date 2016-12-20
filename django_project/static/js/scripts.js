$(function(){

  $("#try-now-button").click(function(ev) {

    ev.stopPropagation();
    $('#demo-modal').modal();
    $('head').append('<link rel="manifest" href="/IZLUX5Y42DGPW1CS7/manifest.json">');
    $("head").append('<script src="/sdk/config-IZLUX5Y42DGPW1CS7.js"></script>');
  })
});