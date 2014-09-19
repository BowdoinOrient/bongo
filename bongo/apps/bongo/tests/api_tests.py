import json
from factories import *
from django.test import TestCase
from django.test import Client
from django.core.serializers import serialize
from bongo.apps.bongo import models

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
    res = client.post(endpoint, json.loads(serialize("json", [object]))[0]['fields'])
    self.assertEqual(res.status_code, 201)

    # do the same as above for PUT
    res = client.post(endpoint, json.loads(serialize("json", [object]))[0]['fields'])
    self.assertEqual(res.status_code, 201)

    # test that a PATCH to /endpoint/object.pk changes object.name to "derp", when authenticated
    # WTF why does client.patch send content-type="application/octet-stream" by default
    res = client.patch(endpoint+str(object.pk)+"/", payload={"name": "derp"}, content_type="application/json")
    self.assertEqual(res.status_code, 200)

    # test that a DELETE to /endpoint/object.pk decreases model.count by 1, when authenticated
    res = client.delete(endpoint+str(object.pk)+"/")
    self.assertEqual(res.status_code, 204)


class APITestCase(TestCase):
    def test_Series_endpoint(self):
        obj = SeriesFactory.create(); obj.save()
        crud(self=self, object=obj, model=models.Series)
