import models as archive_models
from bongo.apps.bongo import models as bongo_models
from django.utils.timezone import get_current_timezone
from django.utils.timezone import make_aware

tz = get_current_timezone()


""" Import the old ads table into the new Advertiser, Ad models """
def import_ads():
    for old_ad in archive_models.Ads.objects.using('archive').all():
        (advertiser, created) = bongo_models.Advertiser.objects.get_or_create(name=old_ad.sponsor)
        (ad, created) = bongo_models.Ad.objects.get_or_create(pk=old_ad.id, run_from=make_aware(old_ad.start_date, tz), run_through=make_aware(old_ad.end_date, tz))

        if created:
            ad.url = old_ad.link
            ad.save()

            # @TODO: Address file download and re-upload with requests and boto

        else:
            # the add must have been created on a previous run of the task
            pass

""" Import the old tips table into the new Tips model """
def import_tips():
    for old_tip in archive_models.Tips.objects.using('archive').all():
        (tip, created) = bongo_models.Tip.objects.get_or_create(pk=old_tip.id, content=old_tip.tip, submitted_at=make_aware(old_tip.submitted, tz))

        if created:
            tip.submitted_from = old_tip.user_ip
            tip.useragent = old_tip.user_agent
            tip.save()


def import_all():
    import_ads()
    import_tips()
