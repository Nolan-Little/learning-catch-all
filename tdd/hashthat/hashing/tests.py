from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash
from django.core.exceptions import ValidationError
import time

class FuntionalTestCase(TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        super().tearDown()
        self.browser.quit()

    def test_homepage_exists(self):
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn("Enter hash here:", self.browser.page_source)

    def test_hash_ajax(self):
        text = "testing text 2"
        self.browser.get("http://127.0.0.1:8000")
        text_element = self.browser.find_element_by_id("id_text")
        text_element.send_keys("testing text 2")
        time.sleep(5)
        hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.assertIn(hash, self.browser.page_source)

    def test_hash_of_hello(self):
        self.browser.get("http://127.0.0.1:8000")
        text = self.browser.find_element_by_id("id_text")
        text.send_keys("hello")
        self.browser.find_element_by_name("submit").click()
        self.assertIn("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", self.browser.page_source)


class UnitTestCase(TestCase):
    def test_home_page_template(self):
        res = self.client.get("/")
        self.assertTemplateUsed(res, "hashing/home.html")

    def test_hash_form(self):
        form = HashForm(data={"text": "hello"})
        self.assertTrue(form.is_valid())

    def test_hashing_result(self):
        text_hash = hashlib.sha256("hello".encode('utf-8')).hexdigest()
        self.assertEqual("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", text_hash)

    def test_hash_objects(self):
        hash = Hash()
        hash.text = "hello"
        hash.hash = hashlib.sha256(hash.text.encode('utf-8')).hexdigest()
        hash.save()

        fetched_hash = Hash.objects.get(hash=hash.hash)

        self.assertEqual(hash.text, fetched_hash.text)

    def test_form_input_saves_model(self):
        text = "testing text"
        form = HashForm(data={"text": text})
        form.save()
        self.assertTrue(Hash.objects.filter(text=text).exists())

    def test_user_post_saves_models(self):
        text = "testing text 2"
        hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.client.post("", {"text": text})
        self.assertTrue(Hash.objects.filter(text=text).exists())
        self.assertTrue(Hash.objects.filter(hash=hash).exists())

    def test_viewing_hash(self):
        hash = self.save_hash()
        response = self.client.get(f"/hash/{hash.hash}")
        self.assertContains(response, hash.text)

    def save_hash(self):
        hash = Hash()
        hash.text = "hello"
        hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        hash.save()
        return hash

    def test_bad_data(self):
        def bad_hash():
            hash = Hash()
            hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824toolong"
            hash.full_clean()
        self.assertRaises(ValidationError, bad_hash)
