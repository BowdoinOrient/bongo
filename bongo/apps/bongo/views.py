from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.files.storage import default_storage as storage
from django.shortcuts import render
from django.conf import settings
import re

def custom404(request):
    # detect requests for photos we think we have, reroute them
    if re.match("/media/photos/", request.path):
        requested_photo = re.split("/", request.path)[-1]
        requested_photo = re.split("_", requested_photo)
        photo_id = requested_photo[0]

        if storage.exists("photos/"+photo_id+".jpg"):
            photo_size = requested_photo[1][:-4]
            with storage.open("photos/"+photo_id+".jpg", 'rb') as f:
                return HttpResponse(f.read(), content_type="image/jpeg")

    return render(request, "custom404.html", status=404)

