$(function() {

  var chromeDefaultTitle = $("#chrome-title").html();
  var chromeDefaultMessage = $("#chrome-message").html();
  var firefoxDefaultTitle = $("#firefox-title").html();  
  var firefoxDefaultMessage = $("#firefox-message").html();    
  $('#dashboard form .form-control').unbind('keyup change input paste').bind('keyup change input paste',function(e){

    var $this = $(this);
    var val = $this.val();
    var valLength = val.length;
    var maxCount = $this.attr('maxlength');
    if(valLength>maxCount){

      $this.val($this.val().substring(0, maxCount));
    }
  }); 
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
  $("#custom-notification").submit(function(ev){

    ev.preventDefault();
    var values = $(this).serializeArray();
    var empty = false;
    $.each(values, function(i, v){

      if (v["value"].trim().length === 0) {

        empty = true;
        return;
      }
    });
    if (empty) {

      alert("All fields are required.");
      return;
    }
    var url = "/push_message";
    var data = values;
    $.ajax({
      type: "POST",
      url: url,
      data: data,
      success: function(data, status) {

        console.log(data);
        console.log(status);
        if (status == "success") {

          $('#custom-notification-success').modal();
        } else {

          $('#custom-notification-failed').modal();          
        }
      },
      error: function(req, status, error) {

        $('#custom-notification-failed').modal();          
      }
    });
  });
});