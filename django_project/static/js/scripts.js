$(function(){

  // $("#try-now-button").click(function(ev) {

  //   ev.preventDefault();
  //   ev.stopPropagation();
  //   $('#demo-modal').modal();
  //   $('head').append('<link rel="manifest" href="/KNYA5C86QSOPRU4XM/manifest.json">');
  //   $("head").append('<script src="/sdk/config-KNYA5C86QSOPRU4XM.js"></script>');
  // })   
  window.safari.pushNotification.requestPermission(
    "https://www.getpushmonkey.com/push",
    "web.com.pushmonkey.KNYA5C86QSOPRU4XM", 
  {
    url: window.location.href
  },
  function(p) {

    console.log(p);
  })
});