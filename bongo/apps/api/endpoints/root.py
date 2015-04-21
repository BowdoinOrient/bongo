from __future__ import unicode_literals

from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    """# Bongo API
    The Bongo API is a RESTful interface to the following data models. Navigate to
    the route for each to browse individual documentation on each resource.
    Some features of the API require authentication to access. If you do not
    posess a username/password or an authentication token, contact [Brian](mailto:bjacobel@gmail.com).
    ---
    """

    return Response(OrderedDict([
        ('series', reverse("series-list", request=request, format=format)),
        ('volume', reverse("volume-list", request=request, format=format)),
        ('issue', reverse("issue-list", request=request, format=format)),
        ('section', reverse("section-list", request=request, format=format)),
        ('tag', reverse("tag-list", request=request, format=format)),
        ('job', reverse("job-list", request=request, format=format)),
        ('creator', reverse("creator-list", request=request, format=format)),
        ('text', reverse("text-list", request=request, format=format)),
        ('video', reverse("video-list", request=request, format=format)),
        ('pdf', reverse("pdf-list", request=request, format=format)),
        ('photo', reverse("photo-list", request=request, format=format)),
        ('html', reverse("html-list", request=request, format=format)),
        ('pullquote', reverse("pullquote-list", request=request, format=format)),
        ('post', reverse("post-list", request=request, format=format)),
        ('alert', reverse("alert-list", request=request, format=format)),
        ('advertiser', reverse("advertiser-list", request=request, format=format)),
        ('ad', reverse("ad-list", request=request, format=format)),
        ('tip', reverse("tip-list", request=request, format=format)),
        ('event', reverse("event-list", request=request, format=format)),
        ('scheduledpost', reverse("scheduledpost-list", request=request, format=format)),
        ('search', reverse("search", request=request, format=format)),
    ]))