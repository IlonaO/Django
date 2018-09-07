import time
from django.test import LiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from selenium import webdriver

class SeleniumLoggingInTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.test_user = User.objects.create_user(username="someone",
        #                                      email="test@test.com",
        #                                      password='somepassword')
        # self.test_user.save()
        # self.user = User.objects.get(username="someone")
        # self.user.delete()
        self.username = 'someone'
        self.email = 'test@test.com'
        self.password = 'somepassword'

    def tearDown(self):
        self.driver.quit()
        # self.test_user.delete()

    def test_registering_and_logging_in(self):
        """Verifies new user registering and logging in and out authenticated user"""

        self.driver.get(self.live_server_url + '/user/create/')
        time.sleep(2)
        username_label = self.driver.find_element_by_xpath("//label[@for='id_username']")
        assert username_label.text == 'Username'
        email_label = self.driver.find_element_by_xpath("//label[@for='id_email']")
        assert email_label.text == 'Email'
        password1_label = self.driver.find_element_by_xpath("//label[@for='id_password1']")
        assert password1_label.text == 'Password'
        password2_label = self.driver.find_element_by_xpath("//label[@for='id_password2']")
        assert password2_label.text == 'Password confirmation'
        username_input = self.driver.find_element_by_id('id_username')
        username_input.send_keys(self.username)
        email = self.driver.find_element_by_id('id_email')
        email.send_keys(self.email)
        password = self.driver.find_element_by_id('id_password1')
        password.send_keys(self.password)
        password = self.driver.find_element_by_id('id_password2')
        password.send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@value="Create!"]').click()
        time.sleep(2)
        self.driver.get(self.live_server_url + '/user/login/')
        time.sleep(1)
        username = self.driver.find_element_by_id('id_username')
        username.send_keys(self.username)
        password = self.driver.find_element_by_id('id_password')
        password.send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@value="Log in!"]').click()
        time.sleep(2)
        # log out -> first toggle dropdown menu
        self.driver.find_element_by_class_name('dropdown-toggle').click()
        time.sleep(1)
        self.driver.find_element_by_partial_link_text('Log out').click()
        time.sleep(2)

