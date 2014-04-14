from django.contrib import admin
from models import *

# Some of these we will definitely want to customize later
# But for now the default admin view is fine
admin.site.register(Series)
admin.site.register(Volume)
admin.site.register(Issue)
admin.site.register(Creator)
admin.site.register(Text)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(HTML)
admin.site.register(Post)
admin.site.register(Alert)
admin.site.register(Advertiser)
admin.site.register(Ad)