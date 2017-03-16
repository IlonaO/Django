import time
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoggingInTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.test_user = User.objects.create_user('admin',
                                        'test@test.com',
                                        'secret666')
        self.test_user.save()

    def tearDown(self):
        self.driver.quit()

    def test_logging_in(self):
        """Verifies logging in authenticated user"""

        self.driver.get('http://127.0.0.1:8000/user/login/')
        time.sleep(1)
        username = self.driver.find_element_by_id('id_username')
        username.send_keys('kopytko')
        password = self.driver.find_element_by_id('id_password')
        password.send_keys('haslo')
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@value="Log in!"]').click()
        time.sleep(3)