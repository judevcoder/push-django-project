// $(function(){

//   // $("#try-now-button").click(function(ev) {

//   //   ev.preventDefault();
//   //   ev.stopPropagation();
//   //   $('#demo-modal').modal();
//   //   $('head').append('<link rel="manifest" href="/KNYA5C86QSOPRU4XM/manifest.json">');
//   //   $("head").append('<script src="/sdk/config-KNYA5C86QSOPRU4XM.js"></script>');
//   // })   
// });


// $(function() {

//   if (window.safari) {

//     window.safari.pushNotification.requestPermission(
//       "https://www.getpushmonkey.com/push",
//       "web.com.pushmonkey.KNYA5C86QSOPRU4XM", 
//       { user: "123" }, 
//       function(p) {

//         console.log(p);
//     });  
//   }
// });

document.body.onload = function() {

    // Ensure that the user can receive Safari Push Notifications.

    if ('safari' in window && 'pushNotification' in window.safari) {

        var permissionData = window.safari.pushNotification.permission('web.com.pushmonkey.KNYA5C86QSOPRU4XM');

        checkRemotePermission(permissionData);

    }

};

 

var checkRemotePermission = function (permissionData) {

    if (permissionData.permission === 'default') {

        // This is a new web service URL and its validity is unknown.

        window.safari.pushNotification.requestPermission(

            'https://www.getpushmonkey.com', // The web service URL.

            'web.com.pushmonkey.KNYA5C86QSOPRU4XM',     // The Website Push ID.

            {}, // Data that you choose to send to your server to help you identify the user.

            checkRemotePermission         // The callback function.

        );

    }

    else if (permissionData.permission === 'denied') {

        // The user said no.
        console.log("NO!");

    }

    else if (permissionData.permission === 'granted') {

        // The web service URL is a valid push provider, and the user said yes.

        // permissionData.deviceToken is now available to use.

    }

};

