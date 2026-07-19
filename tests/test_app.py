import os
import unittest

os.environ['TESTING'] = 'true'

from app import app, mydb, TimelinePost


class AppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mydb.connect(reuse_if_open=True)
        mydb.create_tables([TimelinePost])

    @classmethod
    def tearDownClass(cls):
        mydb.drop_tables([TimelinePost])
        if not mydb.is_closed():
            mydb.close()

    def setUp(self):
        TimelinePost.delete().execute()
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Ashley" in html
        assert "/hobbies" in html
        assert "/timeline" in html

    def test_hobbies_page(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "My Hobbies" in html

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Timeline" in html

    def test_timeline(self):
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 200

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html