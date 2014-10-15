from django.http import StreamingHttpResponse
from django.core.files.storage import default_storage as storage
from django.shortcuts import render
from django.conf import settings
from bongo.apps.bongo import models
import re
from PIL import Image

def custom404(request):
    # detect requests for photos we think we have, reroute them
    if re.search("photos/", request.path):
        requested_photo = re.split("/", request.path)[-1]
        requested_photo = re.split("_", requested_photo)

        if len(requested_photo) > 1:
            photo_id = requested_photo[0]
            photo_size = int(requested_photo[-1][:-4])

        else:
            photo_id = requested_photo[0][:-4]
            photo_size = None

        photo_exists = storage.exists("photos/{}.jpg".format(photo_id))
        storage.exists("photos/1002.jpg")

        if photo_exists and photo_size:
            with storage.open("photos/"+photo_id+".jpg", 'rb') as f:
                pil_img = Image.open(f)

                (cW, cH) = pil_img.size
                (nW, nH) = (photo_size, int(1.0 * cH / (1.0 * cW / photo_size)))

                resized = pil_img.resize((nW, nH))

                b = resized.tobytes("jpeg", "RGB")

                return StreamingHttpResponse(b, content_type="image/jpeg")

    return render(request, "custom404.html", status=404)

