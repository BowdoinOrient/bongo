import json
from factories import *
from django.test import TestCase
from django.test import Client
from django.core.serializers import serialize
from bongo.apps.bongo import models
from django.forms.models import model_to_dict

# @TODO: These tests don't do a very good job of cleaning up after themselves

def debug_res(res):
    print res.request.get('wsgi.input').read()


def authorize(client):
    user = UserFactory.build()
    user.save()
    client.login(username=user.username, password="defaultpassword")
    return client


def crud(self, object, model, endpoint=None):
    if not endpoint:
        # not sure if this is a hack or clever
        endpoint = "http://testserver/api/v1/" + str(type(object)).split('.')[-1][:-2] + "/"

    client = Client()

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

    # test that a POST to /endpoint with {object} increases model.count by 1, when authenticated
    import ipdb; ipdb.set_trace()
    res = client.post(endpoint, model_to_dict(object), content_type="application/json", secure=True)
    self.assertEqual(res.status_code, 201)

    # do the same as above for PUT
    res = client.post(endpoint, model_to_dict(object), content_type="application/json", secure=True)
    self.assertEqual(res.status_code, 201)

    # test that a PATCH to /endpoint/object.pk changes object.name to "derp", when authenticated
    res = client.patch(endpoint+str(object.pk)+"/", data={"id": 999}, content_type="application/json", secure=True)
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

    def test_Pullquote_endpoint(self):
        obj = PullquoteFactory.create(); obj.save()
        crud(self, obj, models.Pullquote)

    def test_Series_endpoint(self):
        obj = SeriesFactory.create(); obj.save()
        crud(self, obj, models.Series)

    # def test_Issue_endpoint(self):
    #     obj = IssueFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Issue)

    # def test_Volume_endpoint(self):
    #     obj = VolumeFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Volume)

    # def test_Section_endpoint(self):
    #     obj = SectionFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Section)

    # def test_Tag_endpoint(self):
    #     obj = TagFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Tag)

    # def test_Post_endpoint(self):
    #     obj = PostFactory.create(); obj.save()
    #     crud_tests(self, obj, models.Post)
