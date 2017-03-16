from colour import Color
from django.conf import settings
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from models import Segment
from pushmonkey.models import Device, WebServiceDevice
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def segments(request, account_key):
  segments = Segment.objects.filter(account_key = account_key)
  formatted_segments = [{s.id: s.name} for s in segments]
  backgroundColor = Color(request.GET.get("backgroundColor", settings.DEFAULT_DIALOG_BACKGROUND))
  lightColor = Color(backgroundColor)
  lightColor.luminance += 0.1
  darkColor = Color(backgroundColor)
  darkColor.luminance -= 0.1
  darkestColor = Color(backgroundColor)
  darkestColor.luminance -= 0.6
  if darkestColor.luminance < 0:
    darkestColor.luminance = 0.1
  response_data = json.dumps({

    "segments": formatted_segments,
    "template": render_to_string('segments/dialog.html', {
      'segments': segments,
      'backgroundColor': backgroundColor,
      "lightColor": lightColor.hex,
      "darkColor": darkColor.hex,
      "darkestColor": darkestColor.hex,
      "buttonColor": settings.DEFAULT_DIALOG_BUTTON,
      }),
  })
  return HttpResponse(response_data, content_type = "application/json")

@csrf_exempt
def save_segments(request, account_key):
  logger.error(request)
  segments = Segment.objects.filter(id__in = request.POST.getlist("segments[]", []))
  logger.error(segments)
  token = request.POST.get("token", None)
  if len(token) == 0:
    token = None
  logger.error(token)
  if not token:
    response_data = json.dumps({"response": "no token"})
    return HttpResponse(response_data, content_type = "application/json")      
  for segment in segments:
    try:
      device = Device.objects.get(token = token, account_key = account_key)
      segment.device.add(device)
      segment.save()
    except Device.DoesNotExist:
      try:
        web_service_device = WebServiceDevice.objects.get(endpoint = token, account_key = account_key)
        segment.web_service_device.add(web_service_device)
        segment.save()        
      except WebServiceDevice.DoesNotExist:
        response_data = json.dumps({"response": "no device"})
        return HttpResponse(response_data, content_type = "application/json")      
  response_data = json.dumps({"response": "ok"})
  return HttpResponse(response_data, content_type = "application/json")  
