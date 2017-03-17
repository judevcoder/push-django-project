from colour import Color
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from models import Segment
from django.contrib.auth.decorators import login_required
from pushmonkey.models import Device, WebServiceDevice
from clients.models import ClientProfile
from forms import SegmentForm
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
  segments = Segment.objects.filter(id__in = request.POST.getlist("segments[]", []))
  token = request.POST.get("token", None)
  if len(token) == 0:
    token = None
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
        subscription_id = token.split("/")[-1]
        endpoint = token.replace("/%s" % subscription_id, '')
        web_service_device = WebServiceDevice.objects.get(subscription_id = subscription_id, 
          endpoint = endpoint,
          account_key = account_key)
        segment.web_service_device.add(web_service_device)
        segment.save()        
      except WebServiceDevice.DoesNotExist:
        response_data = json.dumps({"response": "no device"})
        return HttpResponse(response_data, content_type = "application/json")      
  response_data = json.dumps({"response": "ok"})
  return HttpResponse(response_data, content_type = "application/json") 

@login_required
def delete(request, id):
  try:
    segment = Segment.objects.get(id = id)
    segment.delete()
  except Segment.DoesNotExist:
    pass
  return redirect((reverse('dashboard') + "?tab=segmentation"))

@login_required
def create(request):
  if request.method == "POST":
    form = SegmentForm(request.POST)
    account_key = None
    if form.is_valid():
      try:
        profile = request.user.clientprofile
        account_key = profile.account_key
      except ClientProfile.DoesNotExist:
        try:
          website = request.user.website_set.all()[0]
          account_key = website.account_key
        except IndexError:
          pass
      if account_key:
        is_duplicate = Segment.objects.filter(account_key = account_key, 
          name = form.cleaned_data.get("name")).count() > 0
        if not is_duplicate:
          Segment.objects.create(account_key = account_key,
            name = form.cleaned_data.get("name"))
          response_data = json.dumps({"response": "ok"})
          return HttpResponse(response_data, content_type = "application/json") 
  response_data = json.dumps({"response": "error"})
  return HttpResponse(response_data, content_type = "application/json") 
