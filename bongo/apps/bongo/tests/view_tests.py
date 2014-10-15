from django.test import TestCase
from django.test import Client
from factories import PhotoFactory
from django.core.files.storage import default_storage as storage

class CropperCase(TestCase):
    def test_cropper(self):
        client = Client()

        # photo doesn't exist, no size -> 404
        res = client.get("/media/photos/99999.jpg")
        self.assertEqual(res.status_code, 404)

        # photo doesn't exist, yes size -> 404
        res = client.get("/media/photos/99999_1024.jpg")
        self.assertEqual(res.status_code, 404)

        photo = PhotoFactory.build(); photo.save()

        # photo exists, no size -> 200
        res = client.get(photo.staticfile.url)
        self.assertEqual(res.status_code, 200)

        byte_len = 0
        for chunk in res.streaming_content:
            byte_len += len(chunk)

        # photo exists, yes size -> 200 and crop
        res = client.get("/media/{}_50.jpg".format(photo.staticfile.name[:-4]))
        self.assertEqual(res.status_code, 200)

        byte_len_cropped = 0
        for chunk in res.streaming_content:
            byte_len_cropped += len(chunk)

        # filesize of 50x50 should be less than that of the 100x100
        self.assertLess(byte_len_cropped, byte_len)

        # test an enlargement too, why not
        res = client.get("/media/{}_1000.jpg".format(photo.staticfile.name[:-4]))
        self.assertEqual(res.status_code, 200)

        byte_len_enlarged = 0
        for chunk in res.streaming_content:
            byte_len_enlarged += len(chunk)

        # filesize of 50x50 should be less than that of the 100x100
        self.assertGreater(byte_len_enlarged, byte_len)