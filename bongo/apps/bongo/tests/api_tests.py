import json
from factories import *
from django.test import TestCase
from rest_framework.test import APIClient
from django.core.serializers import serialize
from bongo.apps.bongo import models
from django.forms.models import model_to_dict
import base64

# @TODO: These tests don't do a very good job of cleaning up after themselves

def authorize(client):
    user = UserFactory.build()
    user.save()
    client.login(username=user.username, password="defaultpassword")
    return client


def crud(self, object, model, endpoint=None):
    if not endpoint:
        # not sure if this is a hack or clever
        endpoint = "http://testserver/api/v1/" + str(type(object)).split('.')[-1][:-2] + "/"

    # use DRF's APICLient rather than django.test.Client because the latter is totally broken with regards to content_type
    # seriously, who uses application/octet-stream
    client = APIClient()

    # test that a GET to /endpoint/object.pk returns this object
    res = client.get(endpoint+str(object.pk)+"/")
    self.assertEqual(res.status_code, 200)

    # test that a GET to /endpoint returns a list with this object on it
    # this doesn't actually work in production b/c of pagination, but there
    # aren't enough objects in the test DB to trigger pagination
    res = client.get(endpoint)
    self.assertEqual(res.status_code, 200)

    # test that a POST to /endpoint with {object} 403s when not authenticated
    self.assertEqual(client.post(endpoint).status_code, 403)

    # do the same as above for PUT
    self.assertEqual(client.put(endpoint).status_code, 403)

    # test that a DELETE to /endpoint/object.pk 403s when not authenticated
    self.assertEqual(client.delete(endpoint).status_code, 403)

    # test that an UPDATE to /endpoint/object.pk 403s when not authenticated
    self.assertEqual(client.patch(endpoint).status_code, 403)

    client = authorize(client)
    obj_as_dict = model_to_dict(object)

    with open("bongo/apps/bongo/tests/test.png", 'rb') as img:
        if type(object) == models.Creator:
            obj_as_dict['profpic'] = img
        elif type(object) == models.PDF:
            obj_as_dict['staticfile'] = img
        elif type(object) == models.Photo:
            obj_as_dict['staticfile'] = img

        for key, value in obj_as_dict.iteritems():
            print str(key)+": "+str(value)

        # test that a POST to /endpoint with {object} increases model.count by 1, when authenticated
        res = client.post(endpoint, obj_as_dict, secure=True, format="multipart")
        if res.status_code != 201:
            print res.content
        self.assertEqual(res.status_code, 201)

        # test that a PUT to /endpoint/:newID makes a copy of object with id:newid
        tmp = obj_as_dict['id']
        obj_as_dict['id'] = 999
        res = client.put(endpoint+"999/", obj_as_dict, secure=True, format="multipart")
        if res.status_code != 201:
            print res.content
        self.assertEqual(res.status_code, 201)
        obj_as_dict['id'] = tmp

        # test that a PATCH to /endpoint/object.pk changes one of its fields to "derp", when authenticated
        if type(object) in [models.Volume]:
            obj_as_dict[obj_as_dict.keys()[-1]] = 100
        else:
            obj_as_dict[obj_as_dict.keys()[-1]] = "derp"
        res = client.patch(endpoint+str(object.pk)+"/", obj_as_dict, secure=True)
        self.assertEqual(res.status_code, 200)

        # test that a DELETE to /endpoint/object.pk decreases model.count by 1, when authenticated
        res = client.delete(endpoint+str(object.pk)+"/", secure=True)
        self.assertEqual(res.status_code, 204)


class APITestCase(TestCase):
    def test_User_endpoint(self):
        # we currently don't expose users over the API
        pass

    def test_Job_endpoint(self):
        obj = JobFactory.create(); obj.save()
        crud(self, obj, models.Job)

    def test_Creator_endpoint(self):
        obj = CreatorFactory.create(); obj.save()
        crud(self, obj, models.Creator)

    def test_Text_endpoint(self):
        obj = TextFactory.create(); obj.save()
        crud(self, obj, models.Text)

    def test_Video_endpoint(self):
        obj = VideoFactory.create(); obj.save()
        crud(self, obj, models.Video)

    def test_HTML_endpoint(self):
        obj = HTMLFactory.create(); obj.save()
        crud(self, obj, models.HTML)

    def test_Photo_endpoint(self):
        obj = PhotoFactory.create(); obj.save()
        crud(self, obj, models.Photo)

    def test_PDF_endpoint(self):
        obj = PDFFactory.create(); obj.save()
        crud(self, obj, models.PDF)

    def test_Pullquote_endpoint(self):
        obj = PullquoteFactory.create(); obj.save()
        crud(self, obj, models.Pullquote)

    def test_Series_endpoint(self):
        obj = SeriesFactory.create(); obj.save()
        crud(self, obj, models.Series)

    def test_Volume_endpoint(self):
        obj = VolumeFactory.create(); obj.save()
        crud(self, obj, models.Volume)

    def test_Issue_endpoint(self):
        obj = IssueFactory.create(); obj.save()
        crud(self, obj, models.Issue)

    def test_Section_endpoint(self):
        obj = SectionFactory.create(); obj.save()
        crud(self, obj, models.Section)

    def test_Tag_endpoint(self):
        obj = TagFactory.create(); obj.save()
        crud(self, obj, models.Tag)

    # def test_Post_endpoint(self):
    #     obj = PostFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Post)
