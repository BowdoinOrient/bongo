import models as archive_models
from bongo.apps.bongo import models as bongo_models
from django.utils.timezone import get_current_timezone
from django.utils.timezone import make_aware

tz = get_current_timezone()


""" Import the old ads table into the new Advertiser, Ad models """
def import_ads():
    for old_ad in archive_models.Ads.objects.using('archive').all():
        (advertiser, created) = bongo_models.Advertiser.objects.get_or_create(name=old_ad.sponsor)
        (ad, created) = bongo_models.Ad.objects.get_or_create(
            pk=old_ad.id, 
            run_from=make_aware(old_ad.start_date, tz), 
            run_through=make_aware(old_ad.end_date, tz)
        )

        if created:
            ad.url = old_ad.link
            ad.save()

            # @TODO: Address file download and re-upload with requests and boto

        else:
            # the add must have been created on a previous run of the task
            pass


""" Import the old tips table into the new Tip model """
def import_tips():
    for old_tip in archive_models.Tips.objects.using('archive').all():
        (tip, created) = bongo_models.Tip.objects.get_or_create(
            pk=old_tip.id, 
            content=old_tip.tip,
            submitted_at=make_aware(old_tip.submitted, tz)
        )

        if created:
            tip.submitted_from = old_tip.user_ip
            tip.useragent = old_tip.user_agent
            tip.save()


""" Import the old alerts table into the new Alert model """
def import_alerts():
    for old_alert in archive_models.Alerts.objects.using('archive').all():
        if not old_alert.end_date or not old_alert.start_date:
            print "Refusing to commit an alert with a null datetime"
            continue

        (alert, created) = bongo_models.Alert.objects.get_or_create(
            pk=old_alert.id,
            # They are each datetimes in the archive, this is unneccesary. Convert to date.
            run_from=old_alert.start_date,
            run_through=old_alert.end_date,
            urgent=True if old_alert.urgent == 1 else False,  # Apparently ternary expressions are "frowned upon by Pythonistas" but that's really their problem, isn't it
            message=old_alert.message
        )


""" Import the old volumes table into the new Volume model """
def import_volumes():
    for old_volume in archive_models.Volume.objects.using('archive').all():
        (volume, created) = bongo_models.Volume.objects.get_or_create(
            pk=old_volume.id,
            volume_number=old_volume.arabic,
            volume_year_start=old_volume.annodomini,  # toph.... why
            volume_year_end=old_volume.annodomini+1
        )


""" Import the old issues table into the new Issue model """
def import_issues():
    for old_issue in archive_models.Issue.objects.using('archive').all():
        (issue, created) = bongo_models.Issue.objects.get_or_create(
            pk=old_issue.id,
            issue_date=old_issue.issue_date,
            issue_number=old_issue.issue_number,
            volume=bongo_models.Volume.objects.get(volume_number__exact=old_issue.volume),
            scribd=old_issue.scribd,
            # @TODO: Host our own PDFs?
        )


""" Import the old series table into the new Series model """
def import_series():
    for old_series in archive_models.Series.objects.using('archive').all():
        (series, created) = bongo_models.Series.objects.get_or_create(
            pk=old_series.id,
            name=old_series.name
        ) 



def import_all():
    import_ads()
    import_tips()
    import_alerts()
    import_volumes()
    import_issues()
