from __future__ import print_function

from bongo.apps.archive import models as archive_models
from bongo.apps.bongo import models as bongo_models
from bongo.apps.bongo.helpers import strip_tags
from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage as storage
from django.utils.timezone import make_aware
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.test import override_settings
from django.db import connection
from django.conf import settings
from datetime import datetime
from optparse import make_option
from ipdb import launch_ipdb_on_exception
import pytz
import requests

options = None
session = None

tz = pytz.timezone('America/New_York')
cursor = connection.cursor()


def memcheck():
    """Checks memory usage; this script used to run out of memory so this reporting was helpful.
    Now the script runs out of CPU instead! slow clap

    """

    import resource
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000.0


def staticfiler(obj, filename, local_path, remote_uri):
    """couple of cases here:
      - file already exists on the system, has filesize of 0
      - file already exists on system, has a filesize > 0
      - file does not exist, nodownload is set
      - file does not exist, nodownload is off, reading from local copy fails
      - file does not exist, nodownload is off, download succeeds

    """

    global options
    global session

    if options.get("verbose"):
        print("looking for file {}...".format(filename), end = " ")

    stale_copy = False
    if storage.exists(local_path):
        if options.get("verbose"):
            print("It already exists", end = "")
        if storage.size(local_path) > 0 or options.get("ign_empt"):
            stale_copy = storage.open(local_path, 'rb')
            f = ContentFile(stale_copy.read())
            stale_copy.close()
            if options.get("verbose"):
                print("")
        else:
            if options.get("verbose"):
                print(", but its filesize is 0.")
        storage.delete(local_path)

    if not stale_copy and not options.get('nodownload'):
        if options.get("verbose"):
            print("Getting it from bowdoinorient.com/{}...".format(remote_uri), end = " ")

        try:
            r = session.get("http://bowdoinorient.com/" + remote_uri, timeout = 1)

            if r.status_code == 200:
                f = ContentFile(r.content)
            else:
                if options.get("verbose"):
                    print('Failed because of a {} response code'.format(r.status_code))
                f = ContentFile("")
        except requests.exceptions.RequestException as e:
            if options.get("verbose"):
                print(e)
            f = ContentFile("")

    elif not stale_copy and options.get('nodownload'):
        if options.get("verbose"):
            print("Faking the download.")
        f = ContentFile("")

    obj.save(filename, f)
    f.close()


def datetimeify(d):
    """Convert a date to a datetime, do nothing to a datetime"""
    if d.__class__.__name__ == "datetime":
        return d
    elif d.__class__.__name__ == "date":
        return datetime.combine(d, datetime.min.time())
    else:
        raise Exception("Things are really fucked: datetimeify called with a " + d.__class__.__name__)


def import_ads():
    """ Import the old ads table into the new Advertiser, Ad models
    There aren't actually any, so this is pointless

    """

    global options
    for old_ad in archive_models.Ads.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing ad #{}".format(old_ad.pk))

        (advertiser, created) = bongo_models.Advertiser.objects.get_or_create(
            imported = True,
            name = old_ad.sponsor
        )
        (ad, created) = bongo_models.Ad.objects.get_or_create(
            imported = True,
            pk = old_ad.id,
            run_from = make_aware(datetimeify(old_ad.start_date), tz),
            run_through = make_aware(datetimeify(old_ad.end_date), tz),
            url = old_ad.link,
            owner = advertiser,
        )

        staticfiler(
            ad.adfile,
            old_ad.filename,
            "ads/" + old_ad.filename,
            "ads/" + old_ad.filename
        )
        ad.save()


def import_tips():
    """Import the old tips table into the new Tip model"""

    global options
    for old_tip in archive_models.Tips.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing tip #{}".format(old_tip.pk))

        (tip, created) = bongo_models.Tip.objects.get_or_create(
            imported = True,
            pk = old_tip.id,
            content = old_tip.tip,
            submitted_at = make_aware(datetimeify(old_tip.submitted), tz),
            submitted_from = old_tip.user_ip,
            useragent = old_tip.user_agent
        )


