'use strict';

var pushMonkeySWConfig = {
    version: 2,
    logging: false, // TODO: set to false when live
    host: "https://getpushmonkey.com" // TODO: add live
};

var url = pushMonkeySWConfig.host + "/push/v1/notifs/{{ account_key }}";
self.addEventListener('push', function(event) {

  event.waitUntil(fetch(url).then(function(response) {

    return response.json().then(function(data) {

      var title = data.title;
      var body = data.body;
      var icon = data.icon;
      var tag = data.id;
      return  self.registration.showNotification(title, {
            body: body,
            icon: icon,
            {% if account_key == "CW598XLRMJ3YUBTZI" %}
            image: "https://getpushmonkey.com/static/images/getpushmonkey-logo.png",
            {% endif %}
            tag: tag,
            requireInteraction: true            
        });
    });
  })
  );
});

self.addEventListener('notificationclick', function(event) {

  console.log('On notification click: ', event.notification.tag);
  // Android doesn’t close the notification when you click on it
  // See: http://crbug.com/463146
  event.notification.close();
  // This looks to see if the current is already open and
  // focuses if it is
  event.waitUntil(clients.matchAll({
    type: "window"
  }).then(function(clientList) {
    for (var i = 0; i < clientList.length; i++) {
      var client = clientList[i];
      if (client.url == '/' && 'focus' in client)
        return client.focus();
    }
    if (clients.openWindow)
      return clients.openWindow(pushMonkeySWConfig.host + '/stats/track_open/' + event.notification.tag);
  }));
});