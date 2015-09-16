from django.contrib import admin
from bongo.apps.archive.models import *


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'archive'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(
            db_field, request=request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, using=self.using, **kwargs
        )


# admin.site.register(Ads, MultiDBModelAdmin)
# admin.site.register(Alerts, MultiDBModelAdmin)
# admin.site.register(Article, MultiDBModelAdmin)
# admin.site.register(Articleauthor, MultiDBModelAdmin)
# admin.site.register(Articlebody, MultiDBModelAdmin)
# admin.site.register(Articletype, MultiDBModelAdmin)
# admin.site.register(Attachments, MultiDBModelAdmin)
# admin.site.register(Author, MultiDBModelAdmin)
# admin.site.register(Issue, MultiDBModelAdmin)
# admin.site.register(Job, MultiDBModelAdmin)
# admin.site.register(Links, MultiDBModelAdmin)
# admin.site.register(Photo, MultiDBModelAdmin)
# admin.site.register(Quote, MultiDBModelAdmin)
# admin.site.register(Related, MultiDBModelAdmin)
# admin.site.register(Section, MultiDBModelAdmin)
# admin.site.register(Series, MultiDBModelAdmin)
# admin.site.register(Tips, MultiDBModelAdmin)
# admin.site.register(Volume, MultiDBModelAdmin)
