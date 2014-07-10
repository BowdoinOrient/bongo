from bongo.apps.archive import models as archive_models
from bongo.apps.bongo import models as bongo_models
from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone
from django.utils.timezone import make_aware
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.db import transaction, models
from datetime import date, datetime
import requests

tz = get_current_timezone()

def getfile(url):
    print("Downloading "+url)
    r = requests.get(url)

    if r.status_code == 200:
        return ContentFile(r.content)
    else:
        print("Error: File not found.")
        return ContentFile("")


""" Convert a date to a datetime, do nothing to a datetime """
def datetimeify(d):
    if str(type(d)) == "<type 'datetime.datetime'>":
        return d
    elif str(type(d)) == "<type 'datetime.date'>":
        return datetime.combine(d, datetime.min.time())
    else:
        raise Exception("Things are really fucked: datetimeify called with a "+str(type(d)))


""" Import the old ads table into the new Advertiser, Ad models """
def import_ads():
    for old_ad in archive_models.Ads.objects.using('archive').all():

        print ("Importing ad "+str(old_ad.id))

        (advertiser, created) = bongo_models.Advertiser.objects.get_or_create(name=old_ad.sponsor)
        (ad, created) = bongo_models.Ad.objects.get_or_create(
            pk=old_ad.id, 
            run_from=make_aware(datetimeify(old_ad.start_date), tz), 
            run_through=make_aware(datetimeify(old_ad.end_date), tz),
            url=old_ad.link,
            owner=advertiser,
        )

        ad.adfile.save(old_ad.filename, getfile("http://bowdoinorient.com/ads/"+old_ad.filename), upload_to="ads")


""" Import the old tips table into the new Tip model """
def import_tips():
    for old_tip in archive_models.Tips.objects.using('archive').all():

        print ("Importing tip "+str(old_tip.id))

        (tip, created) = bongo_models.Tip.objects.get_or_create(
            pk=old_tip.id, 
            content=old_tip.tip,
            submitted_at=make_aware(datetimeify(old_tip.submitted), tz),
            submitted_from = old_tip.user_ip,
            useragent = old_tip.user_agent
        )



""" Import the old alerts table into the new Alert model """
def import_alerts():
    for old_alert in archive_models.Alerts.objects.using('archive').all():

        if not old_alert.end_date or not old_alert.start_date:
            print "Refusing to commit an alert with a null datetime"
            continue

        print ("Importing alert "+str(old_alert.id))

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

        print ("Importing volume "+str(old_volume.id))

        (volume, created) = bongo_models.Volume.objects.get_or_create(
            pk=old_volume.id,
            volume_number=old_volume.arabic,
            volume_year_start=old_volume.annodomini,  # toph.... why
            volume_year_end=old_volume.annodomini+1
        )


""" Import the old issues table into the new Issue model """
def import_issues():
    for old_issue in archive_models.Issue.objects.using('archive').all():

        print ("Importing issue "+str(old_issue.id))

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

        print ("Importing series "+str(old_series.id))

        (series, created) = bongo_models.Series.objects.get_or_create(
            pk=old_series.id,
            name=old_series.name
        )

""" Import the old sections table into the new Section model """
def import_section():
    for old_section in archive_models.Section.objects.using('archive').all():

        print ("Importing section "+str(old_section.id))

        (section, created) = bongo_models.Section.objects.get_or_create(
            pk=old_section.id,
            section=old_section.shortname,
            priority=old_section.priority
        )

""" Import the old jobs table into the new Job model """
def import_job():
    for old_job in archive_models.Job.objects.using('archive').all():

        print ("Importing job "+str(old_job.id))

        (job, created) = bongo_models.Job.objects.get_or_create(
            pk=old_job.id,
            title=old_job.name,
        )


""" Holy shit all of these last few are interrelated so this is going to be a piece of work """

def import_attachment():
    for old_attachment in archive_models.Attachments.objects.using('archive').all():

        print ("Importing attachment "+str(old_attachment.id))

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


            # have to create the Creators before we can link them here
            import_creator()

            if old_attachment.author_id:
                creator = bongo_models.Creator.objects.get(pk__exact=old_attachment.author_id)
                atchmt.creators.add(creator)
                atchmt.save()
            
            # ditto for content
            import_content()

            post = bongo_models.Post.objects.get(pk__exact=old_attachment.article_id)
            post.content.add(atchmt)
            post.save()