def import_alerts():
    """Import the old alerts table into the new Alert model"""

    global options
    for old_alert in archive_models.Alerts.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing alert #{}".format(old_alert.pk))

        if not old_alert.end_date or not old_alert.start_date:
            if options.get("verbose"):
                print("Refusing to commit an alert with a null datetime")
            continue

        (alert, created) = bongo_models.Alert.objects.get_or_create(
            imported = True,
            pk = old_alert.id,
            run_from = old_alert.start_date,
            run_through = old_alert.end_date,
            urgent = True if old_alert.urgent == 1 else False,
            message = old_alert.message
        )


def import_volumes():
    """Import the old volumes table into the new Volume model"""

    global options
    for old_volume in archive_models.Volume.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing volume #{}".format(old_volume.pk))

        (volume, created) = bongo_models.Volume.objects.get_or_create(
            imported = True,
            pk = old_volume.id,
            volume_number = old_volume.arabic,
            volume_year_start = int(old_volume.annodomini),  # toph.... why
            volume_year_end = int(old_volume.annodomini) + 1
        )


def import_issues():
    """Import the old issues table into the new Issue model"""

    global options
    for old_issue in archive_models.Issue.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing issue #{}".format(old_issue.pk))

        try:
            vol = bongo_models.Volume.objects.get(volume_number__exact = old_issue.volume)
        except bongo_models.Volume.DoesNotExist as e:
            # Cover the cases where nobody created Volume 144 or 145 in the DB
            # @TODO: lots of magic numbers in here

            if old_issue.volume in [144, 145]:
                (vol, created) = bongo_models.Volume.objects.get_or_create(
                    id = archive_models.Volume.objects.using('archive').all().count() + old_issue.volume - 143,
                    volume_number = old_issue.volume,
                    volume_year_start = 1870 + old_issue.volume,
                    volume_year_end = 1870 + old_issue.volume + 1,
                    imported = True
                )
            else:
                raise e

        (issue, created) = bongo_models.Issue.objects.get_or_create(
            imported = True,
            pk = old_issue.id,
            issue_date = old_issue.issue_date,
            issue_number = old_issue.issue_number,
            volume = vol,
            scribd = old_issue.scribd,
            # @TODO: Host our own PDFs?
        )


def import_series():
    """Import the old series table into the new Series model"""

    global options
    for old_series in archive_models.Series.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing series #{}".format(old_series.pk))

        (series, created) = bongo_models.Series.objects.get_or_create(
            imported = True,
            pk = old_series.id,
            name = old_series.name
        )


def import_section():
    """Import the old sections table into the new Section model"""

    global options
    for old_section in archive_models.Section.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing section #{}".format(old_section.pk))

        (section, created) = bongo_models.Section.objects.get_or_create(
            imported = True,
            pk = old_section.id,
            section = old_section.shortname,
            priority = old_section.priority
        )


def import_job():
    """Import the old jobs table into the new Job model"""

    global options
    for old_job in archive_models.Job.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing job #{}".format(old_job.pk))

        (job, created) = bongo_models.Job.objects.get_or_create(
            imported = True,
            pk = old_job.id,
            title = strip_tags(old_job.name).title(),
        )


def import_attachment():
    global options
    for old_attachment in archive_models.Attachments.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing attachment #{}".format(old_attachment.pk))

        if old_attachment.id <= 5:
            # Attachments 1-5 are absent in the current frontend and have the wrong content1/content2
            # ordering. I'm comfortable dropping them.
            continue
        else:
            if old_attachment.type == "html":
                (atchmt, created) = bongo_models.HTML.objects.get_or_create(
                    imported = True,
                    pk = old_attachment.id,
                    content = old_attachment.content1
                )
            elif old_attachment.type == "vimeo":
                (atchmt, created) = bongo_models.Video.objects.get_or_create(
                    imported = True,
                    pk = old_attachment.id,
                    host = "Vimeo",
                    uid = old_attachment.content1,
                )
            elif old_attachment.type == "youtube":
                (atchmt, created) = bongo_models.Video.objects.get_or_create(
                    imported = True,
                    pk = old_attachment.id,
                    host = "YouTube",
                    uid = old_attachment.content1,
                )
            elif old_attachment.type == "pullquote":
                (atchmt, created) = bongo_models.Pullquote.objects.get_or_create(
                    imported = True,
                    pk = old_attachment.id,
                    quote = old_attachment.content1,
                    attribution = old_attachment.content2
                )

            if old_attachment.type != "pullquote":
                atchmt.caption = old_attachment.content2
                atchmt.save()

            if old_attachment.author_id:
                creator = bongo_models.Creator.objects.get(
                    pk__exact = old_attachment.author_id
                )
                atchmt.creators.add(creator)
                atchmt.save()

            try:
                post = bongo_models.Post.objects.get(
                    pk__exact = old_attachment.article_id
                )
            except:
                if options.get("verbose"):
                    print("Attachment {} wants to connect to post {}, but that post does not exist.".format(
                        old_attachment.id,
                        old_attachment.article_id
                    ))
            if old_attachment.type == "html":
                post.html.add(atchmt)
            elif old_attachment.type == "vimeo":
                post.video.add(atchmt)
            elif old_attachment.type == "youtube":
                post.video.add(atchmt)
            elif old_attachment.type == "pullquote":
                post.pullquote.add(atchmt)
            post.save()


