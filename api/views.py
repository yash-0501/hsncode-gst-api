from django.shortcuts import render
from xltojson import getData
from django.http import HttpResponse
import json

# Create your views here.
def get_gst(request, hsn):
    if request.method == "GET":
        try:
            data = getData(hsn)
            response = json.dumps(data)
        except:
            response = json.dumps([{'error':'Invalid HSN'}])
    return HttpResponse(response, content_type='text/json')