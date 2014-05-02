import models as archive_models
from bongo.apps.bongo import models as bongo_models
from django.utils.timezone import get_current_timezone
from django.utils.timezone import make_aware
from django.core.files.base import ContentFile
from django.utils.text import slugify
from datetime import date
import requests

tz = get_current_timezone()


def getfile(url):
    r = requests.get(url)

    if r.status_code == 200:
        return ContentFile(r.content)
    else
        raise Exception("File not found.")




""" Import the old ads table into the new Advertiser, Ad models """
def import_ads():
    for old_ad in archive_models.Ads.objects.using('archive').all():
        (advertiser, created) = bongo_models.Advertiser.objects.get_or_create(name=old_ad.sponsor)
        (ad, created) = bongo_models.Ad.objects.get_or_create(
            pk=old_ad.id, 
            run_from=make_aware(old_ad.start_date, tz), 
            run_through=make_aware(old_ad.end_date, tz),
            url = old_ad.link
        )

        ad.adfile.save(old_ad.filename, getfile("http://bowdoinorient.com/ads/"+old_ad.filename))


""" Import the old tips table into the new Tip model """
def import_tips():
    for old_tip in archive_models.Tips.objects.using('archive').all():
        (tip, created) = bongo_models.Tip.objects.get_or_create(
            pk=old_tip.id, 
            content=old_tip.tip,
            submitted_at=make_aware(old_tip.submitted, tz),
            submitted_from = old_tip.user_ip,
            useragent = old_tip.user_agent
        )



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

""" Import the old sections table into the new Section model """
def import_section():
    for old_section in archive_models.Section.objects.using('archive').all():
        (section, created) = bongo_models.Section.objects.get_or_create(
            pk=old_section.id,
            section=old_section.shortname,
            priority=old_section.priority
        )

""" Import the old jobs table into the new Job model """
def import_job():
    for old_job in archive_models.Job.objects.using('archive').all():
        (job, created) = bongo_models.Job.objects.get_or_create(
            pk=old_job.id,
            title=old_job.name,
        )


""" Holy shit all of these last few are interrelated so this is going to be a piece of work """

def import_attachment():
    for old_attachment in archive_models.Attachments.objects.using('archive').all():
        if old_attachment.id <= 5:
            # Attachments 1-5 are absent in the current frontend and have the wrong content1/content2
            # ordering. I'm comfortable dropping them.
            continue
        else:
            if old_attachment.type == "html":
                (atchmt, created) = bongo_models.HTML.objects.get_or_create(
                    pk=old_attachment.id,
                    content=old_attachment.content1
                )
            elif old_attachment.type == "vimeo":
                (atchmt, created) = bongo_models.Video.objects.get_or_create(
                    pk=old_attachment.id,
                    host="Vimeo",
                    uid=old_attachment.content1,
                )
            elif old_attachment.type == "youtube":
                (atchmt, created) = bongo_models.Video.objects.get_or_create(
                    pk=old_attachment.id,
                    host="YouTube",
                    uid=old_attachment.content1,
                )
            elif old_attachment.type == "pullquote":
                (atchmt, created) = bongo_models.Pullquote.objects.get_or_create(
                    pk=old_attachment.id,
                    quote=old_attachment.content1,
                    attribution=old_attachment.content2
                )   

            if old_attachment.type != "pullquote":
                atchmt.caption=old_attachment.content2
                atchmt.save()

            # have to create the Posts before we can link them here
            import_content()

            # Ditto with the Creators
            import_creator()

            # this shouldn't fail now that posts have been created
            post = bongo_models.Post.objects.get(pk__exact=old_attachment.article_id)
            post.content.add(atchmt)
            post.save()

            # ditto, again
            creator = bongo_models.Creator.objects.get(pk__exact=old_attachment.author_id)
            atchmt.creators.add(creator)
            atchmt.save()



def import_content():
    pass


def import_creator():
    for old_author in archive_models.Author.objects.using('archive').all():
        (creator, created) = bongo_models.Creator.objects.get_or_create(
            name=old_author.name,
            job=bongo_models.Job.objects.get(pk__exact=old_author.job),
        )

        creator.profpic.save(slugify(old_author.name), getfile("http://bowdoinorient.com/images/authors"+old_author.photo))


def import_photo():
    for old_photo in archive_models.Photo.objects.using('archive').all():
        (photo, created) = bongo_models.Attachment.objects.get_or_create(
            caption=old_photo.caption,
        )

        image_url = "http://bowdoinorient.com/images/{date}/{fname}".format(
            date=old_photo.article_date.date.today().strftime("%Y-%m-%d"),
            fname=old_photo.filename_original,
        )

        photo.staticfile.save(slugify(old_author.name), getfile(image_url))

        photo.creators.add(bongo_models.Creator.objects.get(pk__exact=old_photo.photographer_id))
        photo.save()



def import_all():
    import_ads()
    import_tips()
    import_alerts()
    import_volumes()
    import_issues()
    import_series()
    import_section()
    import_job()
    import_attachment()
    # import_content() and import_creator() will be called by import_attachment()
    import_photo()


