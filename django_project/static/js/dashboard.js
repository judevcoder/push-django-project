$(function() {

  var chromeDefaultTitle = $("#chrome-title").html();
  var chromeDefaultMessage = $("#chrome-message").html();
  var firefoxDefaultTitle = $("#firefox-title").html();  
  var firefoxDefaultMessage = $("#firefox-message").html();    
  $('#title').on('input', function() {

    var el = $(this);
    var val = el.val().substring(0, 20);
    if (val.length > 0) {

      $('#chrome-title').html(val);
      $('#firefox-title').html(val);
    } else {

      $('#chrome-title').html(chromeDefaultTitle);      
      $('#firefox-title').html(firefoxDefaultTitle);      
    }
  });
  $('#message').on('input', function() {

    var el = $(this);
    var val = el.val().substring(0, 80);
    if (val.length > 0) {

      $('#chrome-message').html(val);
      $('#firefox-message').html(val);      
    } else {

      $('#chrome-message').html(chromeDefaultMessage);      
      $('#firefox-message').html(firefoxDefaultMessage);            
    }
  });
  $("#code").focus(function() {
      var $this = $(this);
      $this.select();

      // Work around Chrome's little problem
      $this.mouseup(function() {
          // Prevent further mouseup intervention
          $this.unbind("mouseup");
          return false;
      });
});  
});