@override_settings(DEBUG = False)
def import_content():
    global options
    archive_articles = archive_models.Article.objects.using('archive').all().iterator()
    archive_articlebodies = archive_models.Articlebody.objects.using('archive')
    archive_articleauthors = archive_models.Articleauthor.objects.using('archive')
    archive_authors = archive_models.Author.objects.using('archive')

    for old_article in archive_articles:
        if options.get("verbose"):
            print("importing article #{}".format(old_article.pk))

        # get the Text
        try:
            old_articlebody = archive_articlebodies.filter(
                article_id = old_article.id
            ).order_by("-timestamp")[0]
        except:
            old_articlebody = None

        # get the Creator(s)

        old_authors = []
        for old_articleauthor in archive_articleauthors.filter(article_id__exact = old_article.id):
            old_authors.append(archive_authors.get(id__exact = old_articleauthor.author_id))

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

        try:
            iss = bongo_models.Issue.objects.get(
                issue_number__exact = old_article.issue_number,
                volume__exact = bongo_models.Volume.objects.get(
                    volume_number__exact = old_article.volume
                )
            )
        except bongo_models.Issue.DoesNotExist:
            # Some articles specify an issue that does not exist (cough, 9989)
            # Set their issue to be the existing issue with date closest to the article date

            iss_before = bongo_models.Issue.objects.filter(
                issue_date__gt=old_article.date_created.date()
            ).order_by('issue_date').first()

            iss_after = bongo_models.Issue.objects.filter(
                issue_date__lt=old_article.date_created.date()
            ).order_by('-issue_date').first()

            if not iss_before and not iss_after:
                raise Exception("Can't find any issues near this article's date")
            elif not iss_before:
                iss = iss_after
            elif not iss_after:
                iss = iss_before
            elif (
                old_article.date_created.date() - iss_before.issue_date >
                iss_after.issue_date - old_article.date_created.date()
            ):
                iss = iss_after
            else:
                iss = iss_before

        (post, created) = bongo_models.Post.objects.get_or_create(
            imported = True,
            pk = old_article.id,
            published = old_article.date_published,
            is_published = (
                True if old_article.published == 1 else False
            ),
            opinion = (
                True if old_article.opinion == 1 else False
            ),
            issue = iss,
            volume = bongo_models.Volume.objects.get(
                volume_number__exact = old_article.volume
            ),
            section = bongo_models.Section.objects.get(
                pk__exact = old_article.section_id
            ),
            title = old_article.title,
            views_local = old_article.views_bowdoin,
            views_global = old_article.views,
        )

        if created:
            post.created = old_article.date_created
            post.updated = old_article.date_updated

        if old_articlebody:

            (text, created) = bongo_models.Text.objects.get_or_create(
                imported = True,
                pk = old_articlebody.id,
                body = old_articlebody.body
            )

            post.text.add(text)

            if old_authors:
                for old_author in old_authors:
                    text.creators.add(bongo_models.Creator.objects.get(pk__exact = old_author.id))
                text.save()

            post.primary_type = "text"

        if old_article.series != 0:
            post.series.add(
                bongo_models.Series.objects.get(
                    pk__exact = old_article.series
                )
            )

            if post.series.all()[0].name == "Snapshot":
                post.primary_type = "photo"

        post.save(auto_dates = False)  # prevent auto-save of created and updated fields


