from django.http import JsonResponse
import json


def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data["header"] = dict(request.headers)
    data["parms"] = dict(request.GET)
    data["content_type"] = request.content_type
    return JsonResponse(data)