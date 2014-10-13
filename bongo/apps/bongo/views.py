from django.http import StreamingHttpResponse
from django.core.files.storage import default_storage as storage
from django.shortcuts import render
from django.conf import settings
from bongo.apps.bongo import models
import re

def custom404(request):
    # detect requests for photos we think we have, reroute them
    if re.match("/media/photos/", request.path):
        requested_photo = re.split("/", request.path)[-1]
        requested_photo = re.split("_", requested_photo)

        if len(requested_photo) > 1:
            photo_id = requested_photo[0]
            photo_size = requested_photo[1][:-4]

        else:
            photo_id = requested_photo[0][:-4]
            photo_size = None

        photo_exists = storage.exists("photos/{}.jpg".format(photo_id))

        if photo_exists and photo_size:
            with storage.open("photos/"+photo_id+".jpg", 'rb') as f:
                return StreamingHttpResponse(f.read(), content_type="image/jpeg")

    return render(request, "custom404.html", status=404)

