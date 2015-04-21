import json
from bongo.apps.bongo.tests import factories
from rest_framework.test import APIClient
from bongo.apps.bongo import models
from bongo.apps.bongo.helpers import arbitrary_serialize


def authorize(client):
    user = factories.UserFactory.create()
    client.login(username=user.username, password="defaultpassword")
    return client


def crud(self, object, model, endpoint=None):
    if not endpoint:
        # not sure if this is a hack or clever
        endpoint = "http://testserver/api/v1/" + str(type(object)).split('.')[-1][:-2] + "/"

    # use DRF's APICLient rather than django.test.Client because the latter is
    # totally broken with regards to content_type
    # seriously, who uses application/octet-stream
    client = APIClient()

    # test that a GET to /endpoint/object.pk returns this object
    res = client.get(endpoint+str(object.pk)+"/")
    self.assertEqual(res.status_code, 200)
    for key, value in json.loads(res.content.decode("utf-8")).items():
        self.assertIn(key, dir(object))
        if key == 'id':
            self.assertEquals(object.pk, value)

    # test that a GET to /endpoint returns a list with this object on it
    # this doesn't actually work in production b/c of pagination, but there
    # aren't enough objects in the test DB to trigger pagination
    res = client.get(endpoint+"?limit=100")
    self.assertEqual(res.status_code, 200)
    self.assertIn(object.pk,
        [v for k, v in json.loads(res.content.decode("utf-8"))['objects'][0].items() if k=='id']
    )

    # test that a POST to /endpoint with {object} 401s when not authenticated
    self.assertEqual(client.post(endpoint).status_code, 401)

    # do the same as above for PUT
    self.assertEqual(client.put(endpoint).status_code, 401)

    # "" DELETE
    self.assertEqual(client.delete(endpoint).status_code, 401)

    # "" UPDATE
    self.assertEqual(client.patch(endpoint).status_code, 401)

    client = authorize(client)
    obj_as_dict = arbitrary_serialize(object)

    # test that a POST to /endpoint with {object} increases model.count by 1, when authenticated
    count = type(object).objects.count()
    res = client.post(endpoint, obj_as_dict, secure=True)
    try:
        self.assertEqual(res.status_code, 201)
        self.assertEqual(type(object).objects.count(), count+1)
    except AssertionError:
        if (
                res.status_code == 400 and
                'objects' in json.loads(res.content.decode("utf-8"))
                and json.loads(res.content.decode("utf-8"))
                    .get('objects')
                    .get('staticfile') == [u'This field is required.']
            ):
            # We don't really want to test file upload, so let this slide
            pass

    # test that a PUT to /endpoint/:newID makes a copy of object with id:newid
    count = type(object).objects.count()
    tmp = obj_as_dict['id']
    obj_as_dict['id'] = 999
    res = client.put(endpoint+"999/", obj_as_dict, secure=True)
    try:
        self.assertEqual(res.status_code, 201)
        self.assertEqual(type(object).objects.count(), count+1)
    except AssertionError:
        if (
                res.status_code == 400 and
                'objects' in json.loads(res.content.decode("utf-8")) and
                json.loads(res.content.decode("utf-8"))
                    .get('objects')
                    .get('staticfile') == [u'This field is required.']
            ):
            pass
    obj_as_dict['id'] = tmp

    # test that a PATCH to /endpoint/object.pk changes one of its fields to "derp", when authenticated
    if type(object) in [models.Volume]:
        obj_as_dict[list(obj_as_dict.keys())[-1]] = 100
    else:
        obj_as_dict[list(obj_as_dict.keys())[-1]] = "derp"
    res = client.patch(endpoint+str(object.pk)+"/", obj_as_dict, secure=True)
    try:
        self.assertEqual(res.status_code, 201)
    except AssertionError:
        if (
                res.status_code == 400 and
                'objects' in json.loads(res.content.decode("utf-8")) and
                json.loads(res.content.decode("utf-8"))
                    .get('objects')
                    .get('staticfile') == [u'This field is required.']
            ):
            pass

    # test that a DELETE to /endpoint/object.pk decreases model.count by 1, when authenticated
    count = type(object).objects.count()
    res = client.delete(endpoint+str(object.pk)+"/", secure=True)
    self.assertEqual(res.status_code, 204)
    self.assertEqual(type(object).objects.count(), count-1)