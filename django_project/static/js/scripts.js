$(function(){

  $("#try-now-button").click(function(ev) {

    ev.stopPropagation();
    $('#demo-modal').modal();
    $('head').append('<link rel="manifest" href="/AV8TFG72EMHJ5NXB0/manifest.json">');
    $("head").append('<script src="/sdk/config-AV8TFG72EMHJ5NXB0.js"></script>');
  })
});