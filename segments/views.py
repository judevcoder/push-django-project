from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from models import Segment
from django.conf import settings
from colour import Color

import json

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
      "lightColor": lightColor.hex,
      "darkColor": darkColor.hex,
      "darkestColor": darkestColor.hex,
      "buttonColor": settings.DEFAULT_DIALOG_BUTTON,
      }),
  })
  return HttpResponse(response_data, content_type = "application/json")