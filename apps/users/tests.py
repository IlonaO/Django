import time

from django.test import LiveServerTestCase, TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from nose.plugins.attrib import attr
from selenium import webdriver


@attr('db', 'selenium_test')
class SeleniumLoggingInTest(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.username = 'seleniumuser'
		self.email = 'selenium@test.com'
		self.password = 'somepassword'

	def tearDown(self):
		self.driver.quit()

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
		create_button = self.driver.find_element_by_xpath("//input[@type='submit']")
		assert create_button.get_attribute("value") == 'Create!'
		create_button.click()
		success_text = self.driver.find_elements_by_xpath('//h4')
		assert success_text[0].text == "Hurray! You've just signed in!"
		assert success_text[1].text == "Now you can log in!"
		self.driver.find_element_by_partial_link_text('Log in').click()
		username_label = self.driver.find_element_by_xpath("//label[@for='id_username']")
		assert username_label.text == 'Username'
		password_label = self.driver.find_element_by_xpath("//label[@for='id_password']")
		assert password_label.text == 'Password'
		sign_in_text = self.driver.find_elements_by_xpath('//h4')
		assert "You don't have an account?" in sign_in_text[0].text
		assert "No problem!" in sign_in_text[0].text
		username = self.driver.find_element_by_id('id_username')
		username.send_keys(self.username)
		password = self.driver.find_element_by_id('id_password')
		password.send_keys(self.password)
		self.driver.find_element_by_xpath('//input[@value="Log in!"]').click()


@attr('db')
class LoggingInTest(TestCase):
	def setUp(self):
		self.username = 'someone'
		self.email = 'test@test.com'
		self.password = 'somepassword'
		self.test_user = User.objects.create_user(username=self.username,
												  email=self.email,
												  password=self.password)
		self.test_user.save()
		self.user = User.objects.get(username="someone")
		self.client = Client()

	def tearDown(self):
		self.user.delete()
		self.client = None

	def test_login(self):
		response = self.client.post('/user/login/',
									{'username': self.username, 'email': self.email,
									 'password1': self.password, 'password2': self.password},
									follow=True)
		self.assertEqual(response.status_code, 200, "status code is not what should be")

	def test_logout(self):
		response = self.client.post('/user/logout/',
									follow=True)
		self.assertEqual(response.status_code, 200, "status code is not what should be")
		self.assertRedirects(response, '/')

	def test_create_user(self):
		response = self.client.post('/user/create/',
									{'username': 'otheruser', 'email': 'test@email.com',
									 'password1': self.password, 'password2': self.password})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'create_success.html')

	def test_create_user_with_existing_user(self):
		response = self.client.post('/user/create/',
									{'username': self.username, 'email': self.email,
									 'password1': self.password, 'password2': self.password})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'create_user.html')
		self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')

	def test_create_user_error(self):
		response = self.client.get('/user/create/',
								   {'username': 'user', 'email': 'some@mail.pl',
									'password1': self.password, 'password2': self.password})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'create_user.html')

	def test_create_success(self):
		response = self.client.post('/user/create/create_success/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'create_success.html')

	def test_reset_pass(self):
		response = self.client.post('/user/password/reset')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.is_rendered)
		self.assertTemplateUsed(response, 'reset_pass_form.html')

	def test_my_account(self):
		self.client.login(username=self.username, password=self.password)
		response = self.client.get('/user/my_account/')
		self.assertEqual(response.status_code, 200, "status code is not what should be")
		self.assertEqual(response.templates[0].name, 'my_account.html')