""" this is complex """
def import_content():
    for old_articlebody in archive_models.Articlebody.objects.using('archive').all():

        print ("Importing old article "+str(old_articlebody.article_id))

        (text, created) = bongo_models.Text.objects.get_or_create(
            pk=old_articlebody.id,
            body=old_articlebody.body
        )

        try:
            old_article = archive_models.Article.objects.using('archive').get(pk__exact=old_articlebody.article_id)
        except:
            # Ohhh boy, an articlebody without an article. Somebody's been messing with the database.
            # Log it and move on.
            print("Article {} has a body but no entry in the Article table.".format(old_articlebody.article_id))
            continue

        # find the author of this article (different than articlebody.creator_id)
        try:
            old_articleauthor = archive_models.Articleauthor.objects.using('archive').get(article_id__exact=old_articlebody.article_id)
            text.creators.add(bongo_models.Creator.objects.get(pk__exact=old_articleauthor.author_id))
            text.save()
        except:
            # the post does not have an author, which is bad but nonfatal
            pass
 
        # If an article has no volume number, try to guess it by the year. Better than nothing. 
        # This shouldn't actually ever be invoked now that I did some manual DB cleanup
        if old_article.volume == 0:
            old_article.volume = old_article.date_created.year - 1870
        
        # If any of these fields are missing, set them to the unix epoch
        if old_article.date_created is None:
            old_article.date_created = make_aware(datetime(1970, 1, 1), tz)
        if old_article.date_updated is None:
            old_article.date_updated = make_aware(datetime(1970, 1, 1), tz)
        if old_article.date_published is None:
            old_article.date_published = make_aware(datetime(1970, 1, 1), tz)

        # if the article referenced by old_articlebody.article_id already exists, then this is a revision. Update the body only.
        try:
            bongo_models.Post.objects.get(pk__exact=old_articlebody.article_id)
            existing_post = bongo_models.Post.objects.get(pk__exact=old_articlebody.article_id)
            for existing_content in existing_post.content.all():
                existing_content.delete()
            existing_post.content.add(text)
            existing_post.save()

        except:         
            post = bongo_models.Post.objects.create(
                pk=old_article.id,
                created=old_article.date_created,
                updated=old_article.date_updated,
                published=old_article.date_published,
                is_published=(True if old_article.published == 1 else False),  # I love you Python
                opinion=(True if old_article.opinion == 1 else False),
                issue=bongo_models.Issue.objects.get(issue_number__exact=old_article.issue_number, volume__exact=bongo_models.Volume.objects.get(volume_number__exact=old_article.volume)),
                volume=bongo_models.Volume.objects.get(volume_number__exact=old_article.volume),
                section=bongo_models.Section.objects.get(pk__exact=old_article.section_id),
                title=old_article.title,
                views_local=old_article.views_bowdoin,
                views_global=old_article.views,
            )

            post.series.add(bongo_models.Series.objects.get(pk__exact=old_article.series))

            post.content.add(text)

            for old_articleauthor in archive_models.Articleauthor.objects.using('archive').filter(article_id__exact=old_article.id):
                post.creators.add(bongo_models.Creator.objects.get(pk__exact=old_articleauthor.author_id))

            post.save()


def import_creator():
    for old_author in archive_models.Author.objects.using('archive').all():

        print ("Importing author "+str(old_author.id))

        (creator, created) = bongo_models.Creator.objects.get_or_create(
            pk=old_author.id,
            name=old_author.name,
        )

        if old_author.job:
            creator.job = bongo_models.Job.objects.get(pk__exact=old_author.job)
            creator.save()

        if old_author.photo:
            creator.profpic.save(slugify(old_author.name)+".jpg", getfile("http://bowdoinorient.com/images/authors/"+old_author.photo), upload_to="headshots")


def import_photo():
    for old_photo in archive_models.Photo.objects.using('archive').all():

        print ("Importing photo "+str(old_photo.id))

        image_url = "http://bowdoinorient.com/images/{date}/{fname}".format(
            date=old_photo.article_date,
            fname=old_photo.filename_original,
        )

        (photo, created) = bongo_models.Photo.objects.get_or_create(
            caption=old_photo.caption,
            staticfile=models.ImageField(old_photo.id+".jpg", getfile(image_url), upload_to="photos/"+old_photo.article_date.year)
        )

        photo.creators.add(bongo_models.Creator.objects.get(pk__exact=old_photo.photographer_id))
        photo.save()
        
        post_owner = bongo_models.Post.objects.get(pk__exact=old_photo.article_id)
        post_owner.content.add(photo)
        post_owner.save()



class Command(BaseCommand):

    def handle(self, *args, **options):

        transaction.set_autocommit(False)
        sid = transaction.savepoint()

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

        print("So, what do you think? Take a look around and see if you think the import went OK.")
        print("To accept the import, type 'commit' below.")
        print("To abort the import, type 'rollback'.")

        resp = None
        while resp not in ['commit', 'rollback']:
            resp = raw_input("[commit/rollback]: ")

        if resp == 'rollback':
            transaction.savepoint_rollback(sid)
        elif resp == "commit":
            transaction.commit()

