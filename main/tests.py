from urllib import response
from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_Exist(self):
        response =  Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_templates(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')