from django.test import TestCase
'''
from selenium import webdriver
from django.test import LiveServerTestCase

# Create your tests here.
class AdminTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()

    def tearDown(self):
        self.selenium.quit()
'''

class Admin(TestCase):
    
    def setUp(self):
        pass

    def teadDown(self):
        pass

    def test_animals_can_speak(self):
        
        self.assertEqual(2,2)
    
