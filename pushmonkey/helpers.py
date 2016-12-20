from django.conf import settings

def is_demo_account(account_key):

  pass

def send_demo_notification(account_key):

  message = PushMessage(title = "Welcome to Push Monkey", 
    body = "Keep your readers engaged.", 
    url_args = "",
    account_key = account_key, 
    custom = "", 
    comment = "")
  message.save()
  message_id = message.id
  subprocess.Popen("sleep 10; python " + settings.SUBPROCESS_COMMAND_PATH  + " " + str(message_id), shell=True)