def import_creator():
    global options
    for old_author in archive_models.Author.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing author #{}".format(old_author.pk))

        (creator, created) = bongo_models.Creator.objects.get_or_create(
            imported = True,
            pk = old_author.id,
            name = old_author.name,
        )

        if old_author.job:
            creator.job = bongo_models.Job.objects.get(pk__exact = old_author.job)
            creator.save()

        if old_author.photo:
            staticfiler(
                creator.profpic,
                slugify(old_author.name) + ".jpg",
                "headshots/" + slugify(old_author.name) + ".jpg",
                "images/authors/" + old_author.photo
            )
            creator.save()


def import_photo():
    global options
    new_ids_created = 1
    for old_photo in archive_models.Photo.objects.using('archive').all().iterator():
        if options.get("verbose"):
            print("importing photo #{}".format(old_photo.pk))

        (photo, created) = bongo_models.Photo.objects.get_or_create(
            imported = True,
            pk = old_photo.id,
            caption = old_photo.caption,
        )

        try:
            image_url = "images/{date}/{fname}".format(
                date = (old_photo.article_date if old_photo.article_date else archive_models.Article.objects.using(
                    'archive'
                ).get(id__exact = old_photo.article_id).date),
                fname = (old_photo.filename_original if old_photo.filename_original else old_photo.filename_large)
            )

            staticfiler(
                photo.staticfile,
                str(old_photo.id) + ".jpg",
                "photos/" + str(old_photo.id) + ".jpg",
                image_url
            )
        except Exception as e:
            if options.get("verbose"):
                print(e)

        # Courtesy photos have a photographer id of 1, which doesn't exist.
        # We have to come up with a new id for this photographer that doesn't interfere with any existing id
        if old_photo.photographer_id == 1:
            (photographer, created) = bongo_models.Creator.objects.get_or_create(
                imported = True,
                name = old_photo.credit,
                courtesyof = True,
                pk = archive_models.Author.objects.using('archive').latest('id').id + new_ids_created
            )
            photo.creators.add(photographer)
            new_ids_created += 1
        elif old_photo.photographer_id == 0:
            pass
        else:
            try:
                photo.creators.add(
                    bongo_models.Creator.objects.get(
                        pk__exact = old_photo.photographer_id
                    )
                )
            except:
                if options.get("verbose"):
                    print("Issues crediting this photo to author #" + str(old_photo.photographer_id))

        photo.save()

        try:
            post_owner = bongo_models.Post.objects.get(
                pk__exact = old_photo.article_id
            )
            post_owner.photo.add(photo)
            post_owner.save()
        except:
            if options.get("verbose"):
                print("The article owning this photo has been deleted.")


class Command(BaseCommand):

    help = "Echo all positional arguments."

    option_list = BaseCommand.option_list + (
        make_option(
            '--verbose',
            dest = 'verbose',
            action = 'store_true',
            default = False,
            help = "Print verbose logging."
        ),
        make_option(
            '--fake',
            dest = 'nodownload',
            action = 'store_true',
            default = False,
            help = "Fake downloading of files."
        ),
        make_option(
            '--ignore_empties',
            dest = 'ign_empt',
            action = 'store_true',
            default = False,
            help = "Do not attempt to replace empty files."
        ),
        make_option(
            '--ipdb',
            dest = 'ipdb',
            action = 'store_true',
            default = False,
            help = "Launch ipdb if an unhandled exception occurs."
        )

    )

    def handle(self, *args, **opts):
        global options
        options = opts

        global session
        session = requests.Session()

        # Dynamically append mysql db to settings

        settings.DATABASES['archive'] = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB02Orient',
            'USER': 'root',
            'PASSWORD': settings.MYSQL_PASS,
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }

        with launch_ipdb_on_exception() if options.get("ipdb") else dummy_context_mgr():
            import_ads()
            import_tips()
            import_alerts()
            import_volumes()
            import_issues()
            import_series()
            import_section()
            import_job()
            import_creator()
            import_content()
            import_attachment()
            import_photo()


class dummy_context_mgr():
    def __enter__(self):
        return None

    def __exit__(self, *args):
        return False
